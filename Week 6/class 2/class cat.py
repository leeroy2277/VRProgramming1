class Cat:
    name = ""
    age = 0
    registered = False

    def __init__(self, input_name, input_age):
        self.name = input_name
        self.age = input_age

        if input_age > 2:
            self.registered = True

    def meow(self, number_times):
        for m in range(number_times):
            print("meow")

    def meow(self, number_times, phrase=""):
        for m in range(number_times):
            print("meow" + phrase)

c1 = Cat("jack", 2)
c2 = Cat("samantha", 9)

print("Cat c1 registration state is " + str(c1.registered))
print("Cat c2 registration state is " + str(c2.registered))

c1.meow(5)