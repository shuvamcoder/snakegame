class Animal:
    def __int__(self):
        self.num_eyes = 2 #attribute

    def breathe(self): #method
        print("Inhale,Exhale")


class Fish(Animal):

    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()