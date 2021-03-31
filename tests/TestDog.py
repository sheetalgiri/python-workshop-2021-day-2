import unittest
from projects.zoo.dog import Dog

class TestDog(unittest.TestCase):
    def setUp(self):
        # This is called immediately before calling the test method; more info https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
        self.dog = Dog("tommy",10)

    def test_bark(self):
        the_dog_says= self.dog.bark()
        self.assertEqual(the_dog_says, "bow", "Incorrect Answer")

if __name__ == '__main__':
    unittest.main()

#run with python -m unittest tests.TestDog