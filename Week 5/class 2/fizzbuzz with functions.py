
def FizzBuzz ():

    def num_case(num, Test_num):
        if num % Test_num == 0:
            return True

    for num in range(0, 21):
        print(str(num)+":",end="")




        if (num_case(num, 3) and num_case(num, 5)):
            print(" FizzBuzz")
        elif num_case (num, 3):
            print(" Fizz")
        elif num_case (num, 5):
            print(" Buzz")

        else:
            print()

FizzBuzz()








