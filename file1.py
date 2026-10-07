print("hello world")

def sum(num1,num2):
    return num1+num2

def multiply(num1,num2):
   return num1*num2

def total_(num):
    liste = []
    for sayı in range(1,num+1):
        if num%sayı == 0:
            liste.append(sayı)
    return liste
print(total_(12))
