from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise ValueError("mau khac 0")
        self.tu = tu
        self.mau = mau
        self.rut_gon()
    def __init__(self, tu=0, mau=1):
        if mau == 0:
            raise ValueError("mau khac 0")
        self.tu = tu
        self.mau = mau
        self.rut_gon()
    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __str__(self):
        return f"{self.tu}/{self.mau}"
    def __add__(self, other):
        new_tu = self.tu * other.mau + self.mau * other.tu
        new_mau = self.mau * other.mau
        return PhanSo(new_tu, new_mau)
    def __sub__(self, other):
        new_tu = self.tu * other.mau - self.mau * other.tu
        new_mau = self.mau * other.mau
        return PhanSo(new_tu, new_mau)
    def __mul__(self, other):
        new_tu = self.tu * other.tu
        new_mau = self.mau * other.mau
        return PhanSo(new_tu, new_mau)
    def __truediv__(self, other):
        new_tu = self.tu * other.mau
        new_mau = self.mau * other.tu
        return PhanSo(new_tu, new_mau)

a = PhanSo(3,5)
b= PhanSo(7,3)
c = PhanSo()
c.mau = 1
c.tu = 2

print (f"{a} + {b} = {a + b }")
print (f"{a} - {b} = {a - b}")
print (f"{a} * {b} = {a * b}")
print (f"{a} / {b} = {a / b}")

        
    
            
        
        
        
        
       
        
        