import random
fruits = ["apple","orenge","mango","pineapple","graps","banana","sappota"]
selected = random.choice(fruits)
#print (selected)
print (len(selected))
array = list(selected)
#print (array)

i=0
a = input ("enter the letter: ")
while i < len(selected):
    print("_", end = ' ')
    i = i+1
    #print ("enter the letter: " ,end = ' ')
