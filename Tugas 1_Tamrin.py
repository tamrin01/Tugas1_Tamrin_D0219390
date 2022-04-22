def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
print("Pilih Operasi.")
print("a.penjumlahan")
print("b.pengurang")
print("c.perkalian")
print("d.pembagian")

choice = input("Masukkan pilihan Anda: ")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))
if choice == 'a':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == 'b':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == 'c':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == 'd':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Input yang dimasukkan error!")
