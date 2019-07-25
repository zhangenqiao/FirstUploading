from random import randint


class Die():
    def __int__(self, side_num):
        self.sides = side_num

    def roll_die(self):
        a = randint(1, self.sides)
        print("这次骰子的点数是：" + str(a))


a = Die(6)
a.roll_die