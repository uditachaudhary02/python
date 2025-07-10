class Robot:
    def __init__(self,name):
        self.name=name
        self.position=[0,0]
        print('name',self.name)

    def walk(self,x):
        self.position[0]=self.position[0]+ x
        print('new ',self.position)

class RobotDog(Robot):
    def make_noise(self):
        print('woof')

my_RobotDog=RobotDog('bud')
my_RobotDog.walk(10)
my_RobotDog.make_noise() 