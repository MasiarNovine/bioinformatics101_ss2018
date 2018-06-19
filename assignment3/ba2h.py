#defining Hamming Distance = mi
def setHamming(Pattern, secPattern):
    HammingDistance = 0
    for i in range(len(Pattern)):
        if Pattern[i] != secPattern[i]:
            HammingDistance += 1
    return HammingDistance
#Distance between Pattern and String
def DistanceBetweenPatternAndStrings(Pattern, Dna):
    """Find the distance between a k-mer 'Pattern' and a set of strings 'Dna'"""
    k = len(Pattern)
    distance = 0
    split_Dna = Dna.split(', ')
    #iteration of string 'Text' over 'Dna'
    for Text in split_Dna:
        HammingDistance = float('inf') #defining infinity
        #iteration over every index of 'Text'
        for i in range((len(Text) - k) + 1):
            hit = setHamming(Pattern, Text[i:(i + k)])
            if HammingDistance > hit:
                HammingDistance = hit
            distance = distance + HammingDistance
    return distance
print(DistanceBetweenPatternAndStrings('AAA', 'TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'))
