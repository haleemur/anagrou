__author__ = 'hali'

class Employee(object):

    def __init__(self, name, number, years_worked, salary):
        self._name = name
        self._number = number
        self._years_worked = years_worked
        self._salary = salary
        self._holiday_entitlement = 0

    def set_holiday(self, holiday_entitlement):
        self._holiday_entitlement = holiday_entitlement

    def get_name(self):
        return self._name

    def __repr__(self):
        obj_representation = "<Employee: name: {}, emp_number: {}, years_worked: {}, salary: {}, holiday {}>".format(
            self._name, self._number, self._years_worked, self._salary, self._holiday_entitlement)
        return obj_representation