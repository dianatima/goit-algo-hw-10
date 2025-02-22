import pulp

model = pulp.LpProblem("Production_maximization", pulp.LpMaximize)

x = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
y = pulp.LpVariable('Juice', lowBound=0, cat='Integer')

model += x + y, "Maximization"

model += 2 * x + 1 * y <= 100, "Water"
model += 1 * x <= 50, "Sugar"
model += 1 * x <= 30, "Lemonade"
model += 2 * y <= 40, "Fruit"

model.solve()

print(f"Number of Lemonade: {x.varValue}")
print(f"Number of Juice: {y.varValue}")
print(f"Total production: {pulp.value(model.objective)}")