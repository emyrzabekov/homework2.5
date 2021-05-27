income = [300, 40, 44440, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]
spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]

for i in range(12):
    try:
        if income == 0:
            koef = 0
        else:
            koef = spendings[i] / income[i]
        koef += koef
        res = koef/12
    except ZeroDivisionError:
        koef = 0
        continue

print(koef)
print(res)
