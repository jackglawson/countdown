#Countdown solver

An algorithm to find a solution to the numbers round of 'countdown'.

A depth first search is used to visit all possible solutions.

## Improvements to be made:

### Remove redundancy in solutions.

e.g. 10+20=30 followed by 30+100=130 is redundant with 10+100=110 followed by 110+20=130.

This will significantly decrease the number of solutions.

### Use dynamic programming

Cache previous calculations to reduce the computation time.