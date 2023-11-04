#FizzBuzz Code

#Number divisible by 3 gets Fizz
#Number divisible by 5 gets Buzz
#Divisble by both gets FizzBuzz

num1 = 3
num2 = 5
count = 100
for i in range(count):
    output = ""
    if i % num1 == 0: 
        output += "Fizz"
    if i % num2 == 0: 
        output += "Buzz"
    if output == "":
        output = i
    print(output)

    