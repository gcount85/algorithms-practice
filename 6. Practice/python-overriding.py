class Animal:
    def make_sound(self):
        print("The animal makes a sound")


class Dog(Animal): # Animal 클래스 상속
    def make_sound(self): # 메소드 오버라이딩
        print("The dog barks") 


class Cat(Animal): # Animal 클래스 상속
    def make_sound(self): # 메소드 오버라이딩
        print("The cat meows")


animal = Animal()
animal.make_sound()

cute_cat = Cat()
cute_cat.make_sound()

cute_dog = Dog()
cute_dog.make_sound()
