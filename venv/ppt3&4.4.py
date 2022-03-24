hi = "Hello"
bye = "Bye"
print(hi+bye)
print(hi + " " + bye)

name = input("What is your name?")
print("Nice to meet you", name)

age = input("How old are you? ")
print("in 2032 you will be ", int(age) + 10)
###
text = "a nut for a jar of tuna"
text = text.replace(" ", "")
print(text)
reversed = text[::-1]
if text == reversed:
    print("this is a palindrome")
else:
    print("this is not a palindrome")
###
a = 5
b = 5
if a > b:
    print("the first number is bigger")
elif a < b:
    print("the first number is smaller")
else:
    print("they are equal")
##
greeting = "hello, how are you?"
for letter in greeting:
    print(letter*2, end="")
print()
print(2*greeting)

print(greeting[::-1])
##
try:
    age = input("How old are you? ")
    print("in 2032 you will be ", int(age) + 10)
    print(100/int(age))
except ValueError:
    print("Hey, that is not a number")
except ZeroDivisionError:
    print("can not divide by zero")
except:
    print("this is a new error that I did not see")
finally:
    print("this is what we do after all is done")