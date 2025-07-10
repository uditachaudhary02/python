class Robot:
    def eat(self):
        print('hungry')
class RobotDog:
    def eat(self):
        super().eat()
        print('i eat meat')
    my_robotdog = RobotDog('bub')
    my_robotdog.eat()