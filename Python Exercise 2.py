class ClubMembers:
	def __init__(self, name, birthday, age, favorite_food, goal):
		self.name = name
		self.birthday = birthday
		self.age = age
		self.favorite_food = favorite_food
		self.goal = goal

	def display_info(self):
		print("Name: " + self.name)
		print("Birthday: " + self.birthday)
		print("Age: " + self.age)
		print("Favorite Food: " + self.favorite_food)
		print("Goal: " + self.goal)


class ClubOfficers(ClubMembers):
	def __init__(self, name, birthday, age, favorite_food, goal, position):
		self.name = name
		self.birthday = birthday
		self.age = age
		self.favorite_food = favorite_food
		self.goal = goal
		self.position = position

	def display_officer_info(self):
		print("Name: " + self.name)
		print("Birthday: " + self.birthday)
		print("Age: " + self.age)
		print("Favorite Food: " + self.favorite_food)
		print("Goal: " + self.goal)
		print("Position: " + self.position)

m_1 = ClubMembers("Tom", "January 16", "14", "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", "16", "Beef stroganoff", "To be the world's greatest chef", "Treasurer")

ClubMembers.display_info(m_1)
ClubOfficers.display_officer_info(o_4)