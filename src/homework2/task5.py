# 5 Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы. n - вводится

n_number = int(input())
first_num = 0
second_num = 1
for number in range(1, n_number - 1):
    first_num, second_num = second_num, first_num + second_num
print(second_num)
