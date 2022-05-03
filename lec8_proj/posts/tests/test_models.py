from django.test import TestCase
from ..models import *


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass


    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass


    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)


    def test_false_is_true(self):
        print("Method: test_true_is_true.")
        bool =True
        self.assertTrue(bool)


    def test_is_equal(self):
        post=Categories()
        print("Equal")
        self.assertEqual(post.is_equal(),1)


    # def test_one_pus_one(self):
    #     print("two")
    #     self.assertEqual(1+1,2)


