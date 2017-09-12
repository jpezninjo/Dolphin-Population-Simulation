import threading

class SummingThread(threading.Thread):
     def __init__(self, id):
         super(SummingThread, self).__init__()
         self.id = id
         self.dolphin_pool = []

     def run(self):
         countDolphins(self.id)

populations = []
num_threads = 5

num_trials = 15
years_per_trial = 150
report_frequency = 25
male_chance = 0.5

def countDolphins(id):
	print("Thread {} reporting for duty!".format(id))
	for i in range(num_trials / num_threads):
		string_builder = "Trial {}".format(i + id*(num_trials/num_threads))
		# for j in range(years_per_trial):
			# self.dolphin_pool = []
		print(string_builder)

thread_pool = []
for i in range(num_threads):
	thread_pool.append(SummingThread(i))
for thread in thread_pool:
	thread.start()
for thread in thread_pool:
	thread.join()

# for l in populations:
	# print(l)