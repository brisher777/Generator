'''
Created on Feb 16, 2013

@author: ben
'''
import random
import hashlib

class Password(object):
	
	def __init__(self, lowercase, uppercase, special, numbers, min_length, max_length):
		self.lowercase   = int(lowercase)
		self.uppercase   = int(uppercase)
		self.special     = int(special)
		self.numbers     = int(numbers)
		self.min_length  = int(min_length)
		self.max_length  = int(max_length)
		self.total_length = (self.lowercase + self.uppercase + self.special + self.numbers)

		if self.min_length > self.total_length:
			self.lowercase += int(self.min_length - self.total_length)
		elif self.max_length < self.total_length:
			while self.max_length < self.total_length:
				if self.lowercase >= self.total_length - self.max_length and self.lowercase > 0:
					self.lowercase -= 1
					self.total_length -= 1
					print 'dec lower'
				elif self.uppercase > self.total_length - self.max_length and self.uppercase > 0:
					self.uppercase -= 1
					self.total_length -= 1
					print 'dec upper'
				elif self.special > self.total_length - self.max_length and self.special > 0:
					self.special -= 1
					self.total_length -= 1
					print 'dec spec'
				elif self.numbers > self.total_length - self.max_length and self.numbers > 0:
					self.numbers -= 1
					self.total_length -= 1
					print 'dec num'
				else:
					break
					
	
	def gen_lowercase(self):
		temp_list = []
		for x in range(self.lowercase):
			temp_list.append(chr(random.randint(97, 122)))
		return ''.join(temp_list)
	
	def gen_uppercase(self):
		temp_list = []
		for x in range(self.uppercase):
			temp_list.append(chr(random.randint(66, 90)))
		return ''.join(temp_list)
	
	def gen_special(self):
		temp_list = []		
		for x in range(self.special):
			temp_list.append(chr(random.randint(33, 47)))
		return ''.join(temp_list)
	
	def gen_numbers(self):
		temp_list = []		
		for x in range(self.numbers):
			temp_list.append(str(random.randint(0, 9)))
		return ''.join(temp_list)
	
	def mix_em_up(self, unshuffled):
		temp_list = []
		temp_list = list(unshuffled)
		random.shuffle(temp_list)
		final_string = ""

		for x in range(int(len(temp_list))):
			final_string += str(temp_list[x])

		return final_string

	def hash_it(self, shuffled):
		return hashlib.sha1(shuffled).hexdigest()
	
		
		





