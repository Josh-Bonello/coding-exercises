import unittest, os, spiral


class SpiralUnitTest(unittest.TestCase):
    def test_reddit_case(self):
        self.maxDiff=None
        spiral.main(['-i', 'input.txt', '-o', 'test_reddit_output.txt'])
        f1 = open('test_reddit_output.txt')
        f2 = open('output.txt')
        self.assertEqual(f1.read(), f2.read())


    def doCleanups(self):
        try:
            os.remove('test_reddit_output.txt')
        except OSError:
            pass