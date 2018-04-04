# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestGrounds(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # And I handle everything except the grounds
        self.actionwords.i_handle_everything_except_the_grounds()

    def test_message_empty_grounds_is_displayed_after_30_coffees_are_taken_uid1b80f2ff095f42fc9ee6a025448af4f0(self):
        # Tags: priority:high
        # When I take "30" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 30)
        # Then message "Empty grounds" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Empty grounds")

    def test_when_the_grounds_are_emptied_message_is_removed_uid6b76fef5a7b54000afa6987069c08a6d(self):
        # Tags: priority:medium
        # When I take "30" coffees
        self.actionwords.i_take_coffee_number_coffees(coffee_number = 30)
        # And I empty the coffee grounds
        self.actionwords.i_empty_the_coffee_grounds()
        # Then message "Ready" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "Ready")
