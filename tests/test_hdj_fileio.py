import unittest
from sample.hdj_fileio import file_check_ignored


class TestFileCheckIgnored(unittest.TestCase):
    """
    Test that file_check_ignored throws an error if tested with wrong files
    """

    def test_function(self):
        missing_file = ""
        ignored_link = ""
        self.assertRaises(
            FileNotFoundError, file_check_ignored, missing_file, ignored_link
        )
