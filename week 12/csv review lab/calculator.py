from random import randint

class Pycalc:

    def __init__(self, num_list):
        self.num_list = num_list


    def get_average(self):

        return sum(self.num_list) / len(self.num_list)


    def get_max(self):

        max_val = self.num_list[0]

        for item in self.num_list:

            if item > max_val:

                max_val = item

        return max_val


    def get_min(self):

        min_val = self.num_list[0]

        for item in self.num_list:

            if item < min_val:

                min_val = item

        return min_val

    def Clear_list (self):

        self.num_list.clear()

        print(self.num_list)

    def random_num(self, x_elements, from_y, to_z):

        for element in range(x_elements):

            self.num_list.append(randint(from_y, to_z))

        return self.num_list




# testing with number inputs and print statements
num_list = [2, 3, 4, 5]

print("Here is my list of numbers: {} ".format(num_list))

c = Pycalc(num_list)

print("The average value is:", c.get_average())
print("Min value is:", c.get_min())
print("Max value is:", c.get_max())
print("Clear the list:", c.Clear_list())
print("The new list is:", c.random_num(4,0,20))