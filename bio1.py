import numpy
import math

def symbolToNumber(symbol):
    return {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }[symbol]

def numberToSymbol(number):
    return {
        0: "A",
        1: "C",
        2: "G",
        3: "T"
    }[number]

def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    a = pattern[:-1]
    b = pattern[-1:]
    return 4*patternToNumber(a) + symbolToNumber(b)

def numberToPattern(number,k):
    if k == 1:
        return numberToSymbol(number)
    quotient, remainder = divmod(number,4)
    prefixPattern = numberToPattern(quotient,k-1)
    symbol = numberToSymbol(remainder)
    return prefixPattern+symbol

def computingFrequencies(text, k):
    frequencyArray = numpy.zeros( math.pow(4,k), dtype=numpy.int )
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        j = patternToNumber(pattern)
        frequencyArray[j] += 1
        
    return frequencyArray

def betterClumpFinding(genome, k, L, t):
    frequentPatterns = []
    clump = numpy.zeros( math.pow(4,k), dtype=numpy.int )
    text = genome[0:L]
    frequencyArray = computingFrequencies(text,k)
    for i in range(len(clump)):
        if frequencyArray[i] >= t
            clump[i] = 1
    for i in range(1,len(genome)-L+1):
        firstPattern = genome[i-1:i-1+k]
        j = patternToNumber(firstPattern)
        frequencyArray[j] = frequencyArray[j] - 1
        lastPattern = genome[i+L-k:i+L]
    
    for i in range(len(genome)-L+1):
        text = genome[i:i+L]
        frequencyArray = computingFrequencies(text, k)
        for j in range(len(clump)):
            if frequencyArray[j] >= t:
                clump[j] = 1
    for i in range(len(clump)):
        if clump[i] == 1:
            pattern = numberToPattern(i,k)
            frequentPatterns.append(pattern)    
        
    return frequentPatterns
    