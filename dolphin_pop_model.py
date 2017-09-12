from __future__ import print_function
from dolphins import Dolphin
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
# import os.path
from random import random
import re
from string import ascii_lowercase
import urllib2

def get_names(sex):
    writer = open("{}_names.dat".format(sex), "w")
    for i in range(1, 212):
        url = "http://www.prokerala.com/kids/baby-names/{}/page-{}.html".format(sex, i)
        inputfile = urllib2.urlopen(url)
        input_html = inputfile.read() 
        names = re.findall("<span class=\"a nameDetails\">(.*)</span>", input_html)

        for name in names:
            writer.write(name)
            writer.write("\n")
    writer.close()

def generate_male_names():
    i = 0
    names = open("boy_names.dat", "r").read().splitlines()
    use_middle_names = False

    while(True):
        if(use_middle_names):
            middle_name = "".join(sample(ascii_lowercase, 10))
            yield "{} {}".format(names[i], middle_name)
        else:
            yield names[i]

        i += 1

        if(i >= len(names)):
            i = 0;
            use_middle_names = True

def generate_female_names():
    i = 0
    names = open("girl_names.dat", "r").read().splitlines()
    use_middle_names = False

    while(True):
        if(use_middle_names):
            middle_name = "".join(sample(ascii_lowercase, 10))
            yield "{} {}".format(names[i], middle_name)
        else:
            yield names[i]

        i += 1
        if(i >= len(names)):
            i = 0;
            use_middle_names = True

# I am a Windows user, but this is how I would automatically run my name 
# scraper if we didn't already have the name data files
# if(os.path.exists("girl_names.dat")):
# 	get_names("girl")
# if(os.path.exists("boy_names.dat")):
# 	get_names("boy")

def do_growth_cycle(dolphin_pool):
	for dolphin in dolphin_pool:
		if(dolphin.age_record()):
			dolphin_pool.remove(dolphin)

def breed(sex, dolphin_1, dolphin_2, dolphin_pool, generator):
	if(dolphin_1.sex == "Male"):
		dolphin_pool.append(Dolphin(generator.next(), sex, dolphin_2.name, dolphin_1.name))
	else:
		dolphin_pool.append(Dolphin(generator.next(), sex, dolphin_1.name, dolphin_2.name))

def plotGeneology(dolphin_pool):

	lucky = np.random.choice(np.array(dolphin_pool), 1)[0]
	parents = [lucky.mother, lucky.father]

	half_sibs1 = []
	half_sibs2 = []
	full_sibs = []


	for dolphin in dolphin_pool:
		if dolphin.mother == lucky.mother:
			if dolphin.father == lucky.father and not lucky is dolphin:
				full_sibs.append(dolphin)
			else:
				half_sibs1.append(dolphin)
		elif dolphin.father == lucky.father:
			half_sibs2.append(dolphin)

	#Uncomment this out to verify that the geneology plot is correct
	# print("I am {}".format(lucky.name))
	# print("Parents: ", parents[0], " ", parents[1])
	# print("Mother's others ")
	# for sibling in half_sibs1:
	# 	print(sibling.name)
		
	# print("Father's others ")
	# for sibling in half_sibs2:
	# 	print(sibling.name)

	# print("Full siblings: ")
	# for sibling in full_sibs:
	# 	print(sibling.name)

	siblings = half_sibs1 + full_sibs + half_sibs2

	g = nx.DiGraph()
	pos = {}
	g.add_node(lucky.name)			
	pos[lucky.name] = (-1, 0.5)
	g.add_node(lucky.mother)
	pos[lucky.mother] = (-1, 2)
	g.add_node(lucky.father)
	pos[lucky.father] = (-0.5 + 0.33*(len(half_sibs1) + 1), 2)
	var = -1
	for sibs in siblings:
		g.add_node(sibs.name)
		if sibs.mother == lucky.mother and sibs.father == lucky.father:
			pos[sibs.name] = (var, 0.5)
			g.add_edge(lucky.mother, sibs.name)
			g.add_edge(lucky.father, sibs.name)
		else:
			if sibs.mother == lucky.mother:
				g.add_edge(lucky.mother, sibs.name)
			else:
				g.add_edge(lucky.father, sibs.name)
			pos[sibs.name] = (var, -1)
		var += 1

	plt.figure()
	nx.draw(g, pos=pos, with_labels =True)
	# plt.show()
	plt.savefig("genealogy.png")

def debug(dolphin_pool):
	for dolphin in dolphin_pool:
		print(dolphin)


'''
<!--Midterm Project Part II A-->

Finds the average number of living dolphins and the standard deviation for each of the 150 years.
Evolves a growing dolphin population at least 10 times in order to caculate an accurate mean and the standard deviation.
On each trial, the information for the population every 25 years is printed out. At year 100, the total number of dolphins
is also logged.
'''
num_trials = 10
years_per_trial = 150
report_frequency = 25
male_chance = 0.5

populations = [[] for i in range(years_per_trial)]

