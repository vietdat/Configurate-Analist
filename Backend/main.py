from stopwords import stopwords
from tkinter import *
from gui import *
def count(original_text, save_text):
	with open(original_text, 'r') as f:
		f_content = f.read().split()
		freq = [f_content.count(w) for w in f_content]
		word_dict = {}
		for i in range(len(f_content)):
			if f_content[i] not in word_dict and f_content[i] not in stopwords:
				word_dict[f_content[i]] = freq[i]
		# print (word_dict)
		# print(freq)


	with open(save_text, 'w') as w:
		for i in word_dict:
			w.write(i + ": " + str(word_dict[i]) + '\n')

def filter_content(s):
	return

def update_dictionary(cat):
	name = cat.name + '_dictionary.txt'
	with open(name, 'a+') as d:
		content = d.read().split()
		for i in cat.key:
			if i not in content:
				d.write(i + '\n')

def reset_dictionary(cat):
	name = cat.name + '_dictionary.txt'


def make_category(read_file):
	with open(read_file, 'r') as f:
		f_content = f.readlines()
		for i in f_content:
			if (not any([elem.contain(i) for elem in main_cate])):
				gui(i)

class Category:
	content = []
	key = []
	def __init__(self, name, contents = [], keys = []):
		self.name = name
		self.content = contents
		self.key = keys

	def update_dict(self):
		name = cat.name + '_dictionary.txt'
		with open(name, 'a+') as d:
			content = d.read()
			for i in cat.key:
				if i not in content:
					d.write(i + '\n')


	def get_name(self):
		return self.name

	def add_content(self, s):
		if (not self.content):
			self.content = [s]
		elif s not in self.content:
			self.content.append(s)
		

	def gui_content(self, s, root):
		if (not self.content):
			self.content = [s]
		elif s not in self.content:
			self.content.append(s)
		contents = s.split()
		key_words = [word for word in contents if word not in stopwords]
		cate_button = Label(root, text = 'Categories:')
		cate_button.pack(side= TOP)
		for i in key_words:
			b = Button(root, text = i)
			b.configure(command = lambda k=i: self.add_key(k))
			b.pack(side = LEFT)
		Button(root, text = 'Next', command = root.quit).pack(side=BOTTOM)

	def add_key(self, key):
		if (not self.key):
			self.key = [key]
		elif key not in self.key:
			self.key.append(key)
		else:
			print ("'{0}' alrealy exists in {1}'s dicionary.".format(key, self.name))
		update_dictionary(self)

	def remove(self, s):
		if s not in self.content:
			return ("Cannot find '{0}' in '{1}' category".format(s, self.name))
		else:
			self.content.remove(s)

	def contain(self, s):
		return (s in self.content)


ou = Category('OU')
tuition = Category('Tuition')
expense = Category('Living Expense')
other = Category('Others')
main_cate = [ou, tuition, expense, other]

def print_categories():
	for i in range (len(main_cate)):
		print ('{0}. {1}'.format(i+1, main_cate[i].name))


def gui(s):
	root = Tk()
	l = Label(root, text = s)
	l.pack()
	for item in main_cate:
		b = Button(root, text = item.get_name())
		b.configure(command = lambda k=item: k.gui_content(s, root))
		b.pack(side = LEFT)
	# content = s.split()
	# key_words = [word for word in content if word not in stopwords]
	# cate_button = Button(root, text = 'Categories:')
	# cate_button.pack(side= TOP)
	# for i in key_words:
	# 	b = Button(root, text = i)
	# 	b.configure(command = lambda k=i: k.add_key(k))
		b.pack(side = LEFT)
	root.mainloop()

def cate(s):
	# nonlocal main_cate
	print ('')
	print (s)
	content = s.split()
	key_words = [word for word in content if word not in stopwords]
	result = 'Possible key words: ' 
	print (result)
	print (*key_words, sep = ', ')
	print ('Categories: ')
	print_categories()
	# for i in range(len(main_cate)):
	# 	print (str(i + 1) + '. ' + main_cate[i].name)
	choice = input('Which category do you think this one belongs to: ')
	main_cate[int(choice) - 1].add_content(s)
	if main_cate[int(choice) - 1].name == 'Others':
		ask = input('What category would you like to add? ')
		if ask not in [i.name for i in main_cate]:
			new_cate = Category(ask)
			main_cate.pop()
			main_cate.append(new_cate)
			main_cate.append(other)
		# else:
		# 	choice = 
	opt = 'non'
	while opt != 'y' and opt != 'n':
		opt = input('Would you like to add the key word to the dictionary [y/n]?')
	if opt == 'y':
		for i in range(len(key_words)):
			print (str(i + 1) + '. ' + key_words[i])
		pick_key = input("which key would you like to add? ")
		main_cate[int(choice) - 1].add_key(key_words[int(pick_key) - 1])


