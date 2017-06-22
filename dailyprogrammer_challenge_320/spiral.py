#spiral.py
#Usage: To output a spiral
#
#Author: Josh Bonello

from sys import argv
from getopt import getopt, GetoptError

def main(argv):

    #Initialize input parameters
    try:
        opts,args = getopt(argv, "hi:o:",["ifile=","ofile="])
    except GetoptError:
        info = 'spiral.py -i <inputfile> -o <outputfile>'
        #print(info)
        return "GetOpt Error"

    for opt,arg in opts:
        if opt == '-h':
            info = 'spiral.py -i <inputfile> -o <outputfile>'
            #print(info)
            return info
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg


    f1 = open(inputfile)
    f2 = open(outputfile, 'a+')

    for line in f1:
        if line != "\n":
            size = int(line)
            square = [[0 for width in range(size+1)] for height in range(size+1)]
            incr = 1

            height = 0
            width = 0
            #print("Further inputs detected : ")
            for layer in range(size-1, 0, -1):
                width = size-layer-1
                height = size-layer-1
                #print("Height at start of layer : " + str(height))
                if height == size-layer-1:
                    for width in range(size-layer-1, layer):
                        if square[height][width]==0:
                            square[height][width]=incr
                            incr+=1
                        #print("X : " + str(width) + " Y : " + str(height) + " Going right")
                    width=layer
                if width == layer:
                    for height in range(size-layer-1,layer):
                        if square[height][width] == 0:
                            square[height][width]=incr
                            incr+=1
                        #print("X : " + str(width) + " Y : " + str(height) + " Going up")
                    height=layer
                if height == layer:
                    for width in range(layer, 0, -1):
                        if square[height][width] == 0:
                            square[height][width]=incr
                            incr+=1
                        #print("X : " + str(width) + " Y : " + str(height) + " Going left")
                    width=size-layer-1
                if width == size-layer-1 and height != size-layer-1:
                    for height in range(layer, size-layer-1, -1):
                        if square[height][width] == 0:
                            square[height][width]=incr
                            incr+=1
                        #print("X : " + str(width) + " Y : " + str(height) + " Going down")
                    width=size-layer
                #print("End of Layer : " + str(layer))

            #Store result for logging
            for height in range(size):
                for width in range(size+1):
                    if width+1 == size+1:
                        f2.write("\n")
                    else:
                        f2.write(str(square[height][width])+ " ")


        else:
            f2.write("\n\n")

    output = f2.read()
    print(output)
    f1.close()
    f2.close()




if __name__ == "__main__":
    main(argv[1:])