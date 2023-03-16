from time import sleep

from hero import Hero

knight = Hero('Ричард', 50, 25, 20, 'меч')
rascal = Hero('Питер', 20, 5, 5, 'нож')
dragon = Hero('Дракон', 100, 25, 10, 'пламя')

knight.print_info()
rascal.print_info()
sleep(5)
knight.fight(rascal)





