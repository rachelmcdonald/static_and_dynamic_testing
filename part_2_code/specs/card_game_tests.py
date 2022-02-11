import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("hearts", 1)
        self.card1 = Card("club", 2)
        self.card_game = CardGame()
        self.cards = [self.card, self.card1]

    def test_check_for_ace_True(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card))

    def test_check_for_ace_False(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card1))

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card, self.card1)
        self.assertEqual(2, result.value)

    def test_cards_total(self):
        result = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 3", result)