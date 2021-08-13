import matplotlib.pyplot as plt

f = open("learning_curve.txt", "r")
content = f.read()

content = content.split(',')

generation_number = []
worst_case = []
best_case = []
mean_case = []

for value in content:
    string = value.split(':')
    if len(string) < 4:
        continue
    generation_number.append(int(string[0]))
    worst_case.append(int(string[1]))
    best_case.append(int(string[2]))
    mean_case.append(int(string[3]))

plt.plot(generation_number, worst_case)
plt.plot(generation_number, best_case)
plt.plot(generation_number, mean_case)
plt.show()


