class Person:
    #le mot clee self permet d'heriter (et utiliser) tous les attributs de l'instance
    #sinon on reste local dans la methode
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            initialAge = 0
        #on initialise une variable dinstances self.age appele attribut
        self.age = initialAge
        #on peut appeler dans le constructeur les autres methodes
        self.myAge()

    #une methode
    def amIOld(self):
        if self.age < 13: print("You are young.")
        elif self.age >= 13 and self.age < 18: print("You are a teenager.")
        else: print("You are old.")

    #une deuxieme methode
    def yearPasses(self):
        self.age += 1
    
    #une troisieme methode
    def myAge(self):
        print("Your age is "+str(self.age))

if __name__ == '__main__':
    age = int(input())
    pierre = Person(age)
    pierre.amIOld()
    pierre.yearPasses()

    #3 possibilites pour afficher lage:
    #on appele lattribut age (la variable seule)
    print(pierre.age)
    #on appelle a travers la methode (=une fonction dans une classe):
    pierre.myAge()
    #equivalent a travers la fonction (on passe en param lobjet):
    Person.myAge(pierre)
    del pierre