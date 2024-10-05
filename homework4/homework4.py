while True:
  try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    break  
  except ValueError:
    print("Ошибка! Введите числа.")
if a > b:
  a, b = b, a
print("Числа между", a, "и", b, ":")
for i in range(int(a) + 1, int(b)):
  print(i, end=" ")

    