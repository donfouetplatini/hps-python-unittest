# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestServeCoffee(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_simple_use_uidac82fb5a87254b9f81cc98f8c85e8bf9(self):
        # Well, sometimes, you just get a coffee.
        # Tags: priority:high
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I take a coffee
        self.actionwords.i_take_a_coffee()
        # Then coffee should be served
        self.actionwords.coffee_should_be_served()
