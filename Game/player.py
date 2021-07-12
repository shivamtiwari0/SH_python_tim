class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives > 0:
            self._lives = lives
        else:
            print("Lives can't be negative.")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level >= 1:
            self._level = level
            self.score = (level-1) * 1000
        else:
            print("cant go below level 1")
            self._level = 1
            self.score = 0

    level = property(_get_level, _set_level)
    lives = property(_get_lives, _set_lives)  # Don't give same name to property as attribute.

    def __str__(self):  # Created this method to easily see the value of objects
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
