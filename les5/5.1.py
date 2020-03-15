# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа
# должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict
from statistics import mean
QUARTER = 4
factories = defaultdict(float)
total = int(input("total factories: "))
for i in range(total):
    factory_name = input(f"Factory {i+1} name: ")
    for j in range(QUARTER):
        factories[factory_name] += int(input(f"{j+1} quarter profit: "))
aver = mean(factories.values())
print(f"Average profit - {aver:.2f}")
more = []
less = []
for i in factories:
    if factories[i] > aver:
        more.append(i)
    elif factories[i] < aver:
        less.append(i)
print(f"factories with profit more than average - {', '.join(more)}")
print(f"factories with profit less than average - {', '.join(less)}")
