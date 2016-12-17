from stopwords import stopwords

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
