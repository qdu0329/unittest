
import re
from datetime import datetime
class PhysicalInfo():

    def __init__(self):
        self.date = None
        self.name = None
        self.gender = None
        self.height = None
        self.temperature = None

    def set_name(self, name):

        if not isinstance(name, str):
            raise ValueError

        reg = re.search(r'[^a-z\s-]', name)
        if reg != None:
            raise ValueError

        reg = re.match(r'([\s-]*[a-zA-Z][\s-]*){3}', name)
        if reg == None:
            raise ValueError

        reg = re.search(r'[a-zA-Z]+', name)
        if reg == None:
            raise ValueError

        self.name = name


    def set_gender(self, gender):
        if not isinstance(gender, str):
            raise ValueError

        if len(gender) != 1:
            raise ValueError

        reg = re.match(r'[^FM]', gender)
        if reg != None:
            raise ValueError

        self.gender = gender


    def set_height(self, height):
        if not isinstance(height, int):
            raise ValueError

        if 84 < height or height < 17:
            raise ValueError

        self.height = height

    def set_temperature(self, temp):

        if not isinstance(temp, float):
            raise ValueError

        if 104 < temp or temp < 95:
            raise ValueError

        self.temperature = temp

    def set_date(self, date):

        if not isinstance(date, str):
            raise ValueError

        tmp = ""
        try:
            tmp = datetime.strptime(date, '%d-%m-%Y')
        except:
            tmp = datetime.strptime(date, '%m-%d-%Y')

        try:
            if 2100 < tmp.year or tmp.year < 1900:
                raise ValueError
        except:
            raise ValueError


        self.date = date
