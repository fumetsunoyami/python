from datetime import datetime
class SinhVien:
    truong = "Đại học đà lạt"
    def __init__(self, maSo: int, hoten: str, ngaySinh: datetime ) -> None: 
        self._maSo = maSo
        self.hoten = hoten
        self._ngaySinh = ngaySinh
    @property
    def maSo(self):
        return self._maSo   
    def hoten(self):
        return self.hoten       
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLen(maso):
            self._maSo = maso
    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7
    @classmethod
    def doitenTruong(self, tenmoi):
        self.truong = tenmoi
    def __str__(self) -> str:
        return f'{self._maSo}\t{self.hoten}\t{self._ngaySinh.strftime("%d-%m-%Y")}'
    def xuat(self):
        print(f"{self._maSo}\t{self.hoten}\t{self._ngaySinh.strftime('%d-%m-%Y')}")
    
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []
    def themsv(self, sv: SinhVien): 
        self.dssv.append(sv)
    def Xuat(self):
        for sv in self.dssv:
            print(sv)
    def timsvtheomssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    def timVt(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:   
                return i
        return -1
    def xoa(self, mssv: int): 
        vt = self.timVt(mssv)
        if vt != -1:
            del self.dssv[vt]
            return True
        else: return False
    
    def timsvTheoten(self, ten: str):
        return [sv for sv in self.dssv if ten in sv.hoten]
    
    def timsvsinhtruocngay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaysinh < ngay]
    
sv1 = SinhVien(1234567, 'nguyễn việt linh', datetime(2003, 9, 18))
sv2 = SinhVien(1244567, 'nguyễn thọ thành', datetime(2003, 9, 17))




dssv = DanhSachSv()
dssv.themsv(sv1)
dssv.themsv(sv2)

ten = str(input('nhap: '))

kq = dssv.timsvTheoten(ten)
for sv in kq:
    sv.xuat()

print(sv1)


     
            
    
        
       
       
    
    
    
        