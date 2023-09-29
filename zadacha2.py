import pulp
import time
start = time.time()
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

problem_min = pulp.LpProblem('0_max', pulp.LpMinimize)
problem_min += -2 * x1 -4 * x2 -2 * x3, "Функция цели"
problem_min += -2 * x1 + x2 + x3 <= 4, "1"
problem_min += -x1 + x2 + 3 * x3 <=6, "2"
problem_min += x1 - 3 * x2 + x3 <=2, "3"
problem_min.solve()

print("Результат для минимизации:")
for variable in problem_min.variables():
    print(variable.name, "=", variable.varValue)

print("Оптимальное значение для переменных x:")
print(pulp.value(problem_min.objective))

stop = time.time()
print("Время :")
print(stop - start)