import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.string_example = 'foo'

    def test_upper(self):
        self.assertEqual(self.string_example.upper(), 'FOO')


class TestConcurrency(unittest.TestCase):
    def setUp(self):
        self.string_example = 'gee'

    def test_upper(self):
        self.assertEqual(self.string_example.upper(), 'GEE')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestConcurrency('test_upper'))
    return suite


if __name__ == '__main__':
    #unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite())
