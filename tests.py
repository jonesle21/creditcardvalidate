# Author: Laura Jones
# Date: 5/3/2021

import random
import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValid(unittest.TestCase):

    def testLength(self):
        """testing length between 0 - 17"""
        for i in range(0, 100000):
            val = random.randint(0, 99999999999999999)
            credit_card_validator(str(val))

    def testVisa1(self):
        """testing length 16 with prefix 4"""
        for i in range(0, 100000):
            val = random.randint(4000000000000000, 4999999999999999)
            credit_card_validator(str(val))

    def testVisa2(self):
        """testing length 15 with prefix 4"""
        for i in range(0, 100000):
            val = random.randint(400000000000000, 499999999999999)
            credit_card_validator(str(val))

    def testVisa3(self):
        """testing length 17 with prefix 4"""
        for i in range(0, 100000):
            val = random.randint(40000000000000000, 49999999999999999)
            credit_card_validator(str(val))

    def testMC1(self):
        """testing length 16 with prefix 51-55"""
        for i in range(0, 100000):
            val = random.randint(5100000000000000, 5599999999999999)
            credit_card_validator(str(val))

    def testMC2(self):
        """testing length 16 with prefix 2221-2720"""
        for i in range(0, 100000):
            val = random.randint(2221000000000000, 2720999999999999)
            credit_card_validator(str(val))

    def testAmex1(self):
        """testing length 15 with prefix 34-55"""
        for i in range(0, 100000):
            val = random.randint(340000000000000, 349999999999999)
            credit_card_validator(str(val))

    def testAmex2(self):
        """testing length 15 with prefix 37"""
        for i in range(0, 10000):
            val = random.randint(370000000000000, 379999999999999)
            credit_card_validator(str(val))

    def testAmex3(self):
        """testing length 16 with prefix 37"""
        for i in range(0, 100000):
            val = random.randint(3700000000000000, 3799999999999999)
            credit_card_validator(str(val))

    def testAmex4(self):
        """testing length 16 with prefix 34"""
        for i in range(0, 100000):
            val = random.randint(3400000000000000, 3499999999999999)
            credit_card_validator(str(val))


if __name__ == '__main__':
    unittest.main()
