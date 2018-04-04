# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestSupportInternationalisation(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def messages_are_based_on_language(self, language, ready_message):
        # Tags: priority:medium
        # When I start the coffee machine using language "<language>"
        self.actionwords.i_start_the_coffee_machine_using_language_lang(lang = language)
        # Then message "<ready_message>" should be displayed
        self.actionwords.message_message_should_be_displayed(message = ready_message)

    def test_Messages_are_based_on_language_english_uidd0ea589b21c24c49b4c68539841ae0f0(self):
        self.messages_are_based_on_language(language = 'en', ready_message = 'Ready')

    def test_Messages_are_based_on_language_french_uid93b02222348a4374b79e1803cf126db5(self):
        self.messages_are_based_on_language(language = 'fr', ready_message = 'Pret')



    def test_no_messages_are_displayed_when_machine_is_shut_down_uidc414a32b9be64775bccbb3507825d4bb(self):
        # Tags: priority:medium
        # Given the coffee machine is started
        self.actionwords.the_coffee_machine_is_started()
        # When I shutdown the coffee machine
        self.actionwords.i_shutdown_the_coffee_machine()
        # Then message "" should be displayed
        self.actionwords.message_message_should_be_displayed(message = "")
