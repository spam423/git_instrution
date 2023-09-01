numbers = [2, 5, 3, 4, 1]
size = 5
index = 0
sum = 0
mean = 0
while size > index:
    sum = sum + numbers[index]
    index = index + 1
mean = sum / size
print(mean)