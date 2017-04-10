class couples:
	def __init__(self,girl,boy):
		self.girl = girl
		self.boy = boy
		self.compatibility = 0
		self.gifts = []
	def set_happiness(self):
		self.happiness = self.girl.happiness + self,boy.happiness
	def set_compatibility(self):
		self.compatibility = (self.boy.budget - self.girl.maintainance_budget) + abs(self.girl.attractiveness - self.boy.attractiveness)+ abs(self.girl.intelligence_level - self.boy.intelligence) 

