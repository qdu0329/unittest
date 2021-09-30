import unittest
import random
import sys
import datetime
from impl import PhysicalInfo


class TestPhysicalInfo(unittest.TestCase):

    def setUp(self):
        self.physicalinfo =	PhysicalInfo()

    def teardown(self):
        self.physicalinfo = None

    def test_set_name(self):
        self.assertEqual(None, self.physicalinfo.set_name("abc"))
        self.assertRaises(ValueError, self.physicalinfo.set_name, 2)
        self.assertRaises(ValueError, self.physicalinfo.set_name, False)
        self.assertRaises(ValueError, self.physicalinfo.set_name, 2.2)
        self.assertRaises(ValueError, self.physicalinfo.set_name, "2")
        self.assertRaises(ValueError, self.physicalinfo.set_name, "")

        for notion in [char for char in "`~!@#$%^&*()_+|}{\":?><,./;'[]="]:
            self.assertRaises(ValueError, self.physicalinfo.set_name, "abc"+notion)
            self.assertRaises(ValueError, self.physicalinfo.set_name, notion)

        self.assertTrue(self.set_name_helper("abc"))
        self.assertTrue(self.set_name_helper("ab c"))
        self.assertTrue(self.set_name_helper("ab-c"))
        self.assertTrue(self.set_name_helper("a b-c"))
        self.assertTrue(self.set_name_helper("a b c"))
        self.assertTrue(self.set_name_helper("a-b-c"))
        self.assertTrue(self.set_name_helper("a -   b -  c"))

    def set_name_helper(self, name):

        try:
            self.physicalinfo.set_name(name)
            return True
        except:
            return False

    def test_set_gender(self):

        for index in range(178):
            char = chr(index)
            if char not in ["F", "M"]:
                self.assertRaises(ValueError, self.physicalinfo.set_gender, char)

        self.assertEqual(None, self.physicalinfo.set_gender("M"))
        self.assertRaises(ValueError, self.physicalinfo.set_gender, "MMM")
        self.assertRaises(ValueError, self.physicalinfo.set_gender, 2)
        self.assertRaises(ValueError, self.physicalinfo.set_gender, False)
        self.assertRaises(ValueError, self.physicalinfo.set_gender, 2.2)

    def test_set_height(self):
        self.assertEqual(None, self.physicalinfo.set_height(67))
        self.assertRaises(ValueError, self.physicalinfo.set_height, 2.2)
        self.assertRaises(ValueError, self.physicalinfo.set_height, False)
        self.assertRaises(ValueError, self.physicalinfo.set_height, "74")
        self.assertRaises(ValueError, self.physicalinfo.set_height, "abc")

        for index in range(178):
            char = chr(index)
            self.assertRaises(ValueError, self.physicalinfo.set_height, char)

        for i in range(100):
            num = random.randint(0, 16)
            self.assertRaises(ValueError, self.physicalinfo.set_height, num)

        for i in range(100000):
            num = random.randint(85, sys.maxsize)
            self.assertRaises(ValueError, self.physicalinfo.set_height, num)

    def test_set_temperature(self):
        self.assertEqual(None, self.physicalinfo.set_temperature(96.2))
        self.assertRaises(ValueError, self.physicalinfo.set_temperature, False)
        self.assertRaises(ValueError, self.physicalinfo.set_temperature, "7.4")
        self.assertRaises(ValueError, self.physicalinfo.set_temperature, "abc")

        for index in range(178):
            char = chr(index)
            self.assertRaises(ValueError, self.physicalinfo.set_temperature, char)

        for i in range(1000):
            num = random.uniform(.0, 94.9)
            self.assertRaises(ValueError, self.physicalinfo.set_temperature, num)

        for i in range(100000):
            num = random.uniform(104.1, sys.maxsize)
            self.assertRaises(ValueError, self.physicalinfo.set_temperature, num)

    def test_set_date(self):
        self.assertEqual(None, self.physicalinfo.set_date('12-6-2020'))
        self.assertRaises(ValueError, self.physicalinfo.set_date,  2)
        self.assertRaises(ValueError, self.physicalinfo.set_date,  2.2)
        self.assertRaises(ValueError, self.physicalinfo.set_date,  False)


        start = datetime.datetime.strptime('1-1-0001', '%m-%d-%Y')
        end = datetime.datetime.strptime('12-31-1989', '%m-%d-%Y')
        for i in range(1000):
            self.assertRaises(ValueError, self.physicalinfo.set_date,  self.set_date_helper(start, end))


        start = datetime.datetime.strptime('01-01-2101', '%m-%d-%Y')
        end = datetime.datetime.strptime('12-31-9999', '%m-%d-%Y')
        for i in range(1000):
            self.assertRaises(ValueError, self.physicalinfo.set_date,  self.set_date_helper(start, end))


        start = datetime.datetime.strptime('1-1-0001', '%d-%m-%Y')
        end = datetime.datetime.strptime('31-12-1989', '%d-%m-%Y')
        for i in range(1000):
            self.assertRaises(ValueError, self.physicalinfo.set_date,  self.set_date_helper(start, end))


        start = datetime.datetime.strptime('01-01-2101', '%d-%m-%Y')
        end = datetime.datetime.strptime('31-12-9999', '%d-%m-%Y')
        for i in range(1000):
            self.assertRaises(ValueError, self.physicalinfo.set_date,  self.set_date_helper(start, end))

    def set_date_helper(self, start, end):

        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + datetime.timedelta(seconds=random_second)

if	__name__	==	'__main__':
    unittest.main()
