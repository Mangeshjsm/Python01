"""

1) looping statement
2)conditional statement

Assignment
1)

1) create Matrix
2)Matrix multiplication
3)spiral matrix rotation
4)shift elements in Matrix


Looping
1)while
2)for
3)comprehension 



for i in range(0,5):
    for j in range(0,5):
        print(i,j)

for i in range(0,5):
for j in range(0,5)
    

    i=0
    while True:
        if i<=5:
            print("*")
            break
            i +=1


no = 1
while no <= 5:
    print("*")
    no += 1


for i in range(0, 5):
    for j in range(0, 5):
        print("*", end=' ')
    print("\n")



for i in range(0, 5):
    for j in range(0, 5):
        print("*", end=' ')
    print("\r")



for i in range(5):
    for j in range(5):
        if (j==0):
            print("*",end=" ")
        else:
            print("*",end=" ")
     print("\n")


for i in range(0, 5):
    for j in range(0, 5):
        print("1", end=' ')
    print("\r")


#For Assignment no 3
for i in range(0, 5):
    num=i%2
    for j in range(0, 5):
        print(num, end=" ")
    print("\r")


for i in range(0, 5):
    for j in range(0, 5):
        if(i%2==0):
            print("0", end=" ")
        else:
            print("1", end=" ")
    print("")


#For Assignment no 5

for i in range(0, 5):
    for j in range(0, i+1):
        if(j%2==0):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("")



#For Assignment no 4

for i in range(0, 5):
    for j in range(0, i+1):
        i -=1
        if(i%2==0):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("")

#For Assignment no 4
num=0
for i in range(0, 5):
    for j in range(0, i+1):
        print(num%2, end=" ")
        num +=1
    if i%2 == 1:
        num +=1
    print("")


for i in range(1, 6):
    for j in range(0, i+1):
        if(i%2==0):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("")



#For Assignment no 6

for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print("")



#For Assignment no 7

num=1
for i in range(0, 5):
    for j in range(0, 5):
        print('{num:02d}'.format(num=num), end=" ")
        num +=1
    print("")


#OR
num=1
for i in range(0, 5):
    for j in range(0, 5):
        print('{:02d}'.format(num), end=" ")
        num +=1
    print("")



#For Assignment no 8

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j%2, end=" ")
    print("")


for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j%2, end=" ")
    print("")


# for assignment no 12

sum=2
for i in range(0, 6):
    for j in range(0, i+1):
        if(j==0):
            print("1", end=" ")
        else:
            print("0", end=" ")
    print("")

"""

# ctrl+shift+f to format the python script

power_of = 1
for i in range(0, 6):
    power_of = power_of * 2
    for j in range(0, i + 1):
        print(power_of, end=" ")
    print("")
