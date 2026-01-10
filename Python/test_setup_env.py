import unittest
import tempfile
from pathlib import Path

from setup_env import init_project


class TestSetupEnv(unittest.TestCase):
    def test_init_project_simulate(self):
        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            summary = init_project(path=td, name='myproj', create_venv=False, simulate=True)
            # Check directories and files created
            self.assertEqual(summary['project_name'], 'myproj')
            src_pkg = td_path / 'src' / 'myproj'
            self.assertTrue(src_pkg.exists() and src_pkg.is_dir())
            self.assertTrue((src_pkg / '__init__.py').exists())
            self.assertTrue((td_path / 'tests').exists())
            self.assertTrue((td_path / 'requirements.txt').exists())
            self.assertTrue((td_path / 'README.md').exists())
            self.assertTrue((td_path / '.gitignore').exists())


if __name__ == '__main__':
    unittest.main()
