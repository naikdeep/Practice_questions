class Animal:
    def __init__(self,type):
        self.type=type

class dog(Animal):
    def __init__(self,breed):
        self.breed=breed
        self.type=Animal.type

obj_animal=Animal("")

