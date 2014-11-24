import nose
import unittest
from pylint import epylint as lint

APPLICATION_DIR = 'application.py'

class TestApplication(unittest.TestCase):


    def test_lint(self):
        (pylint_stdout, pylint_stderr) = lint.py_run(APPLICATION_DIR, True)

if __name__ == '__main__':
    unittest.main()
