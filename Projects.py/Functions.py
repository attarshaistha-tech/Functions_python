#FUNCTIONS IN PYTHON
#A function is a block of code that performs a specific task.Functions help to organize code, make it reusable.
#defining a function
def attar():
    print("hello world")
#calling a function
attar()

#with parameters
def add(a,b):
    return a+b
result=add(5,3)

def algonex(name,age,location):
    print(f"my name is {name},i am {age} years old and i live in {location}")
    return f"my name is {name},i am {age} years old and i live in {location}"
algonex("attar",25,"nairobi")

#ARGUMENTS
#1.POSITIONAL ARGUMENTS
def greet(name,age):
    print(f"hello {name},you are {age} years old")
greet("attar",25)

#2.KEYWORD ARGUMENTS
def greet(name,age):
    print(f"hello {name},you are {age} years old")
greet(age=25,name="attar")

#3.DEFAULT ARGUMENTS
def greet(name,age=30):
    print(f"hello {name},you are {age} years old")
greet("attar")

#functions with loops and conditions
def college_names(clgs):
    for i in clgs:
        if i=="nbkr":
            break
            print(i)
colleges=list(input("enter college names separated by commas: ").split(","))
#college_names(colleges)