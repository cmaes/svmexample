#!/usr/bin/python

# Test GitHub

from gurobipy import *

x = [ [0,1], [1, 2], [3, 4]]
y = [ [1,1], [2,2], [4,4]]
gamma = 0.1

def optimize(x, y, gamma):
    m = Model()

    a = [ m.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name="a0"),
          m.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name="a1") ]
    beta = m.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, name="beta")

    u = []
    N = len(x)
    for i in xrange(N):
        u.append(m.addVar(name=("u%d" % i)))

    v = []
    M = len(y)
    for i in xrange(M):
        v.append(m.addVar(name=("v%d" % i)))

    m.update()

    m.setObjective(a[0]*a[0] + a[1]*a[1] + gamma*(quicksum(u) + quicksum(v)))

    for i in xrange(N):
        xi = x[i]
        m.addConstr(a[0]*xi[0] + a[1]*xi[1] - beta >= 1 - u[i], name=("x%d" % i))

    for i in xrange(M):
        yi = y[i]
        m.addConstr(a[0]*yi[0] + a[1]*yi[1] - beta <= -(1 - v[i]), name=("y%d" % i))

    m.update()
    m.write('test.lp')
    m.optimize()

    results = {}
    if m.Status == GRB.OPTIMAL:
        results['a'] = [a[0].X, a[1].X]
        results['beta'] = beta.X

    return results

if __name__ == '__main__':
    results = optimize(x, y, gamma)
    print results
