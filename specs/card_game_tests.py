import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        card1 = Card("Hearts", 1)
        card2 = Card("Clubs", 5)
        self.card_game = CardGame(card1, card2)
    
    def test_game_has_cards(self):
        cards = None
        if self.card_game.cards ==  None:
            cards = False
        return cards
        self.assertEqual(True, cards)
    
    def test_check_for_ace(self):
        card1 = Card("Hearts", 1)
        ace = self.card_game.check_for_ace(card1)
        self.assertEqual(True, ace)
    
    def test_check_card_not_ace(self):
        card2 = Card("Clubs", 5)
        ace = self.card_game.check_for_ace(card2)
        self.assertEqual(False, ace)
    
    def test_highest_card(self):
        card1 = Card("Hearts", 1)
        card2 = Card("Clubs", 5)
        high_card = self.card_game.highest_card(card1, card2)
        self.assertEqual(card2, high_card)
    
    def test_card_total(self):
        card1 = Card("Hearts", 1)
        card2 = Card("Clubs", 5)
        cards = (card1, card2)
        total = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 6", total)



        

    



   



    
    
   
