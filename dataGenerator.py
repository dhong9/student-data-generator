import random, csv, json

# Utility functions:

# Reads JSON file into an object
readConfig = lambda src: json.load(open(src))

# Reads text file line by line and store them in a list
readNames = lambda src: open(src, "r").read().split("\n")

# Generates random data
def genData(n, corruptRate):
    scores = []
    for name in names:
        randRule = random.uniform(0, 100)
        x = 0
        randIndex = 0
        for rule in scoreRules:
            if x <= randRule <= x + rule:
                scores.append([-1 if random.uniform(0, 100) < corruptRate else round(randScoreFuncs[randIndex]()) for i in range(n)])
                break
            x += rule
            randIndex += 1
    return scores

# Outputs data to a CSV file
def outputData(fileName, header, rows):
    with open(fileName, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(header)

        # Write rows
        writer.writerows(rows)

# Read config file
print("Loading configuration...")
configData = readConfig("config.json")
inputFolder = configData["inputFolder"]
outputFolder = configData["outputFolder"]
tables = configData["tables"]
outputStudents = outputFolder + "/" + tables["students"]
outputAssignments = outputFolder + "/" + tables["assignments"]
outputQuizzes = outputFolder + "/" + tables["quizzes"]
outputExams = outputFolder + "/" + tables["exams"]
outputWeights = outputFolder + "/" + tables["weights"]
numberOfHomeworks = configData["homeworks"]
numberOfQuizzes = configData["quizzes"]
numberOfExams = configData["exams"]
corruptRate = configData["corruptRate"]
weights = configData["weights"]
assignmentWeight = weights["assignments"]
quizWeight = weights["quizzes"]
examWeight = weights["exams"]

print("Generating data...")

# Read first and last names from input files
firstNames = readNames(inputFolder + "/firstNames.txt")
lastNames = readNames(inputFolder + "/lastNames.txt")

# Make all combinations of first and last names
names = [fName + ' ' + lName for fName in firstNames for lName in lastNames]

# Capture number of students
numberOfStudents = len(names)

print("Found " + str(numberOfStudents) + " students")

# Get year range
yearRange = configData["yearRange"]
yearMin = yearRange["start"]
yearMax = yearRange["end"]
print("Students will be assigned into years from " + str(yearMin) + " to " + str(yearMax) + ".")

# Generate random IDs for each name
ids = sorted(random.sample(range(100000, 1000000), numberOfStudents))

# Define rule for random score generating
scoreRules = configData["scoreRules"]
randScoreFuncs = [lambda p=p: random.uniform(p[0], p[1]) for p in configData["percentageRanges"]]

# Generate random scores
homeworkScores = genData(numberOfHomeworks, corruptRate)
quizScores = genData(numberOfQuizzes, corruptRate)
examScores = genData(numberOfExams, corruptRate)

# Write tables to CSV files
print("Writing generated data to files...")

# Student names with years
outputData(outputStudents, ["Student ID", "Name", "Year"], [[ids[i], names[i], random.randint(yearMin, yearMax)] for i in range(numberOfStudents)])

# Assignments
outputData(outputAssignments, ["Student ID"] + ["Assignment " + str(i + 1) for i in range(numberOfHomeworks)], [[ids[i]] + homeworkScores[i] for i in range(numberOfStudents)])

# Quizzes
outputData(outputQuizzes, ["Student ID"] + ["Quiz " + str(i + 1) for i in range(numberOfQuizzes)], [[ids[i]] + quizScores[i] for i in range(numberOfStudents)])

# Exams
outputData(outputExams, ["Student ID"] + ["Exam " + str(i + 1) for i in range(numberOfExams)], [[ids[i]] + examScores[i] for i in range(numberOfExams)])

# Weights
outputData(outputWeights, ["Category", "Weight"], [["Assignments", assignmentWeight], ["Quizzes", quizWeight], ["Exams", examWeight]])

print("Data has been writen to folder: " + outputFolder)