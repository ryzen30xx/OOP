# color
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

class Warrior:
    def __init__(self, name, health, strength):
        self.name = name;
        self.health = health;
        self.strength = strength;

    def show_info(self):
        print(f"{GREEN}Name: {self.name}, Health: {self.health}, Strength: {self.strength}{END}");

    def got_hit(self, damage):
        print(f"{PURPLE}{self.name} got hit by {damage} damage.{END}");
        self.health -= damage
        if self.health < 0:
            self.health = 0
            print(f"{RED}{self.name} died!{END}");
        print(f"{YELLOW}{self.name}'s health is now {self.health}{END}");


warrior1 = Warrior("Krixi", 100, 20);
warrior2 = Warrior("Violet", 100, 25);

warrior1.show_info();
warrior2.show_info();

warrior1.got_hit(int(input(f"Enter damage to attack: ")));
warrior1.show_info();
warrior2.got_hit(int(input(f"Enter damage to attack: ")));
warrior2.show_info();
