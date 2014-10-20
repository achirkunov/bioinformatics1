
def complement(sequence):
    baseComplement = {'A':'T','C':'G','G':'C','T':'A'}
    output = [baseComplement[base] for base in list(sequence)]
    return "".join(output)
    
def reverseComplement(sequence):
    return complement(sequence)[::-1]
    
def testReverseComplement():
    f = open("data/dataset_3_2.txt")
    lines = f.readlines()
    sequence = lines[0].rstrip()
    print(reverseComplement(sequence))
    
def occurences(pattern,genome):
    o = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            o.append(i)
    return o

def testOccurences():
    f = open("data/dataset_3_5.txt")
    lines = f.readlines()
    pattern = lines[0].rstrip()
    genome = lines[1].rstrip()
    output = occurences(pattern,genome)
    print(" ".join(map(str, output)))