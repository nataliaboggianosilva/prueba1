print(5+2-9)
print(2+3*5)
print(--5)
print(not None)
print(4/2)
print(3.0*1.0)
print(2**3+1)
print(2**(3+1.0))
print(2<3<1)
print(3>(0**0 *4))
prompt='What is the speed of the car?'
speed= input(prompt)
print(int(speed) + 5)
try:
    num=input("Give me a number")
    num=int(num)
    print("The square of the number read is:", num*num)
except:
    print("Please give me a proper number")

try:
    num=input("Give me a number")
    num=int(num)
    num2=input("Give me another number")
    num2=int(num2)
    result=num/num2
    print("The division result is", result)

except ValueError:
    print("Please give me a proper number")
except ZeroDivisionError:
    print("The second number can not be zero")

try:
    num=input("Give me a number")
    num=int(num)
    num2=input("Give me another number")
    num2=int(num2)
    result=num/num2

except ValueError:
    print("Please give me a proper number")
except ZeroDivisionError:
    print("The second number cannot be zero")
except:
    print("Some of the exceptions I did not see coming")
else:
    print("The division result is", result)


if number % 2 ==0:
    print(number,"is an even number")
else:
    print("Nothing would be printed if it were odd")

