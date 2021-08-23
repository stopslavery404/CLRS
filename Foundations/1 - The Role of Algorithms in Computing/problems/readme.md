# Problems - 1

> **_1. Comparison of running times, For each function f(n) and time t in the following table, determine the largest size n of a problem that can be solved in time t, assuming that the algorithm to solve the problem takes f(n) microseconds._**

- Let's  take f(n) = <img src="https://render.githubusercontent.com/render/math?math=lgn">  and  t = **1 sec** and try to find the largest size n.
- I assume base 2 here.
- thus, time to solve the problem must be less than or equal to given time which is ***t (1 sec)***.
- *lgn* <= 10^6
- *n* <= <img src="https://render.githubusercontent.com/render/math?math=2^{{10}^6}">

***Similarly, we will fill the whole table. Below is the final table***


||1-second|1-minute|1-hour|1-day|1-month|1-year|1-century|
|---|---|---|---|---|---|---|---|
|<img src="https://render.githubusercontent.com/render/math?math=lgn">|<img src="https://render.githubusercontent.com/render/math?math=2^{{10}^6}">|---|---|---|---|---|---|
|<img src="https://render.githubusercontent.com/render/math?math=\sqrt{n}">|---|---|---|---|---|---|---|
|<img src="https://render.githubusercontent.com/render/math?math=n">|---|---|---|---|---|---|---|
|<img src="https://render.githubusercontent.com/render/math?math=nlgn">|---|---|---|---|---|---|---|
|<img src="https://render.githubusercontent.com/render/math?math=n^2">|---|---|---|---|---|---|---|
|<img src="https://render.githubusercontent.com/render/math?math=n^3">|---|---|---|---|---|---|---|
|<img src="https://render.githubusercontent.com/render/math?math=2^n">|---|---|---|---|---|---|---|
|<img src="https://render.githubusercontent.com/render/math?math=n!">|---|---|---|---|---|---|---|
