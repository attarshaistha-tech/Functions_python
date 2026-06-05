#lambda functions
addi=lambda x,y,z:x+y-x-z
print(addi(5,3,2))

j=[100,200,300,400,500,1000]
j=int(input("enter the product: "))
for i in range(6):
    discount=i*0.1
    print(discount)

#map()
j=[100,200,300,400,500,1000]
print(list(map(lambda x:x*0.1,j)))

#filter()
emails=["algonex@gmail.com","invalid","user@domain.com","nelamalli@gmail.com","no_at_sign"]
valid_emails=list(filter(lambda email:"@" in email,emails))
print(valid_emails)

#reduce()
transactions=[100,200,300,400,500]
monthly_total=0
for i in transactions:
    monthly_total+=i
print(monthly_total)

transactions=[100,200,300,400,500]
from functools import reduce
total=reduce(lambda x,y:x+y,transactions)
print(total)

#list comprehension
squares=[x**2 for x in range(1,11)]
print(squares)
squares=[x**2 for x in range(1,11) if x!=5]
print(squares)
