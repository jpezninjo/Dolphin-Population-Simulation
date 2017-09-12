from __future__ import division, print_function
import random
import re
import urllib
import webbrowser 

''
part1 = "http://www.prokerala.com/kids/baby-names"
part2 = ["/boy", "/girl"]
part3 = "/page-"
number_of_names = 7500
number_of_pages = number_of_names / (35)
part5 = ".html"


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# part2 = ["girl.htm", "boy.htm"]
print(part2[0])
print(part2[1])
output_files = ["girl.dat", "boy.dat"]

# this is not a typo
# number_of_names = 7500
#this is also not a type
# calculusIII = (int)(number_of_names / len(alphabet))

for i in range(2):
	filenm = output_files[i]
	with open(filenm, "w") as f: 
		for j in range(int(number_of_pages)):
			# print(part1 + each_letter + boygirl)
			try:
				url = part1 + part2[i] + part3 + str(j) + part5
			except IndexError:
				print(i)

			infile = urllib.urlopen(url)
			lines = infile.readlines()   
			infile.close()
			# for i in range(calculusIII):
			regex = '<td><span class="a nameDetails">(.+)</span></td>'
				# if('<tr>' in lines[i - 1]):
			m = re.search(regex, lines[i])
			if(m):
				if(not ' ' in m.group(1)):
					print(m.group(1))
					f.write(m.group(1) + '\n') 
	f.close()
exit()
