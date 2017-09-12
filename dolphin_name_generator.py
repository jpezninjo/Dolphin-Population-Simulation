from string import ascii_lowercase
from random import sample
import re
import urllib2

'''
opens multiple reqests to the prokerala website, parses retrieved html 
for names, and saves the data to a file named {sex}_names.dat
'''
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

'''
generator for male names
'''
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

'''
generator for female names
'''
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


# <!---usage-->
# get_names("boy")
# get_names("girl")