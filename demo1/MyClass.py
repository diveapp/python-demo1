class Person:
    """
    一个简单的类
    """
    name = "F.Lee"

    age = 0

    __secret = "I`m not man"

    def working(self):
        print("I`m {}".format(self.name))


class Worker(Person):

    def __init__(self, name):
        self.name = name

    def working(self):
        print("{} is working!".format(self.name))


mc = Worker('二狗子')

print(mc.name*2)
super(Worker, mc).working()
