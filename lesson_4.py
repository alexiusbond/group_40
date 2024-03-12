from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    HEAL = 1
    CRITICAL_DAMAGE = 2
    BOOST = 3
    BLOCK_DAMAGE_REVERT = 4


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__damage = damage
        self.__health = health

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return (f'{self.__name} health: {self.__health} '
                f'damage: {self.__damage}')


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        # self.__defence = choice([e.value for e in SuperAbility])
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if (hero.ability == SuperAbility.BLOCK_DAMAGE_REVERT and
                        self.defence != SuperAbility.BLOCK_DAMAGE_REVERT):
                    coef = randint(1, 2)
                    hero.blocked_damage = int(self.damage / (coef * 5))
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return (f'BOSS ' + super().__str__()
                + f' defence: {self.__defence}')


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coef = randint(2,5)
        boss.health -= self.damage * coef
        print(f'Warrior {self.name} '
              f'hit critically {self.damage * coef}')




class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        pass


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.BLOCK_DAMAGE_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage,
                         SuperAbility.HEAL)
        self.__heal_points = heal_points

    @property
    def heal_points(self):
        return self.__heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


round_number = 0


def start_game():
    boss = Boss('Tanos', 1000, 50)

    warrior_1 = Warrior('Ahiles', 280, 5)
    warrior_2 = Warrior('Sponge Bob', 270, 10)
    magic = Magic('Hendolf', 180, 20)
    berserk = Berserk('Gatz', 220, 20)
    doc = Medic('Haus', 250, 5, 15)
    junior = Medic('Zolo', 290, 5, 5)

    heroes_list = [warrior_1, warrior_2, magic, berserk, doc, junior]
    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def show_statistics(boss, heroes):
    print(f'ROUND: {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if (hero.health > 0 and boss.health > 0 and
                hero.ability != boss.defence):
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


start_game()
