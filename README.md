# Countdown solver

An algorithm to find a solution to the numbers round of 'countdown'.

A depth first search is used to visit all possible solutions.


### Example output:

```
>> countdown((75, 100, 50, 25, 10, 2), 316)

19 solutions found. One possible solution is:
75 / 25 = 3
100 + 2 = 102
102 * 3 = 306
10 + 306 = 316
```


### Improvements to be made:

1. Remove redundancy in solutions.
- e.g. 10+20=30 followed by 30+100=130 is redundant with 10+100=110 followed by 110+20=130.
- This will significantly decrease the number of solutions.

2. Use dynamic programming
- Cache previous calculations to reduce the computation time.
