# SVM Example
An example of using Gurobi to compute a support vector machine

![](svm.png?raw=true)

# Running the example

1. Start Python's webserver from the command line
    ```
    make
    ```

2. Point your browser at http://localhost:8000

3. Add points of different types (red and green).

4. Click "Compute Classificiation" to solve the SVM optimization problem.

# Performing an optimization

To just solve the model (without running a web server) do:

```
make test
```

## Sources

The idea for this example was based on the [libSVM][1] page and
the model definied in pg. 423 of [Convex Optimization
Stephen Boyd and Lieven Vandenberghe][2]

[1]: https://www.csie.ntu.edu.tw/~cjlin/libsvm/index.html?js=1#svm-toy-js
[2]: http://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf