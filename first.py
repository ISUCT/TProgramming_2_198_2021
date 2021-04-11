a = False
b = True
c = a or b
print(a, b, c)
# Комментарий - ctrl + /
a = 5 # int
a = a + 1 
a += 1
b = 8.5 # float 
c = a + b
d = 5 % 2
print(f"d = {d}")

a = "Hello world"
print(a)
#    0  1  2  3      4      5    6
l = [1, 2, 3, 4 , "Hello", [1,2], "last"]
#   -7  -6 -5 -4    -3     -2    -1
print(l)
print(l[5])
print(l[0])
print(f"Длина списка l = {len(l)}")
print(f"Последний элемент {l[len(l) - 1 ]}")
print(f"Последний элемент {l[-1]}")
print(f"Элементы с 1 по 4 {l[1:4]}")
print(f"Элементы с 0 по 4 {l[:4]}")
print(f"Элементы с 4 до конца (включительно) {l[4:]}")

d = { "name": "Vasya",
      "age": 20  
}
print(d)
print(f"Имя: {d['name']}, возраст: {d['age']}")


