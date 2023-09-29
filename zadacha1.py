import pulp
import time
start = time.time()
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

problem_max = pulp.LpProblem('0_max', pulp.LpMaximize)
problem_max += 33 - 3 * x1 + 2 * x2 - 3 * x4 - x5, "Функция цели"
problem_max += 3 * x1 - 2 * x2 - x3 + x4 = 30, "1"
problem_max += 4 * x1 - x2 + x4 + x5 = 21, "2"
problem_max += 4 * x1 - x2 - x4 + x5 = 13, "3"
problem_max += x1 + x2 - x6 = 3, "4"
problem_max.solve()

print("Результат для максимизации:")
for variable in problem_max.variables():
    print(variable.name, "=", variable.varValue)

print("Max:")
print(pulp.value(problem_max.objective))

stop = time.time()
print("Время :")
print(stop - start)