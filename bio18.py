import math
import numpy

def hammingDistance(a,b):
    j = 0
    for i in range(len(a)):
        if  a[i] != b[i]:
            j += 1
    return j

def testHammingDistance():
    f = open("data/dataset_9_3.txt")
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
    f = open("data/dataset_9_4.txt")
    lines = f.readlines()
    pattern = lines[0].rstrip()
    text = lines[1].rstrip()
    d = int(lines[2].rstrip())
    result = approximateOccurences(pattern,text,d)
    print(prettyint(result))

def approximatePatternCount(text,pattern,d):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        p = text[i:i+len(pattern)]
        if hammingDistance(pattern,p) <= d:
            count += 1
    return count

def testApproximatePatternCount():
    f = open("data/dataset_9_6.txt")
    lines = f.readlines()
    text = lines[0].rstrip()
    pattern = lines[1].rstrip()
    d = int(lines[2].rstrip())
    result = approximatePatternCount(text,pattern,d)
    print(result)

# def frequentWordsWithMismatch(text,k,d):
#     frequentPatterns = []
#     count = [0]*(len(text)-k+1)
#     for i in range(len(text)-k+1):
#         pattern = text[i:i+k]
#         count[i] = approximatePatternCount(text, pattern, d)
#     maxCount = max(count)
#     for i in range(len(text)-k+1):
#         if count[i] == maxCount:
#             frequentPatterns.append(text[i:i+k])
#     return set(frequentPatterns)

def frequentWordsWithMismatches(text, k, d):
    frequentPatterns = []
    close = numpy.zeros(math.pow(4,k), dtype=numpy.int)
    frequencyArray = numpy.zeros(math.pow(4,k), dtype=numpy.int)
    for i in range(len(text)-k+1):
        neighborhood = neighbors(text[i:i+k],d)
        for pattern in neighborhood:
            index = patternToNumber(pattern)
            close[index] = 1
    for i in range(len(close)):
        if close[i] == 1:
            pattern = numberToPattern(i,k)
            frequencyArray[i] = approximatePatternCount(text,pattern,d)
    maxCount = max(frequencyArray)
    for i in range(len(frequencyArray)):
        if frequencyArray[i] == maxCount:
            pattern = numberToPattern(i,k)
            frequentPatterns.append(pattern)
    return frequentPatterns

def testFrequentWordsWithMismatch():
    f = open("data/dataset_9_7.txt")
    lines = f.readlines()
    text = lines[0].rstrip()
    k,d = map(int,lines[1].rstrip().split(" "))
    result = frequentWordsWithMismatches(text,k,d)
    print(" ".join(result))

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
    
def immediateNeighbors(pattern):
    neighborhood = []
    for i in range(len(pattern)):
        symbol = pattern[i]
        bases = ["A","C","G","T"]
        bases.remove(symbol)
        for base in bases:
            neighbor = pattern[:i] + base + pattern[i+1:]
            neighborhood.append(neighbor)
    return neighborhood
    
def suffix(pattern):
    return pattern[1:]

def neighbors(pattern,d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ["A","C","G","T"]
    neighborhood = []
    suffixNeighbors = neighbors(suffix(pattern),d)
    for text in suffixNeighbors:
        if hammingDistance(suffix(pattern),text) < d:
            for x in ["A","C","G","T"]:
                neighborhood.append(x + text)
        else:
            neighborhood.append(pattern[0] + text)
        
    return neighborhood

def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    prefix = pattern[:-1]
    symbol = pattern[-1:]
    return 4*patternToNumber(prefix) + symbolToNumber(symbol)

def symbolToNumber(symbol):
    return {
        'A':0,
        'C':1,
        'G':2,
        'T':3
    }[symbol]
    
def numberToPattern(number,k):
    if k == 1:
        return numberToSymbol(number)
    quotient, remainder = divmod(number,4)
    prefixPattern = numberToPattern(quotient,k-1)
    symbol = numberToSymbol(remainder)
    return prefixPattern+symbol

def numberToSymbol(number):
    return {
        0:'A',
        1:'C',
        2:'G',
        3:'T'
    }[number]

def prettyint(x):
    return " ".join(map(str, x))