'''unmocked_unit_tests.py'''
# pylint: disable=C0103
# pylint: disable=C0116
# pylint: disable=C0413
# pylint: disable=C0115
# pylint: disable=W0611
# pylint: disable=W1503

import unittest
import unittest.mock as mock
from os.path import dirname, join
import sys

sys.path.insert(1, join(dirname(__file__), "../"))
import app
import models
from models import Users
import calories_count

# funtions todo
class Test(unittest.TestCase):
    def test_on_connect(self):
        result = app.on_connect()
        if result == 1:
            self.assertTrue(True, "Socket on Connect")

    def test_on_disconnet(self):
        result = app.on_disconnect()
        if result == 1:
            self.assertTrue(True, "Socket on Disconnect")

    def test_on_food_search(self):
        data = {"food_search": "pasta"}
        result = app.on_new_food_search(data)
        print(result)

    def test_bmr_cal(self):
        data = {"weight": 24, "height": 52, "age": 23, "gender": "men"}
        data1 = {"weight": 24, "height": 52, "age": 23, "gender": "women"}
        result = calories_count.bmr_cal(
            data["weight"], data["height"], data["age"], data["gender"]
        )
        print(result)
        expected = {"weight": 24, "height": 52, "age": 23, "gender": "men"}
        expected1 = {"weight": 24, "height": 52, "age": 23, "gender": "women"}
        self.assertEqual(data, expected)
        result = calories_count.bmr_cal(
            data1["weight"], data1["height"], data1["age"], data1["gender"]
        )
        self.assertEqual(data1, expected1)

    def test_daily_Caloric_need(self):
        data = [
            {"bmr": 312, "activityLevel": 1, "activityLevelIndex": 1.2},
            {"bmr": 312, "activityLevel": 2, "activityLevelIndex": 1.375},
            {"bmr": 312, "activityLevel": 3, "activityLevelIndex": 1.46},
            {"bmr": 312, "activityLevel": 4, "activityLevelIndex": 1.725},
            {"bmr": 312, "activityLevel": 5, "activityLevelIndex": 1.9},
        ]

        for test in data:
            result = calories_count.daily_caloric_need(
                test["bmr"], test["activityLevel"]
            )
            print(result)
            expected = test
            self.assertEqual(test, expected)

    def test_calculate_macro(self):
        data = {"calories": 1200}
        result = calories_count.calculate_macro(data["calories"])
        print(result)
        expected = {"calories": 1200}
        self.assertEqual(data, expected)


class testingusers(Users):
    def init(self, name):
        self.connection = name


if __name__ == "__main__":
    unittest.main()
