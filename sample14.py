i = 0
n = input("enter the number: ")
numbers = []
while i < int(n):
    print (f"enter number {i}: ", end = ' ')
    i = i+1
    input()
    numbers.append(i)
small = numbers[0]
for number in numbers :
     if small > number:
            small = number
print (f"the smallest number is {small}")
