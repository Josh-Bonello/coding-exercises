import sys, getopt
def main(argv):
    inputfile=''
    outputfile=''
    try:
        opts,args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('inputVariables.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    print(opts)
    for opt,arg in opts:
        if opt == '-h':
            print('inputVariables.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print("inputfile argument is : " + inputfile)
    print("outputfile argument is : " + outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
