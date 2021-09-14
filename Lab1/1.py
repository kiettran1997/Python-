# bài 3  
def sumDigit(num):
    sum = 0
    while(num):
        sum += num % 10
        num = int(num / 10)
    return sum

print('Ket qua nho nhat la:', min(100, 321, 267, 59, 40, key=sumDigit))

num = [15, 300, 2700, 821, 52, 10, 6]
print('Ket qua nho nhat la:', min(num, key=sumDigit))