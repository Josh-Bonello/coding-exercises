import sys, getopt

def main(argv):
    inputfile=''
    outputfile=''
    try:
        opts,args = getopt.getopt(argv, "hi:o",["ifile=","ofile="])
    except getopt.GetoptError:
        print('inputVariables.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt,arg in opts:
        if opt=='-h':
            print('inputVariables.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--inputFile"):
            inputfile = arg
        elif opt in ("-o", "--outputFile"):
            outputfile = arg

    print "inputfile argument is : " + inputfile
    print "outputfile argument is : " + outputfile
