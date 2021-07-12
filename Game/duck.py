class Wing(object):
    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("wee I'm flying.")
        elif self.ratio == 1:
            print("It's hard work but I'm flying.")
        else:
            print("I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)  # Composition

    def walk(self):
        print("Waddle, waddle , waddle")

    def swim(self):
        print("come on it! water is lovely.")

    def quack(self):
        print("quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("waddle waddle, I waddle too.")

    def swim(self):
        print("Come on in but water is a bit chilly this far south.")

    def quack(self):
        print("Are you 'avin' a alrf? I'm a penguin.")

    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)

        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("cannot add duck,are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing migrate block exception handling")  # TODO remove this before release
            except AttributeError as e:
                print("One duck down")
                problem = e
        if problem:
            raise problem  # We raised the problem once all the birds off the ground


if __name__ == "__main__":
    donald = Duck()
    donald.fly()