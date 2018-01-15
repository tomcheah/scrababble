
from random import *

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vowels = ['a','e','i','o','u','y']

#Point categories
one_point = ['e','a','i','o','r','t','l','s','u']
two_point = ['d','n','g']
three_point = ['b','c','m','p']
four_point = ['f','h','v','w','y']
five_point = ['k']
eight_point = ['j','x']
ten_point = ['q','z']

list_of_players = []
round_num = 1

def start_game():
	global list_of_players, round_num
	print('Welcome to Scrababble!')
	print('How many players will be playing?')
	num_players = int(input())
	while num_players > 0:
		print('Please enter your name.')
		username = input()
		username = Player(username)
		list_of_players += [username]
		num_players -= 1 
	print('How many rounds would you like to play?')
	user_rounds = int(input())
	while round_num <= user_rounds:
		print('Round ' + str(round_num))
		one_round_play()
		round_num += 1
	end_game()

def end_game():
	scores = []
	for player in list_of_players:
		scores += [player.score]
	winning_score = max(scores)
	winning_score_index = scores.index(winning_score)
	winner = list_of_players[winning_score_index]
	print(str(winner.name) + ' has won the game!')

def one_round_play(): 
	for player in list_of_players: 
		letters = []
		for x in range(7):
			number = randint(0, 25)
			letters += alphabet[number]
		number = randint(0, 5)
		letters += vowels[number]
		print('This is your list of letters: ' + str(letters))
		print('Create a word from your list of letters. Each letter may only be used once.')
		word = input()
		player.scoring(word)

class Player: 
	def __init__(self, name):
		self.name = name
		self.score = 0
	def scoring(self, word):
		for letter in word:
			if letter in one_point:
				self.score += 1
			elif letter in two_point:
				self.score += 2
			elif letter in three_point:
				self.score += 3
			elif letter in four_point:
				self.score += 4
			elif letter in five_point:
				self.score += 5
			elif letter in eight_point:
				self.score += 8
			else:
				self.score += 10
		print(str(self.name) + ' has ' + str(self.score) + ' points.')

start_game()