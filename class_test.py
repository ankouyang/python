class Coffee:
    # __xxxx__魔术方法
    # __init__ 初始化方法
    def __init__(self, water, milk, sugar, coffee):
        self.water = water
        self.milk = milk
        self.sugar = sugar
        self.coffee = coffee
        self.prescription = [self.water, self.milk, self.sugar, self.coffee]

    def showPrecription(self):
        for i in self.prescription:
            print(i)


ice = Coffee(water=150, milk=200, sugar=50, coffee=100)
ice.showPrecription()
