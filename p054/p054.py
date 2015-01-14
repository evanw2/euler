#!/usr/bin/env python

"""

In the card game poker, a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the 
highest value wins; for example, a pair of eights beats a pair of fives 
(see example 1 below). But if two ranks tie, for example, both players 
have a pair of queens, then highest cards in each hand are compared 
(see example 4 below); if the highest cards tie then the next highest 
cards are compared, and so on.

Consider the following five hands dealt to two players:

< See examples on projecteuler.net >


The file, poker.txt, contains one-thousand random hands dealt to two 
players. Each line of the file contains ten cards (separated by a 
single space): the first five are Player 1's cards and the last five are 
Player 2's cards. You can assume that all hands are valid (no invalid 
characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?

"""

# Pratice with classes, although maybe not necessary

class Card:
   rank_nums = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 
                'T':10, 'J':11, 'Q':12, 'K':13, 'A':14 }
   def __init__(self, card):
      """ 'card' will be a two character string """
      assert len(card) == 2
      self.rank = card[0]
      self.suit = card[1]
   def __cmp___(self, other):
      return cmp(rank_nums[self.rank], rank_nums[other.rank])
   def rank_num(self):
      return self.rank_nums[self.rank]

      
class HandType:
   # There might be better ways to make an enum 
   HIGH_CARD = 0
   ONE_PAIR = 1
   TWO_PAIR = 2
   THREE_OF_A_KIND = 3
   STRAIGHT = 4
   FLUSH = 5
   FULL_HOUSE = 6
   FOUR_OF_A_KIND = 7
   STRAIGHT_FLUSH = 8

class Hand:
   cards = []

   def __init__(self, hand):
      """ 'hand' will be a list of 5 card strings."""
      self.cards = [Card(x) for x in hand]
      self.rank_nums = sorted([c.rank_num() for c in self.cards])
      #determine the type of the hand
      f = self.flush()
      s = self.straight()
      if f and s:
         self.hand = HandType.STRAIGHT_FLUSH
      elif f:
         self.hand = HandType.FLUSH
         return
      elif s:
         self.hand = HandType.STRAIGHT
         return
      grps = sorted([g[0] for g in self.groups()])
      if grps == [1,4]:
         self.hand = HandType.FOUR_OF_A_KIND
      elif grps == [2,3]:
         self.hand = HandType.FULL_HOUSE
      elif grps == [1,1,3]:
         self.hand = HandType.THREE_OF_A_KIND
      elif grps == [1,2,2]:
         self.hand = HandType.TWO_PAIR
      elif grps == [1,1,1,2]:
         self.hand = HandType.ONE_PAIR
      else:
         assert grps == [1,1,1,1,1]
         self.hand = HandType.HIGH_CARD

   # returns a list of groups in the hand.
   # Example: [7,7,J,Q,Q] becomes [(2,7),(1,J),(2,Q)]
   def groups(self):
      grps = []
      count = 1
      rk = self.rank_nums[0]
      for i in range(1,5):
         if self.rank_nums[i] == rk:
            count += 1
         else:
            grps.append((count, rk))
            count = 1
            rk = self.rank_nums[i]
      grps.append((count,rk))
      return grps
   
   # Tests this hand for a flush
   def flush(self):
      for c in self.cards:
         if c.suit != self.cards[0].suit:
            return False
      return True

   # Tests this hand for a straight
   def straight(self):
      ranks = sorted([c.rank_num() for c in self.cards])
      # special case for ace-low straight
      if ranks == [2,3,4,5,14]:
         return True
      for i in range(4):
         if ranks[i+1] - ranks[i] != 1:
            return False
      return True

   def __cmp__(self, other):
      return cmp(self.comparable_rep(), other.comparable_rep())

   # returns a tuple of the comparable properties of a hand
   #  in descending priority, so that the tuples can be compared
   #  lexicographically. Conveniently, the 'groups' function is
   #  exactly what is needed for hands of the same type.
   def comparable_rep(self):
      return (self.hand, sorted(self.groups(), reverse = True))


f = open("poker.txt")
p1 = 0
for line in f:
   cards = line.strip().split()
   hand1 = Hand(cards[0:5])
   hand2 = Hand(cards[5:10])
   if hand1 > hand2:
      p1 += 1

print p1
   


