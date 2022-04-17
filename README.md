# Student Data Generator

## Overview
This student data generator outputs data for random levels of students. For example, an A student may have scores ranging from 85 to 100, whereas a C student may have scores ranging from 65 to 78. The score randomness and class distribution is user-defined in input files.

## Input files

The bulk fo the input data is defined in `config.json`. The fields are described in the subsequent subsections.

### `inputFolder`

Which folder contains students' first names and last names?

### `outputFolder`

Which folder should generated data files be outputted in?

### `tables`

Names of output files:
* `students`: Student names and year they are from
* `assignments`: Assignment scores for each student
* `quizzes`: Quiz scores for each student
* `exams`: Exam scores for each student
* `weights`: Weight of each category

### `firstNames`

Which file contains students' first names? Assumption is that each name is on its own line.

### `lastNames`

Which file contains students' last names? Assumption is that each name is on its own line.

### `homeworks`

How many homework assignments does each student get?

### `quizzes`

How many quizzes does each student get?

### `exams`

How many exams does each student get?

### `corruptRate`

What is the probability that an assignment will _not_ get turned in?

### `percentageRanges`

These are the range of scores each grade of student gets. The grade orders are: F (lowest), D, C, B, A (highest). Ranges are defined as pairs of `[min, max]`, and they are allowed to overlap.

### `scoreRules`

These are the grade distributions defined as a list of probabilities. The list order starts from the lowest grade (F) to the highest grade (A). The total of the percentages _must_ sum to `100`.

### `weights`

These are the weights of each category (assignments, quizzes, exams) in precent. The sum fo the weights _must_ equal `100`.

### `yearRange`

Define the year range to that students can be assigned to. Ranges are inclusive. The `end` field _cannot_ be less than `start`. If `start` is the same as `end`, the data generated will be for one year.