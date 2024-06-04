

def fizzBuzz(num):
    for i in range(1,num+1):

        out = ""
        if(i%3 == 0):
            out+= "Fizz"

        if(i%5 == 0):
            out+= "Buzz"

        if(i%3 != 0 and i%5 != 0):
            out += str(i)

        print(out)

num = 100

fizzBuzz(num)