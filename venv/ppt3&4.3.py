n=1
result=0

while n<10:
    result += n
    n+=1
print("The sum of the first 9 numbers is", result)


#another while

while True:
    num=input("Give me a number(type quit to exit)")
    num2=input("Give me another number(type quit to exit")
    if num == "quit" or num2 == "quit":
        break
    num = int(num)
    num2 = int(num2)
    if num2 == 0:
        print("Can not divide by zero")
        continue
    print("The division result of", num, "and", num2, "is", num / num2)
    break
h
