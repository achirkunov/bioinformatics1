import math
import numpy

def read(filename):
    f = open(filename)
    lines = f.readlines()
    return lines[0].rstrip()

def hammingDistance(a,b):
    j = 0
    for i in range(len(a)):
        if  a[i] != b[i]:
            j += 1
    return j

def testHammingDistance():
    f = open("dataset_9_3.txt")
    lines = f.readlines()
    a = lines[0].rstrip()
    b = lines[1].rstrip()
    print(hammingDistance(a,b))
    
def approximateOccurences(pattern,text,d):
    k = len(pattern)
    occurences = []
    for i in range(len(text)-k+1):
        if hammingDistance(text[i:i+k],pattern) <= d:
            occurences.append(i)
    return occurences

def testApproximateOccurences():
    f = open("dataset_9_4.txt")
    lines = f.readlines()
    pattern = lines[0].rstrip()
    text = lines[1].rstrip()
    d = int(lines[2].rstrip())
    result = approximateOccurences(pattern,text,d)
    print(prettyint(result))

def skew(genome):
    values = numpy.zeros(len(genome)+1, dtype=numpy.int)
    for i in range(len(genome)):
        nucleotide = genome[i:i+1]
        if nucleotide == "C":
            values[i+1] = values[i] - 1
        elif nucleotide == "G":
            values[i+1] = values[i] + 1
        else:
            values[i+1] = values[i]
    return values

def minimumSkew(genome):
    s = skew(genome)
    return numpy.where(s == s.min())[0]

def prettyint(x):
    return " ".join(map(str, x))