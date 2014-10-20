def complement(input):
    baseComplement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    letters = list(input)
    letters = [baseComplement[base] for base in letters]
    return ''.join(letters)

def reverseComplement(input):
    return input[::-1]