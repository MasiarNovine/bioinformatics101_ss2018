# We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers.
# For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT",
# and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".
# Frequent Words Problem:
# Find the most frequent k-mers in a string.
# Given: A DNA string Text and an integer k.
# Return: All most frequent k-mers in Text (in any order).

# Definere Funktion
def pat_count(text, pattern):
    count = 0
# loop zur Ausgabe von text
    for i in range(0, len(text) - len(pattern) + 1):
         if text[i:i + len(pattern)] == pattern:
             count += 1
    return count

# Ermitteln der längsten k-mers
def freq_words(text, k):
    most_occur = []
    count = []

# loop zum Finden aller k-mers mit max count
    for i in range(0, len(text) - k + 1):
            curr_pattern = text[i:i + k]
            curr_count = pat_count(text, curr_pattern)

# Bedingungen
            if len(count) == 0:
                most_occur.append(curr_pattern)
                count.append(curr_count)
            elif curr_count == max(count):
                most_occur.append(curr_pattern)
                count.append(curr_count)
            elif curr_count > max(count):
                most_occur = []
                count = []
                most_occur.append(curr_pattern)
                count.append(curr_count)

# Ausgabe der k-mers als Liste
    return list(set(most_occur))

DNA_seq = input("Eingabe der Sequenz: ")
k = int(input("Eingabe von k: "))

# Ausgabe
print(freq_words(DNA_seq, k))
