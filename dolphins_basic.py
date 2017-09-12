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
		self.age += 1
		if (self.has_procreated):
			self.years_since_procreation += 1
		if (self.age >= self.death):
			print("A dophin named {} died at age {}".format(self.name, self.age))


	'''
	This function determines whether this dolphin and another can procreate.
	'''
	def request_procreation(self, other):
		if(self.age < 8):
			return false
		if(self.years_since_procreation < 5):
			return false
		if(self.father == other.father and self.mother == other.father):
			return false
		if(other.age < 8):
			return false
		return true
