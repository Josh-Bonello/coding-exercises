import inputVariables
import unittest


class InputVariablesTestCase(unittest.TestCase):
    def test_help(self):
        result = inputVariables.main('-h')
        self.assertEqual(result.info, "inputVariables.py -i <inputfile> -o <outputfile>")
        print("I made it here")

if __name__ == '___main___':
    unittest.main()