for i in range(num_trials):	

	male_name_generator = generate_male_names()
	female_name_generator = generate_female_names()

	dolphin_pool = [Dolphin(male_name_generator.next(), "Male", female_name_generator.next(), male_name_generator.next()),
		Dolphin(male_name_generator.next(), "Male", female_name_generator.next(), male_name_generator.next()),
		Dolphin(female_name_generator.next(), "Female", female_name_generator.next(), male_name_generator.next()),
		Dolphin(female_name_generator.next(), "Female", female_name_generator.next(), male_name_generator.next())]

	breedings_for_year = 0

	print("\n")
	print("Trial No. {}".format(i + 1))
	for j in range(years_per_trial):

		num_breeding = 0
		if(j % report_frequency == 0):
			for dolphin in dolphin_pool:
				if(dolphin.age > 8 and not dolphin.has_procreated) or (dolphin.age > 8 and dolphin.years_since_procreation > 5):
					num_breeding += 1

		if(j % report_frequency == 0):
			print("##################################################")
			print("entering year {} with {} dolphins, with {} breeding".format(j, len(dolphin_pool), num_breeding))		

		for dolphin in dolphin_pool:
			if (dolphin.age > 8 and not dolphin.has_procreated) or (dolphin.age > 8 and dolphin.years_since_procreation > 5):
				for possible_mate in np.random.choice(np.array(dolphin_pool), len(dolphin_pool)):
					# if (possible_mate.age > 8 and not possible_mate.has_procreated) or (possible_mate.age > 8 and possible_mate.years_since_procreation > 5):
					if dolphin.request_procreation(possible_mate):
						breedings_for_year += 1

						if (random() < male_chance):
							breed("Male", dolphin, possible_mate, dolphin_pool, male_name_generator)
						else:
							breed("Female", dolphin, possible_mate, dolphin_pool, female_name_generator)
						break


		do_growth_cycle(dolphin_pool)
		populations[j].append(len(dolphin_pool))
		
		if(j >= years_per_trial - 1):
			print("##################################################")
			print("at year {}, there are {} living dolphins".format(j, len(dolphin_pool)))
		if(j == 100):
			print("at year {}, there are {} living dolphins".format(j, len(dolphin_pool)))
			print("there have been {} births, in total.".format(breedings_for_year))
		
		
		if(i == 0 and j == 70):		#if this is the first trial and we're on year 70
			#<!--Midterm Project Part II C-->
			plotGeneology(dolphin_pool)

		if(len(dolphin_pool) <= 0):
			print("Oh no. All our dolphins for trial {} died at year {}".format(i, j))
			break


		#<!--end year loop-->
	print("\n")
	print("**************************************************")
	#<!--end trial loop-->

# Uncomment to see our shameful final populations
# print("Final populations")
# for i in range(num_trials):
# 	print("Trial {}: {}".format(i + 1, populations[-1][i]))
# print("\n")

meanNP = np.array([np.mean(np.asarray(year)) for year in populations])
print("Average end population: {}".format(meanNP[-1]))
stdNP = np.array([np.std(np.asarray(year)) for year in populations])
print("End standard deviation: {}\n".format(stdNP[-1]))
x = np.linspace(0, years_per_trial, years_per_trial)


plt.clf()
plt.figure(figsize=(5, 5))
plt.plot(x, meanNP, lw=1.5)
plt.fill_between(x, meanNP+stdNP, meanNP-stdNP, facecolor='red', interpolate=True, alpha=0.5)

plt.suptitle("Average Population and Standard Deviation from {} trials".format(num_trials))
plt.xlabel("Years")
plt.ylabel("Number of Living Dolphins")

plt.savefig("Population_growth.png", bbox_inches='tight')
# plt.show()


'''
<!--Midterm Project Part II B-->

Find the minimum probability of producing males (i.e., P(male)) such that the population
does not die out in 150 years. We accomplish this by systematically increasing P(male)
from 0 to 0.5 by 0.01 each time until the number of living dolphins is greater than 
zero at the end of year 149. We make sure to evolve the dolphin population at least five times
to produce a decently-accurate average minimum probability for P(male).
'''

debug = False	#Controls wether we output the status of the population at EVERY YEAR (warning: console spam)
min_evolutions = 10
min_chances = []
num_trials = 5

print("Part B")

for i in range(num_trials):
	
	happy_ending = False
	male_probability = 0.
	
	while(not happy_ending):
		dolphin_pool = [
			Dolphin(male_name_generator.next(), "Male", female_name_generator.next(), male_name_generator.next()),
			Dolphin(male_name_generator.next(), "Male", female_name_generator.next(), male_name_generator.next()),
			Dolphin(female_name_generator.next(), "Female", female_name_generator.next(), male_name_generator.next()),
			Dolphin(female_name_generator.next(), "Female", female_name_generator.next(), male_name_generator.next())
		]

		if(debug):
			print("Trial No. {}, probability {}".format(i + 1, male_probability))
		

		j = 0
		while j < years_per_trial and len(dolphin_pool) != 0:
			num_breeding = 0
			for dolphin in dolphin_pool:
				if (dolphin.age > 8 and not dolphin.has_procreated) or (dolphin.age > 8 and dolphin.years_since_procreation > 5):
					if(j % report_frequency == 0):
						num_breeding += 1
					for possible_mate in np.random.choice(np.array(dolphin_pool), len(dolphin_pool)):
						if(possible_mate.age > 8 and not possible_mate.has_procreated) or (possible_mate.age > 8 and possible_mate.years_since_procreation > 5):
							if(dolphin.request_procreation(possible_mate)):
								
								if (random() < male_probability):
									breed("Male", dolphin, possible_mate, dolphin_pool, male_name_generator)
								else:
									breed("Female", dolphin, possible_mate, dolphin_pool, female_name_generator)
								break

			if(j == years_per_trial - 1 and len(dolphin_pool) > 0):
				print("Trial {} made it to year {} with {} dolphins using a probability of  {}".format(i, j, len(dolphin_pool), male_probability))
				min_chances.append(male_probability)
				happy_ending = True
			do_growth_cycle(dolphin_pool)
			j += 1
		male_probability += 0.01

print("\n")
print("Average of {} trials: {}".format(num_trials, np.mean(np.array(min_chances))))
print("If this average wasn't close to 0.13, run the program again or try increasing the number of evolutions (current: {})".format(num_trials))

#<!end program -->