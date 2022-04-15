# Student Data Generator

## Overview
This student data generator outputs data for random levels of students. For example, an A student may have scores ranging from 85 to 100, whereas a C student may have scores ranging from 65 to 78. The score randomness and class distribution is user-defined in input files.

## Input files

The bulk fo the input data is defined in `config.json`. The fields are described in the subsequent subsections.

### `inputFolder`

Which folder contains students' first names and last names?

### `firstNames`

Which file contains students' first names? Assumption is that each name is on its own line.

### `lastNames`

Which file contains students' last names? Assumption is that each name is on its own line.

### `homeworks`

How many homework assignments does each student get?

### `corruptRate`

What is the probability that an assignment will _not_ get turned in?

### `percentageRanges`

These are the range of scores each grade of student gets. The grade orders are: F (lowest), D, C, B, A (highest). Ranges are defined as pairs of `[min, max]`, and they are allowed to overlap.

### `scoreRules`

These are the grade distributions defined as a list of probabilities. The list order starts from the lowest grade (F) to the highest grade (A). The total of the percentages _must_ sum to `100`.

### `yearRange`

Define the year range to bucket students in. Ranges are inclusive. The `end` field _cannot_ be less than `start`. If `start` is the same as `end`, the data generated will be for one year.