from player import Player

tim = Player('Tim')

# print(tim.name)
# print(tim.lives)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
tim._lives = 9
print(tim)

# tim.level = 2
# print(tim)
#
# tim.level += 5
# print(tim)
#
# tim.level = 3
# print(tim)

from enemy import Enemy, Troll, Vampyre, VampyreKing
#
random_monster = Enemy('Basic Enemy', 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)
random_monster.take_damage(8)
print(random_monster)
random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll("Pug")
print("Ugly Troll- {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another Troll- {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

monster = Enemy("Basic Enemy")
# monster.grunt()  # AttributeError: 'Enemy' object has no attribute 'grunt

another_troll.take_damage(18)
print(another_troll)

print("-"*40)

vamp = Vampyre("Big Vampyre")
print(vamp)

vamp.take_damage(5)
print(vamp)

another_troll.take_damage(30)
print(another_troll)

while vamp._alive:
    vamp.take_damage(1)
    print(vamp)

vlad_the_king = VampyreKing("VladKing")
print(vlad_the_king)

vlad_the_king.take_damage(40)
print(vlad_the_king)