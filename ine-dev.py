#!/home/vagrant/data/devops/env/bin/python

import glob
import re

fileList = glob.glob('*bb*.txt')
pattern = re.compile(r'router bgp.*no ip http server', re.DOTALL)

# inputFileName = 'rsrack1.bb2.txt'

def inOutFiles(inputFileName, pattern):
        inputFile = open(inputFileName)
        outputFile = open(inputFileName.split('.txt')[0] + '.output.txt', 'w')

        text = inputFile.read()
        result = re.search(pattern, text)
        inputFile.close()

        s = result.start()
        e = result.end() - 18
        # print text[s:e]

        outputFile.write(text[s:e])
        outputFile.close()

if __name__ == '__main__':
    for f in fileList:
        inOutFiles(f, pattern)
