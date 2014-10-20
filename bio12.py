def patternCount(text,pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count
    
def testPatternCount():
    f = open("data/dataset_2_6.txt")
    lines = f.readlines()
    text = lines[0].rstrip()
    pattern = lines[1].rstrip()
    print(patternCount(text,pattern))
    
def frequentWords(text,k):
    frequentPatterns = []
    count = [0]*(len(text)-k+1)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        count[i] = patternCount(text, pattern)
    maxCount = max(count)
    for i in range(len(text)-k+1):
        if count[i] == maxCount:
            frequentPatterns.append(text[i:i+k])            
    return set(frequentPatterns)

def testFrequentWords():
    f = open("data/dataset_2_9.txt")
    lines = f.readlines()
    text = lines[0].rstrip()
    k = int(lines[1].rstrip())
    output = frequentWords(text,k)
    print(" ".join(map(str, output)))