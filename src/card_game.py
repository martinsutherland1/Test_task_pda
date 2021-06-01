### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

# from src.card import Card

class CardGame:
      def __init__(self, card1, card2):
            self.card1 = card1
            self.card2 = card2
            self.cards = [card1, card2]


      def check_for_ace(self, card1):
        if card1.value == 1:
            return True
        return False
   

      def highest_card(self, card1, card2):
        if card1.value > card2.value:
          return card1
        else:
          return card2
  


      def cards_total(self, cards):
        total = 0

        for card in cards:
          total += card.value
        return "You have a total of " + str(total)

  


