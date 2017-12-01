class moduleA(object):
	"""
	moduleA is Nick's class
	this code is just to grab what I need from Nick
	"""
	def __init__(self):
		self.username = "mam-venda@hotmail.com"


class moduleB(moduleA):
	"""
	This is the class to return to Michael
	Contains the username from Nick and a filename of the file that lists out this user's pwned passwords
	"""
	def __init__(self, moduleA):
		self.username = moduleA.username
		self.filename = "passwords_list.txt"
		self.dicts = {}

	def create_dictionary(self):
		"""
		key is username
		value is a list of passwords for that username, retrieved from input file
		ex: {"email@email", ["qwerty", "12345"]}
		important: make sure the input file is on local disk
		"""
		with open("password_dumps.txt", "r") as file:
			for line in file.readlines():
				if line.strip():	# check empty lines
					info = line.split(":")
					value = [info[1].strip()]
					if info[0] not in self.dicts:
						self.dicts[info[0]] = value
					else:
						self.dicts[info[0]].append(info[1].strip())

	def write_file(self, moduleA):
		"""
		writes the passwords of the username one line at a time
		"""
		with open(self.filename, "a") as file:
			if moduleA.username in self.dicts:
				for v in self.dicts[moduleA.username]:
					file.write(v + "\n")

	def print_file(self):
		with open(self.filename, "r") as file:
			print()

def main():
	class1 = moduleA()
	class2 = moduleB(class1)
	class2.create_dictionary()
	class2.write_file(class1)

if __name__ == '__main__':
	main()