# Exercise - 1.1

> **_1. Give a real-world example in which one of the following computational problems appears: sorting, determining the best order for multiplying matrices, or finding the convex hull\._**

| Sorting              | Matrix Chain Multiplication | Convex Hull |
| -------------------- | --------------------------- | ----------- |
| _Contest Scoreboard_ | _In animations to perform rotations of different objects at different positions_ | _TODO_      |

---

> **_2. Other than speed, what other measures of efficiency might one use in a real-world setting?_**

_Resources (i.e. memory), power consumption, mobile data usage, etc. _

---

> **_3. Select a data structure that you have seen previously, and discuss its strengths and limitations\._**

[Array](https://www.geeksforgeeks.org/array/)
_Pros :-_

- independent or random access - _O(1)_

_Cons :-_

- fixed size
- insertion is costly - _O(n)_
- deletion is costly - _O(n)_

---

> **_4. How are the shortest-path and traveling-salesman problems given above similar? How are they different?._**

_Similarities :-_

- They are both problems on graph.
- They are both optimization problem.

_Differences :-_

- Shortest-path problem is used for one way journey, while trveling-salesman problem is for a closed path travel returning to the start.
- Shortest-path is a easier problem and can be solved in polynomial time, while traveling-salesman problem is very difficult problem and it is NP Complete and no efficient solutions have been found till date.

_TODO_

---

> **_5. Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is “approximately” the best is good enough\._**

_Best Solution Required_
- In adverserial gameplay where you play against opponent and it is known that the opponent plays optimally. In this case you will have to take the best possible solution.
Example- Tic-Tac-Toe

_Approximate Solution is Good_
- In problems like routing for parcel deliveries, approximate solutions work, suppose that the cost for going through best path is $1000 with optimal driving, which might varry in range $1000- $1200 due to traffic conditions. And you find a path which costs $1050 with optimal driving, it is good enough and will work fine.

---
