#my first class

class Building:
    def __init__(self, w, h, l, adr):
        self.width = w
        self.height = h
        self.length = l
        self.address = adr

    def set_height(self,h):
        self.height = h

    def calc_volume(self):
        return (self.width*self.height/2*self.length)+(self.width*self.height/2*self.length)/2

def main():
    hus1 = Building(10,2,15,"Kungsgatan 2")
    print(f'hus1 har volymen: {hus1.calc_volume()} m3')

    #hus1 byggs om med en till våning
    hus1.set_height(4)
    print(f'hus1 har volymen: {hus1.calc_volume()} m3')

    hus2 = Building(10,2,15,"Drottnigngatan 1")
    hus2.set_height(18)  

if __name__ == '__main__':
    main()