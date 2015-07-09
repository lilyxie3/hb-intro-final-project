import random

# define tuples and dictinaries for cards
suits = ('Club', 'Spade', 'Heart', 'Diamond')
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
# ranks = ('A', 'J', 'Q', 'K')
values = {'A':1,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

# initialize some global variables for tracking scores and lists of cards
score = 0
dealer = []
player = []
deck = []

# define Card class
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


# deine Deck class
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
	# def return_cards(self, cards):
	# 	for card in cards:
	# 		self.deck.append(card)

# define Hand class
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

	def get_card(self, index):
		return self.hand[index]

# ace counts as 1, if the hand has an ace and the sum (including ace=1) is equal or less than 10, then add 11 to hand value
	def get_value(self):
		sum=0
		ace = False
		for card in self.hand:
			sum += values.get(card.get_rank())
			if card.get_rank()=='A':				
				ace = True

		if ace and sum <=11:
			return sum+10
		else:
			return sum


	def hit(self, deck):
		c = deck.deal_card()
		self.add_card(c)
		

	def busted(self):
		sum=self.get_value()
		if sum > 21:
			return True

#define dealer's hand and player's hand and print out the cards
def deal():
	global player, dealer, deck, score, in_game
	deck = Deck()
	# deck.shuffle()

	player = Hand()
	dealer = Hand()

	player.add_card(deck.deal_card())
	player.add_card(deck.deal_card())
	dealer.add_card(deck.deal_card())
	dealer.add_card(deck.deal_card())

	# print player's cards
	# print dealer's cards

	print "Your cards:\n%s" % str(player)
	print "Dealer's card:\n%s" % str(dealer.get_card(0))
	
	if player.get_value()== 21:
		print ("Horray, you got blackjack!")
		score+=1
		in_game = False

in_game = False

def hit():	
	global in_game, score
	if in_game == True:
		player.hit(deck)
		#print player's cards, if the hand is in play, play hits
		if player.busted():
			print ("You are busted!")
			# print score
			score-=1						
			in_game = False
		

def stand():
	global in_game, score
	if in_game == True:
		# if hand is in play, dealer continues to hit until his hand has a value > 17
		while dealer.get_value () < 17:
			dealer.hit(deck)
			#print dealer's cards
			if dealer.busted():
				print ("Dealer is busted!")
				score+=1				
				break
			#print a message to outcome and update score
		if not dealer.busted() and dealer.get_value() > player.get_value():
				print ("Dealer won. It's not your day.")
				score-=1
		if not dealer.busted():
			if dealer.get_value()==player.get_value():
				print ("It's a push, no winners.")
		if not dealer.busted():
			if dealer.get_value() < player.get_value():
				print ("You win! Good job!")
				score+=1

	in_game = False

# starts game
readme_file = open('README.md', 'r')
for line in readme_file:
	print line

print("Now starting...\n")

while True:
	in_game=True
	deal()	

	while in_game:
		y = raw_input("wanna hit? y/n\n")
		if y == 'y':
			hit()		
			print "Your cards:\n%s" % str(player)
			# print dealer.get_card(0)
		else:
			stand()
			print "Dealer's cards:\n%s" % str(dealer)

	else:
		print "your score is: %i" % int(score)
		y = raw_input ("Deal again? y/n\n")
		if y != 'y':
			break 
	
print player
print len(deck.deck)

# deck.return_cards(player.hand)
# print len(deck.deck)

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

	


