class Car:
    def __init__(self):
        self.fell = 10
        self.efficiency = 40

    def drive(self,distance):
        carfell = distance / self.efficiency
        if self.fell < carfell:
            factdistance = self.fell * self.efficiency
            self.fell = 0
            return factdistance
        else:
            factdistance = carfell * self.efficiency
            self.fell = self.fell - carfell
            return factdistance
        
if __name__ == '__main__':
    test = Car()
    print(test.drive(500))
    print(test.drive(100))
            
    
