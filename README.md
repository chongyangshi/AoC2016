My solutions to Advent of Code 2 (2016), this time as icydoge. Answers written for Python 3.

# Using a solution
Clone this repo, replace the corresponding input file under `inputs` with your input, and run the corresponding solution script (e.g. `python3 day11.py`) to get the answer, which is always outputed in the same form.

# Slow ones
There are a few solutions that are not nearly instant. Below is a current known list of them and explanations:
* `day5.py` : requires a lot of MD5 operations, give it a few minutes.
* `day11.py`: a complex breadth-first search problem which requires extensive branch pruning, and my pruning is not fully done, therefore Part 2 can take up to an hour to run on a mid-range computer.
* `day12.py`: Part 2 has the assembly interpreter going through a far greater magnitude of loops, takes a minute to run.
* `day14.py`: again requires a lot of MD5 operations, especially Part 2. All together it takes a few minutes to run.
