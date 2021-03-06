import sys, getopt
def main(argv):
    inputfile=''
    outputfile=''
    try:
        opts,args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        info = 'inputVariables.py -i <inputfile> -o <outputfile>'
        print(info)
        return "GetOpt Error"

    for opt,arg in opts:
        if opt == '-h':
            info = 'inputVariables.py -i <inputfile> -o <outputfile>'
            print(info)
            return info
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    info ="inputfile argument is : " + inputfile + "\noutputfile argument is : " + outputfile
    print(info)
    return info


if __name__ == "__main__":
   main(sys.argv[1:])
