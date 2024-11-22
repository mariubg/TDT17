grade = [3, 4, 5, 4, 3, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4, 5, 5, 5]
weight = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]

grade_sum = 0
for i in range(len(grade)):
    grade_sum += grade[i] * weight[i]

mean = grade_sum/sum(weight)
print(mean)