class girl:
    def __init__(self,name,attractiveness,maintainance_budget,intelligence_level,_type):
        self.name = name
        self.attractiveness = attractiveness
        self.maintainance_budget = maintainance_budget
        self.intelligence_level = intelligence_level
        self.status = 'single'
        self._type = _type
        self.boyfriend = ''
        self.happiness = 0
    def eligibility(self,budget):
        if self.maintainance_budget <= budget:
            return True
        else:
            return False
    def modify_maitainance_budget(self,budget):
        self.maintainance_budget = budget
    def set_boyfriend(self,boyfriend):
        self.boyfriend = boyfriend
    def set_happiness(self,happiness):
        self.happiness = happiness
        
