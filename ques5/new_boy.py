class boy:
    def __init__(self,name,attractiveness,intelligence,min_attraction_requirement,budget,_type):
        self.name = name
        self.attractiveness = attractiveness
        self.intelligence = intelligence
        self.min_attraction_requirement = min_attraction_requirement
        self.budget = budget
        self.status = 'single'
        self.happiness = 0
        self.girlfriend = ''
        self._type = _type
    def set_happiness(self,happiness):
        self.happiness = happiness
    def set_girlfriend(self,girlfriend):
        self.grilfriend = grilfriend
    def modify_boys_girl_budget(self,budget):
        self.boys_girl_budget = budget
    def eligibility(self,girls_maintainance_cost,girls_attractiveness):
        if self.budget > girls_maintainance_cost and self.min_attraction_requirement >= girls_attractiveness:
            return True
        else:
            return False
        
