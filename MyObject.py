class Animal:
    _name = ""
    _height = 0
    _weight = 0
    _sound = ""

    def __init__(self, name, height, weight, sound):
        self._name = name
        self._height = height
        self._weight = weight
        self._sound = sound

    def get_sound(self):
        return self._sound

    def set_sound(self, sound):
        self._sound = sound

    def toString(self):
        return "{} is {} cm tall {} kg heavy and speaks {}\n".format(self._name, self._height, self._weight,
                                                                     self._sound)


class Dog(Animal):
    _owner = ""

    def __init__(self, name, height, weight, sound, owner):
        super(Dog, self).__init__(name, height, weight, sound)
        self._owner = owner

    def toString(self):
        return "{} is {} cm tall {} kg heavy and speaks {} and owned by {} \n".format(self._name, self._height, self._weight, self._sound, self._owner )

    def multiple_sounds(self,how_many = None):
        if how_many == None:
            print(self._sound)
        else :
            print(self._sound * how_many)




# Main Procedure
cat = Animal("Whiskers", 10, 5, "meow")
print(cat.toString())

dog1 = Dog("Spike", 20, 10, "Ruff", "Mike")
print(dog1.toString())
dog1.multiple_sounds(5)
