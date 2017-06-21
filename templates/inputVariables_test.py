import inputVariables
import unittest


class InputVariablesTestCase(unittest.TestCase):
    def test_help(self):
        result = inputVariables.main(['-h'])
        self.assertEqual(result, "inputVariables.py -i <inputfile> -o <outputfile>")

    def test_infile(self):
        result =  inputVariables.main(['-i', 'infile'])
        self.assertEqual(result, "inputfile argument is : infile\noutputfile argument is : ")

    def test_infile_longoptions(self):
        result =  inputVariables.main(['--ifile', 'infile'])
        self.assertEqual(result, "inputfile argument is : infile\noutputfile argument is : ")

    def test_outfile(self):
        result = inputVariables.main(['-o', 'outfile'])
        self.assertEqual(result, "inputfile argument is : \noutputfile argument is : outfile")

    def test_outfile_longoptions(self):
        result = inputVariables.main(['--ofile', 'outfile'])
        self.assertEqual(result, "inputfile argument is : \noutputfile argument is : outfile")

    def test_inandoutfile(self):
        result = inputVariables.main(['-i','infile','-o','outfile'])
        self.assertEqual(result, "inputfile argument is : infile\noutputfile argument is : outfile")

    def test_inandoutfile_longoptions(self):
        result = inputVariables.main(['--ifile','infile','--ofile','outfile'])
        self.assertEqual(result, "inputfile argument is : infile\noutputfile argument is : outfile")
if __name__ == '___main___':
    unittest.main()
