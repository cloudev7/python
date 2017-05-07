#!/usr/local/bin/python

import sys, getopt

def main(argv):
   inputfile = str() 
   outputfile = str() 

   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print args[0] + ' -i <inputfile> -o <outputfile>'
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   print 'Input file is "%s"' %inputfile
   print 'Output file is "%s"' %outputfile

if __name__ == "__main__":
   main(sys.argv[1:])
