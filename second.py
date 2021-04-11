# Условия и циклы

a = 5
if a < 5:
    print("Less")
elif a == 5:
    print("Equals")
else:
    print("Greater")
print("Вне цикла")

i = 1 # j
while i <= 10:
    print(i)
    i += 1
print("Вне цикла")

# Вывод только четных
i = 1 # j
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
print("Вне цикла")

for i in range(0, 11, 2):
    print(i)

l = [1, 2, 3, 4 , "Hello", [1,2], "last"]
for item in l:
    print(item)

#Таблица умножения
n = 5
m = 3
# 1 x 1 = 1
# 1 x 2 = 2 ...

for i in range(1, n+1):
    for j in range(1, m+1):
        mul = i * j
        print(f"{i} x {j} = {mul}")
    print("-"*10)
