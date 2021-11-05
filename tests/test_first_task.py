from individual.first_task import sample_foo
from .context import individual
import unittest

class TestFirstTask(unittest.TestCase):
    """First task test cases"""

    def test_foo(self):
        self.assertEqual(sample_foo(2), 4) 


if __name__ == '__main__':
    unittest.main()