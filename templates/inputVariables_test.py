import inputVariables
import unittest


class InputVariablesTestCase(unittest.TestCase):
    def test_help(self):
        result = inputVariables.main(['-h'])
        self.assertEqual(result, "inputVariables.py -i <inputfile> -o <outputfile>")

    def test_infile(self):
        result =  inputVariables.main(['-i', 'infile'])
        self.assertEqual(result, "inputfile argument is : infile\noutputfile argument is : ")

    def test_outfile(self):
        result = inputVariables.main(['-o', 'outfile'])
        self.assertEqual(result, "inputfile argument is : \noutputfile argument is : outfile")

    def test_longoptions(self):
if __name__ == '___main___':
    unittest.main()
