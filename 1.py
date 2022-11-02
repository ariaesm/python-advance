'''number = input('Enter Your number: ')

def func(number):
    print(number[::-1])
    
    
func(number)
#######################################################
number = input('Enter Your number: ')

class Reverse():
    def __init__(self,password):
        self.password = password 
    def my_func(self):
        print(number[::-1])
    
obj1 = Reverse(number)
obj1.my_func()
#######################################################

1. tejari , khadamati , maskuni
2. tedad khabe 
3. jonobi , shomali
4. sale sakhat
5. metrage 
6. address 
7. floors 


class BuySell():
    def __init__(self,type,since):
        self.type = type 
        self.since = since 
        
    def show_massage(self):
        print(f'your area type is {self.type} since {self.since}')
        

o1 = BuySell("maskuni",'2020')
o1.show_massage()


class Animal:
    def walk(self):
      print(f'{self.__class__.__name__}: walking...')
    def breathe(self):
      print(f'{self.__class__.__name__}: breathing...')
class Sparrow(Animal):
    def fly(self):
      print(f'{self.__class__.__name__}: flying...')
class Dog(Animal):
    def run(self):
      print(f'{self.__class__.__name__}: running...')


sparrow = Sparrow()
dog = Dog()

sparrow.walk()
sparrow.breathe()
sparrow.fly()

dog.walk()
dog.breathe()
dog.run()



class human():
    def say_hello(self):
        print('Hello from human!')

    def walk(self):
        print("human is walking!")

    def ability(self):
        print('ability from human!')
        
class doctor(human):
    def job(self):
        print('my job is dohtor!')
    def ability(self):
        super().ability()        

class programmer(human):
    def job(self):
        print('my job is programmer!')
    def ability(self):
        super().ability()


h = human()
d = doctor()
p = programmer()



d.job()
p.job()

class shasibolan():
    def func1 (self):
        print("this is from shasdi boland")
    
class savari():
    def func2 (self):
        print("this is from savari")
        
class nimshasi(shasibolan,savari):
    def func3(self):
        print("this is from nimshasi")
        
    
o1 = nimshasi()
o1.func1()
o1.func2()
o1.func3()

'''

class Birds():
    def flying(self):
        print('birds can flying!')
    
    def walking(self):
        print('birds can walking!')
        
    def mammal(self):
        print('some birds are mammal!')
        
class Chicken(Birds):
    def ovipossion(self):
        print('chicken is ovipossion!')
    def mammal(self):
        print('chicken isnt a mammal!')
        
class eagle(Birds):
    def hunting(self):
        print('eagle is a hunter!')
        

o1 = Chicken()
o1.mammal()