class Dog:
	def __init__(self, name):
		self.name = name
		print(name)

	def add_one(self,x):
		return x +1

	def bark(self):
		print("Bark")

d = Dog("Tim")
d.bark()
print(d.add_one(4))
print(d.name)