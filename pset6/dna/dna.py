import csv
from sys import argv

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")

if ".csv" not in argv[1]:
    print("Usage: python dna.py data.csv sequence.txt")
elif ".txt" not in argv[2]:
    print("Usage: python dna.py data.csv sequence.txt")

with open(argv[2]) as DNAfile:
    DNAreader = csv.reader(DNAfile)
    for row in DNAreader:
        DNAlist = row
#store in string
DNA = DNAlist[0]

#create a dictionary
sequences = {}

with open(argv[1]) as peoplefile:
    people = csv.reader(peoplefile)
    for row in people:
        DNASequences = row
        DNASequences.pop(0)
        break

for item in DNASequences:
    sequences[item] = 1

# if repetitions of the values from sequence dictionary are found, count
for key in sequences:
    l = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(DNA)):
        # after having counted a sequence
        # skip at the end of it to avoid counting again
        while temp > 0:
            temp -= 1
            continue
# if the segment of dna corresponds to the key &&
        #there is a repetition of it
        #increment counter
        if DNA[i: i + l] == key:
            while DNA[i - l: i] == DNA[i: i + l]:
                temp += 1
                i += l
# compare the value to the previous longest sequence &&
            # if it is longer it becomes the new max
            if temp > tempMax:
                tempMax = temp
# store the longest sequences in the dictionary using the correspondent key
    sequences[key] += tempMax

with open(argv[1], newline='') as peoplefile:
    people = csv.DictReader(peoplefile)
    for person in people:
        match = 0
        # compares the sequences to every person and prints name
        # leave the program if there is a match
        for DNA in sequences:
            if sequences[DNA] == int(person[DNA]):
                match += 1
        if match == len(sequences):
            print(person['name'])
            exit()
    #otherwise, no match
    print("No match")
