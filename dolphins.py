import random

class Dolphin(object):

	def __init__(self, name, sex, mother, father):
		self.name = name
		self.sex = sex
		self.age = 0
		self.mother = mother
		self.father = father
		self.has_procreated = False
		self.years_since_procreation = 0
		self.death = round(random.gauss(35, 5))

	'''
	This function is used to keep track of the dolphin's age and years since procreation,
	and determines if the dolphin has died.
	'''
	def age_record(self):
		if (self.age > self.death):
			return True
		self.years_since_procreation += 1
		self.age += 1
		return False

	def canBreed(self):
		return (dolphin.age > 8 and not dolphin.has_procreated) or (dolphin.age > 8 and dolphin.years_since_procreation > 5)

	'''
	This function determines whether this dolphin and another can procreate.
	'''
	def request_procreation(self, other):
		if(self.age < 8 or other.age < 8):
			return False
		#This if statement is seriously the difference between averaging 2000, 3000, and 4000 dolphins for each trial
		if(self.years_since_procreation < 5 or other.years_since_procreation <= 5):
			return False

		if(abs(self.age - other.age > 10)):
			return False
		
		if(self.sex == other.sex):
			return False
		
		if(other.father == self.name or self.name == other.father or other.mother == self.name or self.name == other.mother):
			return False
		if(self.father == other.father and self.mother == other.mother):
			return False

		self.years_since_procreation = 0
		self.has_procreated = True
		other.years_since_procreation = 0
		other.has_procreated = True
		return True

	def __str__(self):
		return "A dolphin named {} (age {}, last procrastinated {} years ago, set to die at age {})".format(self.name, self.age, self.years_since_procreation, self.death)