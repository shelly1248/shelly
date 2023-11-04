class test:
    bar = 0

    def bartest(self, value):
        self.test = self.test + value

    def bardown(self, value):
        self.down = self.down - value

class Jin(test):
    Num = 0

    def getNum(self):
        return self.Num
    
class hibar(test):
    conan = 0

    def getconan(self):
        return self.conan
    
Jin1, hibar1 = None, None

Jin1 = Jin()
hibar1 = hibar()

Jin1.bartest = 10
hibar1.bardown = 20

Jin1.Num = 1000
hibar1.Num = 5000

print(f'Jin bartest는 {Jin1.bartest} , Jin1.Num은 {Jin1.Num}')
print(f'hibar1.bardown 은 {hibar1.bardown} , hibar1.Num은 {hibar1.Num}')