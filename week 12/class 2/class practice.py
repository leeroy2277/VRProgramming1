import datetime

class Worker:

    def __init__(self, id_num: int, hire_date: datetime, first_name: str, last_name: str ):
        self.__id_num = id_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__hire_date = hire_date

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_id_num(self,):
        return self.__id_num

    def get_first_name(self,):
        return self.__first_name

    def get_last_name(self,):
        return self.__last_name

    def get_hire_date(self,):
        return self.__hire_date



class Contractor(Worker):
    def __init__(self, id_num: int, worker_type, first_name, last_name, hire_date, rate: float ):
        self.__salary = salary
        super().__init__(id_num, worker_type, first_name, last_name, hire_date,)

    def get_rate(self):
        return self.__rate

    def set_rate(self, rate):
        self.__rate = rate

class Employee(Worker):
    def __init__(self, id_num: int, first_name, last_name, hire_date,salary: float ):
        self.__rate = rate
        super().__init__(id_num, hire_date, first_name, last_name )

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary






class Task:
    def __init__(self, task_id: int, task_name: str, description: str, assigned_to: Worker, duration_hour: float, ):
        self.__task_id = task_id
        self.__task_name = task_name
        self.__description = description
        self.__assigned_to = assigned_to
        self.__duration_hour = duration_hour


class Project:
    def __init__(self, project_id: int, project_name: str, hour_est: int, hours_act: int ):

        self.__project_id = project_id
        self.__project_name = project_name
        self.__hour_est = hour_est
        self.__hours_act = hours_act

    def set_project_name(self, project_name: str):
        self.__project_name = project_name

    def set_hour_est(self, hour_est: int):
        self.__hour_est = hour_est

    def set_hour_act(self, hour_act: int):
        self.__hour_act = hour_act

    