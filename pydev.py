import os
import sys
import subprocess
from site import getuserbase, getusersitepackages
from argparse import ArgumentParser


def development_deploy(paths, dependencies=False, scripts=False, inject_setuptools=False):
    """Python packages deployment in development mode."""
    items = list(paths) if isinstance(paths, (list, tuple, set)) else [paths]

    if items:
        original_path = os.getcwd()
        user_base_path = getuserbase()
        user_sites_path = getusersitepackages()
        user_bin_path = os.path.join(user_base_path, 'bin')

        for path in items:
            os.chdir(os.path.dirname(path))

            # Making arguments
            arguments = [path, 'develop']
            arguments.extend(['--install-dir', user_sites_path])
            arguments.extend(['--script-dir', user_bin_path])
            if not dependencies:
                arguments.append('--no-deps')
            if not scripts:
                arguments.append('--exclude-scripts')

            # Processing
            if not inject_setuptools:
                subprocess.Popen([sys.executable] + arguments).wait()
            else:
                handler = open(path, 'rb')
                content = handler.read()
                handler.close()
                # Adding setuptools import
                content = "import setuptools\n" + content
                # Updating arguments, path and executing
                sys.path.insert(0, '.')
                sys.argv = arguments
                exec(content)
                sys.path[:] = sys.path[1:]

        # Go back to original path
        os.chdir(original_path)


def execute_from_command_line():
    arg_parser = ArgumentParser(description=development_deploy.__doc__)
    arg_parser.add_argument('--deps', action='store_true',
                            help='install dependencies')
    arg_parser.add_argument('--scripts', action='store_true',
                            help='install scripts')
    arg_parser.add_argument('--inject', action='store_true',
                            help='inject setuptools call (for modules without setuptools)')
    arg_parser.add_argument('paths', metavar='path', nargs='+',
                            help='packages search path')

    # Processing
    arguments = arg_parser.parse_args()
    for path in [os.path.abspath(x) for x in arguments.paths]:
        print 'Finding packages at "{0}"...'.format(path)
        for root, dirs, files in os.walk(path):
            dirs[:] = [x for x in dirs if not x.startswith('.')]
            for file_name in files:
                file_name_lower = file_name.lower()
                if file_name_lower == 'setup.py':
                    dirs[:] = []
                    print 'Processing "{0}"'.format(root)
                    development_deploy(os.path.join(root, file_name),
                                       dependencies=arguments.deps,
                                       scripts=arguments.scripts,
                                       inject_setuptools=arguments.inject)


if __name__ == '__main__':
    execute_from_command_line()
