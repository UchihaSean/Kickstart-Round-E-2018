# Kickstart Round E 2018
_Problem discription_ *https://code.google.com/codejam/contest/4394486/dashboard*

## Problem A
- Greedy
- Sort and judge if the kth yogurt could be eated on time
- **O(NlogN)**

## Problem B
_for small case_
--
- enumerate each choice and choose the best one
- **O(2^N)

_for large case_
--
- for Tk, always keep the top 101
- use 0 or 1 for k+1, and generate 202 posibility, and choose top 101
- until the final position
- **O(PM)**

## Problem C
_for small case_
--
- enumerate each A choices and B choices
- select the best win probability for A
- **O(1680^2)**