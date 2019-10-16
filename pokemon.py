class Pokemon:
    attack_by_type = {
        "Fire": {"Fire": 1, "Water": 0.5, "Grass": 2},
        "Water": {"Fire": 2, "Water": 1, "Grass": 0.5},
        "Grass": {"Fire": 0.5, "Water": 2, "Grass": 1}
    }

    evolution = {
        0: "Infant",
        1: "Baby",
        2: "Toddler",
        3: "Child",
        4: "Adolescent",
        5: "Advanced Adolescent",
        6: "Adult",
        7: "Middle-Aged",
        8: "Senior",
        9: "Ancient",
        10: "Elder",
    }

    def __init__(self, name, level, ptype, avatar='default_pokemon.gif'):
        self.name = name
        self.level = level
        self.ptype = ptype
        self.avatar = avatar
        self.max_health = self.level * 10
        self.current_health = self.max_health
        self.knocked_out = False
        self.experience = 0
        self.evolution_stage = 1
        self.speed = 5
        self.attack_power = 3
        self.defense = 5

    def level_up(self, increase=1):
        self.level += increase
        self.max_health = self.level * 10
        #self.experience = 0
        print(f'{self.name} is now at level {self.level}, with maximum health {self.max_health}!')
        if self.level % 5 == 0:
            self.evolution_stage = self.level / 5
        print(f"Congratulations, {self.name} has evolved to {self.evolution[self.evolution_stage]}")

    def increase_health(self, increase):
        self.current_health += increase
        print(f"{self.name}\'s health increased to {self.current_health}")

    def decrease_health(self, decrease):
        self.current_health -= decrease
        print(f"{self.name}\'s health decreased to {self.current_health}")
        if self.current_health == 0:
            self.knock_out()

    def knock_out(self):
        if self.current_health == 0:
            self.knocked_out = True
            print(f"{self.name} is knocked out")

    def revive(self):
        self.knocked_out = False
        print(f"{self.name} has been revived")

    def attack(self, pokemon):
        if self.knocked_out:
            print(f"{self.name} is knocked out and cannot attack {pokemon.name}")
        elif pokemon.knocked_out:
            print(f"{pokemon.name} is already knocked out. Don't kick a Pokemon when they're down!")
        else:
            print(f"{self.name} is attacking {pokemon.name}")
            damage = self.level * self.attack_by_type[self.ptype][pokemon.ptype]
            #print(f"{self.name} is a {self.ptype} Pokemon, and {pokemon.name} is a {pokemon.ptype} Pokemon. {self.name} does {damage} points of damage to {pokemon.name}")
            print(f"{self.name} does {damage} points of damage to {pokemon.name}")
            pokemon.decrease_health(damage)
            self.experience += 1
            pokemon.experience += 1
            if self.experience == self.level * 10:
                self.level_up(1)
            if pokemon.experience == pokemon.level * 10:
                pokemon.level_up(1)

    def battle(self, opponent):
        for _ in range(3):
            if self.speed >= opponent.speed:
                self.attack(opponent)
                opponent.attack(self)
            else:
                opponent.attack(self)
                self.attack(opponent)


class Charmander(Pokemon):
    def __init__(self, name, level, ptype, avatar='default_pokemon.gif'):
        super().__init__(self, name, level, ptype, avatar='default_pokemon.gif')


class Trainer:
    def __init__(self, name, list_of_pokemon, potions=0, currently_active_pokemon=0):
        self.name = name
        if len(list_of_pokemon) <= 6:
            self.list_of_pokemon = list_of_pokemon
        else:
            print(f"{self.name} can have up to 6 Pokemon")
        self.potions = potions
        self.currently_active_pokemon = currently_active_pokemon

    def get_active_pokemon(self):
        return self.list_of_pokemon[self.currently_active_pokemon]

    def use_potion(self):
        self.potions -= 1
        current_pokemon = self.get_active_pokemon()
        current_pokemon.current_health = current_pokemon.max_health
        print(f"{current_pokemon.name} has been healed. Current health is {current_pokemon.health}")

    def switch_pokemon(self, new_pokemon):
        if self.list_of_pokemon[new_pokemon].knocked_out:
            print(f"{self.list_of_pokemon[new_pokemon].name} is knocked out. {self.name} can't switch to them")
        self.currently_active_pokemon = new_pokemon
        pokemon_name = self.list_of_pokemon[self.currently_active_pokemon].name
        print(f"{pokemon_name} is now the currently active Pokemon for {self.name}")

    def attack_trainer(self, trainer):
        current_pokemon = self.get_active_pokemon()
        opponent_pokemon = trainer.get_active_pokemon()
        print(f"{self.name}\'s Pokemon, {current_pokemon.name}, is attacking {trainer.name}\'s Pokemon, {opponent_pokemon.name}")
        current_pokemon.attack(opponent_pokemon)

aleph = Pokemon("Aleph", 1, "Fire")
bet = Pokemon("Bet", 2, "Water")
gimmel = Pokemon("Gimmel", 3, "Grass")
leo = Pokemon("Leo", 5, "Water")
henry = Pokemon("Henry", 6, "Grass")
angel = Pokemon("Angel", 5, "Grass")

Eliza = Trainer("Eliza", [aleph, bet, gimmel], 6, 2)
GR = Trainer("GR", [leo, henry, angel], 20, 1)

aleph.attack(leo)
henry.attack(gimmel)
leo.attack(gimmel)
bet.attack(leo)

Eliza.switch_pokemon(1)
GR.switch_pokemon(2)

print("Battle")
aleph.battle(leo)




