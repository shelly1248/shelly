class Money:
    card = 0
    def upMoney(self, value):
        self.card += value

        print(f'{self.card}')

class only(Money):
    def upMoney(self, value):
        self.card += value

        if self.card>150:
            self.card = 150

            print(f'{self.card}')

class hloy(Money):
    pass

money1 = hloy()
money2 = only()

print('money1 = ', end="")
money1.upMoney(200)

print('money2 = ', end="")
money2.upMoney(200)
    