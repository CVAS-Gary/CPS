"""
Initialize a simple Python project environment.
Creates: venv (optional), src/<project>, tests/, requirements.txt, README.md, .gitignore.

Usage:
  python setup_env.py --path myproject --name myproj
  python setup_env.py --path myproject --no-venv --simulate
"""

from pathlib import Path
import os
import venv
import subprocess


def init_project(path='.', name=None, create_venv=True, install_requirements=False, simulate=False):
    """Create a minimal Python project skeleton at path.

    If simulate is True, do not create a real virtual environment or install packages (useful for tests).
    Returns a dict with summary information.
    """
    p = Path(path).resolve()
    p.mkdir(parents=True, exist_ok=True)
    project_name = name or p.name

    # Create src package
    src_pkg = p / 'src' / project_name
    src_pkg.mkdir(parents=True, exist_ok=True)
    init_file = src_pkg / '__init__.py'
    if not init_file.exists():
        init_file.write_text(f'"""Package {project_name}"""\n')

    # Tests directory
    tests_dir = p / 'tests'
    tests_dir.mkdir(exist_ok=True)

    # README and .gitignore
    readme = p / 'README.md'
    if not readme.exists():
        readme.write_text(f'# {project_name}\n\nInitialized by setup_env.py\n')

    gitignore = p / '.gitignore'
    if not gitignore.exists():
        gitignore.write_text('venv/\n__pycache__/\n*.pyc\n')

    # requirements
    requirements = p / 'requirements.txt'
    if not requirements.exists():
        requirements.write_text('# Add project requirements here\n')

    # Virtual environment
    venv_dir = p / 'venv'
    if create_venv and not simulate:
        if not venv_dir.exists():
            venv.EnvBuilder(with_pip=True).create(str(venv_dir))

    # Install requirements if requested
    if install_requirements and not simulate:
        if os.name == 'nt':
            python_exe = venv_dir / 'Scripts' / 'python.exe'
        else:
            python_exe = venv_dir / 'bin' / 'python'
        subprocess.check_call([str(python_exe), '-m', 'pip', 'install', '-r', str(requirements)])

    return {
        'path': str(p),
        'project_name': project_name,
        'created': {
            'src_pkg': str(src_pkg),
            'tests_dir': str(tests_dir),
            'requirements': str(requirements),
            'readme': str(readme),
            'gitignore': str(gitignore),
            'venv': str(venv_dir) if create_venv else None,
        }
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Initialize a Python project skeleton')
    parser.add_argument('--path', default='.', help='Directory to initialize')
    parser.add_argument('--name', help='Project package name (defaults to directory name)')
    parser.add_argument('--no-venv', action='store_true', help='Do not create a virtual environment')
    parser.add_argument('--install', action='store_true', help='Install requirements into venv (must create venv)')
    parser.add_argument('--simulate', action='store_true', help='Simulate actions (do not create venv or install)')
    args = parser.parse_args()

    summary = init_project(path=args.path, name=args.name, create_venv=not args.no_venv,
                           install_requirements=args.install, simulate=args.simulate)
    print('Initialized project:')
    print(f"  path: {summary['path']}")
    print(f"  project_name: {summary['project_name']}")


if __name__ == '__main__':
    main()
