class Worker:
    """This class represents employee name"""

    def __init__(self, workers_name=""):
        self.name = workers_name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

class Employment(Worker):
    """This class specializes Worker and is salaried"""

    def __init__(self, initial_salary, initial_name):
        self,__salart = initial_salary
        super().__init__(initial_name)

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def set_salary(self):
        return self.__salary
