import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        string_example = 'foo'
        self.assertEqual(string_example.upper(), 'FOO')


class TestConcurrency(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()