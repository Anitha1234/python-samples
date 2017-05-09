i = 0
n = input("enter number: ")
numbers = []
while i < int(n):
    print (f"enter number {i} : ",end = ' ')
    i = i+1
    b=input()
    b=int(b)
    numbers.append(b)
for number in numbers:
    if number % 3 :
        print(f"the odd number {number}")
