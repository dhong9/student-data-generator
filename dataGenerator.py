import random, csv, json

# Utility functions:
readConfig = lambda src: json.load(open(src))
readNames = lambda src: open(src, "r").read().split("\n")

# Read config file
print("Loading configuration...")
configData = readConfig("config.json")
inputFolder = configData["inputFolder"]

print("Generating data...")

# Read first and last names from input files
firstNames = readNames(inputFolder + "/firstNames.txt")
lastNames = readNames(inputFolder + "/lastNames.txt")

# Make all combinations of first and last names
names = sorted([fName + ' ' + lName for fName in firstNames for lName in lastNames])

# Capture number of students
numberOfStudents = len(names)

print("Found " + str(numberOfStudents) + " students")

# Generate random IDs for each name
ids = sorted(random.sample(range(100000, 1000000), numberOfStudents))

# Define rule for random score generating
scoreRules = configData["scoreRules"]
randScoreFuncs = [lambda: random.uniform(p[0], p[1]) for p in configData["percentageRanges"]]

# Generate random scores
numberOfEntries = configData["homeworks"] # Number of entries per student
corruptRate = configData["corruptRate"] # Data corruption probability
scores = []
for name in names:
    randRule = random.uniform(0, 100)
    x = 0
    randIndex = 0
    for rule in scoreRules:
        if x <= randRule <= x + rule:
            scores.append([-1 if random.uniform(0, 100) < corruptRate else round(randScoreFuncs[randIndex]()) for i in range(numberOfEntries)])
            break
        x += rule
        randIndex += 1

header = ["ID", "Name"] + ["Assignment #" + str(i + 1) for i in range(numberOfEntries)]

# Output data to a CSV file
with open('sampleData.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    
    # Write header
    writer.writerow(header)

    # Write rows
    writer.writerows([[ids[i], names[i]] + scores[i] for i in range(numberOfStudents)])