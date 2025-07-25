#when we print(any object) then python internally called __str__ method
# It basically gives the data type

class Fraction:

    def __init__(self, num, den):
        self.den = den
        self.num = num

    def __str__(self):
        return "{}/{}".format(self.num,self.den)
        return "fraction"
    
    def __add__(self,other):
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __sub__(self,other):
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __mul__(self,other):
        temp_num = self.num   * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __truediv__(self ,other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num,temp_den)
    