
def countNumbers(teksts):
  summa = 0
  for simbols in teksts:
    summa = summa + int(simbols)
  return summa
v = input("Ievadit skaitļi")
rez = countNumbers(v)
print(rez)