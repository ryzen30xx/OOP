from random import randint
from requests import get
from requests import post

num_char = ""

class fshare:
	def __init__(self, fchar, length):
		self.__fchar = fchar;


	def rand_num_char(self, length):
		for i in range(length):
			num_rand = randint(0, 9);
			