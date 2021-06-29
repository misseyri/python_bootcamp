

  # This is a sample Python script.
  # Mapsa boot camp
  #exercise




   #  Number 1


def volume(r):
    p = 3.14
    a = (4 / 3) * p * (r ** 3)
    print("volume of the sphere is : ", a)
volume(3)

  # Number 2


def compare():
    myList=[]
    for i in range(3):
        a=int(input())
        myList.append(a)
    myList.sort()
    print("max is: ",myList[2],"\nmin is: ",myList[0])
compare()


   # Number 3
def login():
    correct_pass=1234
    a=int(input("Enter your password : "))
    print("you have successful login :) ")if a ==correct_pass \
        else print("you haven't successful login :( ")
login()

   #Number 4


def cast(a):
    return int(a)
    print(cast(3.2))

    # Number 5


def divisible(A,B):
    print("A bar  B bakhsh pazir hast ")if not A % B \
        else print("A bar  B bakhsh pazir nist")
divisible(6,3)

    # Number 6


def cast_temp(temp):
    F_temp = (9/5) * temp +32
    return F_temp
print(cast_temp(12))

    # Number 7


import math
def calc():
    p=math.pi
    n=int(input("Enter a number : "))
    a=pow((pow(n,4) * p ), 5)
    print(a)
calc()
