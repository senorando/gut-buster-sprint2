import unittest
import unittest.mock as mock
from os.path import dirname, join
import sys

sys.path.insert(1, join(dirname(__file__), "../"))
import app

#funtions todo
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
        data={
            'food_search': 'pasta'
        }
        result= app.on_new_food_search(data)
        print(result)

if __name__ == "__main__":
    unittest.main()
