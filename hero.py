from time import sleep


class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health  # число
        self.armor = armor  # число
        self.power = power  # число
        self.weapon = weapon  # строка

    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья:', self.health)
        # продолжите самостоятельно

    def strike(self, enemy):
        print(
            '-> УДАР! ' + self.name + ' атакует ' + enemy.name +
            ' с силой ' + str(self.power) + ', используя ' + self.weapon + '\n')

        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print(
            enemy.name + ' покачнулся(-ась).\nКласс брони упал до '
            + str(enemy.armor) + ', а уровень здоровья до '
            + str(enemy.health) + '\n')

    def fight(self, enemy):
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелегком бою!\n')
                if self.health > 0:
                    self.recovery()
                break
            sleep(5)

            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в этом нелегком бою!\n')
                break
        sleep(5)

    def recovery(self):
        self.health = 50
        self.power *= 2
        self.armor *= 2
        print(
            '\n' + self.name +
            ' восстановил силы и стал опытнее. Теперь сила его удара: ' + str(
                self.power) + ', а класс брони:' + str(self.armor) + '\n')
