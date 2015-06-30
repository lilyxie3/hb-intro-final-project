import random

suits = ('Club', 'Spade', 'Heart', 'Diamond')
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values = {'A':1,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

score = 0
dealer = []
player = []
deck = []

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.suit + " of " + self.rank

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
		self.shuffle()

	def shuffle(self):
		random.shuffle(self.deck)

	def deal_card(self):
		return self.deck.pop()

	def return_cards(self, cards):
		for card in cards:
			self.deck.append(card)

class Hand:
	def __init__(self):
		self.hand=[]

	def __str__(self):
		output_string = ""
		for card in self.hand:
			output_string += str(card) + '\n' #card.get_suit() + card.get_rank()
		return output_string

	def add_card(self, card):
		self.hand.append(card)

# ace counts as 1, if the hand has an ace and the sum (including ace=1) is equal or less than 10, then add 10 to hand value
	def get_value(self):
		sum=0
		for card in self.hand:
			sum += values.get(card.get_rank())
			if card.get_rank()=='A' and sum <=10:
				return sum+10
			else:
				return sum

	def hit(self, deck):
		self.add_card(deck.deal_card())
	def busted(self, deck):
		sum=self.get_value()
		if sum > 21:
			return True

def deal():
	deck = Deck()
	deck.shuffle()
	player = Hand()
	dealer = Hand()

	player.add_card(deck.deal_card())
	player.add_card(deck.deal_card())

	print player
	print len(deck.deck)

	deck.return_cards(player.hand)
	print len(deck.deck)
deal ()

	


