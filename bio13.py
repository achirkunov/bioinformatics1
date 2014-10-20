
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