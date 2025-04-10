class character:

    name = None
    health = 100
    mp = 100

    def __init__(self, name):
        self.name = name

    def setStat(self, health, mp):
        self.health = health
        self.mp = mp

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}")

class player(character):

    nickname = None
    lives = 3

    def __init__(self, nickname):
        self.name = "Player"
        self.nickname = nickname

    def isAlive(self):
        if self.lives >= 1:
            print(f"{self.nickname} lives on!")
            return True
        else:
            print(f"{self.nickname} has expired.")
            return False

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")

ian = player("Ian the Mighty")
ian.print()
print(ian.isAlive())

class enemy(character):

    type = None
    strength = None

    def __init__(self, name, type, strength):
        self.name = name
        self.type = type
        self.strength = strength

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")

class orc(enemy):

    speed = None

    def __init__(self, speed):
        self.name = "Orc"
        self.type = "Orc"
        self.strength = 200
        self.speed = speed

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength {self.strength}\tSpeed: {self.speed}")

sharron = orc(250)
sharron.print()
garry = orc(205)
garry.print()

class vampire(enemy):

    day = True

    def __init__(self, day):
        self.name = "Vampire"
        self.type = "Vampire"
        self.strength = 150
        self.day = day

    def print(self):
        print(f"{self.name}\tHP: {self.health}\tMP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}")

eric = vampire(False)
eric.print()