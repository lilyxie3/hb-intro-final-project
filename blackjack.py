import random

suits = ['Club', 'Spade', 'Heart', 'Diamond']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
values = {'A':1,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7 '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

class Card:
	def __int__(self, suit, rank):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return self.value + "of" + self.suit

	def get_suit(self):
		return self.suit
	def get_rank(self):
		return self.rank

class Deck:
	def __init__(self):
		self.deck = []
		for s in suits:
			for r in ranks:
				self.deck.append(Card(s, r))
	def shuffle(self):
		random.shuffle(self.deck)
	def deal_card(self):
		return self.deck.pop()

class Hand:
	def __init__(self):
		self.hand=[]
	# def __str__(self):
	def add_card(self, card):
		self.hand.append(card)

	def get_value(self):
		sum=0
		for card in self.hand
		sum = values.get(card.get_rank())
