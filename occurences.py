def occurences(pattern,genome):
    output = []
    for i in range(len(genome)):
        if genome[i:i+len(pattern)] == pattern:
            output.append(i)
    return " ".join(map(str,output))