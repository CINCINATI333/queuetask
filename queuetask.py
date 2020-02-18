num = int(input('Пожалуйста, ведите сумму цифр:   '))
a = [str(0)*i for i in range(999)]

for i in range(1,len(a)):
    a[i] = str(i)
sum = 0

for i in range(len(a)):
    for k in range(len(a[i])):
        sum += int(a[i][k])
        if sum == num:
            print(a[i])
            break

