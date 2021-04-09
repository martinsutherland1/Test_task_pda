### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# The game had no __init__ file to state what variables it could use within the functions

# The if statement is assigning the value of 1, rather than comparing. The else statment is missing a colon.
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
# The function won't run as it's called 'dif' instead of 'def'. There is no comma next to 'card1'. There is a indentation issue with if statement. The varible 'card' has no assignment so won't return a value.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# The indentation of the function is wrong. Total hasn't been assigned a value so when adding the card value there will be nothing to return an error as total is used before assignment. Total needs to be assigned to string before you can concatenate them.
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
