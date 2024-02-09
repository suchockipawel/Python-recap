class Animal:
    def make_sound(self):
        print('Some animal sound')
        
class Duck(Animal):
    def make_sound(self):
        print('Quack')
        
class Cat(Animal):
    def make_sound(self):
        print("Meow")

duck = Duck()
duck.make_sound()
cat = Cat()
cat.make_sound()