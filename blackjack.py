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

	# def get_suit(self):
	# 	return self.suit

	def get_rank(self):
		return self.rank

class Deck:
	def __init__(self):
		self.deck = []
		for s in suits:
			for r in ranks:
				self.deck.append(Card(s, r))
		# self.shuffle()

	# def shuffle(self):
	# 	random.shuffle(self.deck)

	# def deal_card(self):
	# 	return self.deck.pop()

	def deal_card(self):
		return random.choice(self.deck)

	#to put cards into deck
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
		ace = False
		for card in self.hand:
			sum += values.get(card.get_rank())
			if card.get_rank()=='A':
				ace = True
		if ace and sum <=10:
				return sum+10
		else:
			return sum

		
		# num_aces = 0
		# base_points = 0
		# for card in self.hand:
		# 	if card == 'A':
		# 		num_aces +=1
		# 	else:
		# 		base_points +=values.get(card.get_rank())	
			## is this card an Ace?
			## if yes, num_aces += 1
			## else base_points += values.get(card.get_rank())


		# b = calc_point (base_points, num_aces)
		# protocol: 0 => busted, 
		# return b



	def hit(self, deck):
		c = deck.deal_card()
		self.add_card(c)
		

	def busted(self):
		sum=self.get_value()
		if sum > 21:
			return True

def deal():
	global player, dealer, deck
	deck = Deck()
	# deck.shuffle()

	player = Hand()
	dealer = Hand()

	player.add_card(deck.deal_card())
	player.add_card(deck.deal_card())
	dealer.add_card(deck.deal_card())
	dealer.add_card(deck.deal_card())

	print player

	# print ("Your cards: %s" %(Hand()))

in_game = False

def hit():	
	global in_game, score
	if in_game == True:
		player.hit(deck)
		if player.busted():
			print ("You are busted!")
			print ("Deal again?")
			score-=1						
			in_game = False
		if player.get_value() == 21:
			print ("Horray, you got blackjack!")
			print ("Deal again?")
			score+=1
			in_game = False
		

def stand():
	global in_game, score
	if in_game == True:
		while dealer.get_value () < 17:
			dealer.hit(deck)
			if dealer.busted():
				print ("Dealer is busted!")
				score+=1
		if not dealer.busted() and dealer.get_value() > player.get_value():
				print ("Dealer won. It's not your day.")
				score-=1
		if not dealer.busted():
			if dealer.get_value()==player.get_value():
				print ("It's a push, no winners.")
		if not dealer.busted():
			if dealer.get_value < player.get_value():
				print ("You win! Good job!")
				score+=1
	in_game = False
	print ("Deal again?")



while True:
	deal()
	in_game=True

	while in_game:
		y = raw_input("wanna hit? y/n")
		if y == 'y':
			hit()		
			print player
		else:
			stand()
	y = raw_input ("Play again? y/n")
	if y != 'y':
		break


# while True:
# 	deal()
# 	in_game = True
    
#     is_players_turn = True
# 	while in_game:
# 		if is_players_turn:
# 			y = raw_input("play again? ")
# 			if y == 'y':
# 		    	hit(target)
# 		   	else:
# 		   		is_players_turn = False
# 		else:
# 			if get_value < 17
# 				hit(dealer)
# 			else:
# 				#calc 

# 	y = raw_input("play again? ")







# 	print player
# 	print len(deck.deck)

# 	deck.return_cards(player.hand)
# 	print len(deck.deck)
# deal ()

	


