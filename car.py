class Car:
    def __init__(self):
        # 残燃料(リットル)
        self.fell = 10
        # 燃費(キロ/リットル)
        self.efficiency = 40

    def drive(self,distance):
        # 燃料の利用数
        carfell = distance / self.efficiency
        # 残燃料より、燃料の利用数が、多く利用された場合。
        # 走れる上限であり、全ての残燃料を使い果たす。
        if self.fell < carfell:
            factdistance = self.fell * self.efficiency
            self.fell = 0
            return factdistance
        # 残燃料より、燃料の利用数が、少なく利用された場合。
        else:
            factdistance = carfell * self.efficiency
            self.fell = self.fell - carfell
            return factdistance

# 距離を入れて実際に何キロまで走れるのか
# 連続使用した場合どうなるのか        
if __name__ == '__main__':
    test = Car()
    print(test.drive(500))
    print(test.drive(100))
            
    
