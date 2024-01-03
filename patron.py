from Salarie import Sta
class Patron(Sta):
    def __init__(self,nom,ssc,ec,adress,b_s,prim_ris):
        super().__init__(nom,ssc,ec,adress,b_s)
        self.__prim_ris=prim_ris
    


    @property
    def getprim_ris(self):
        return self.__prim_ris


    #stter of prim_ris attri
    def setprim_ris(self,new):
        self.__prim_ris=new

    def salire(self):
        return self.getb_s + self.__prim_ris


    def __str__(self):
        return super().__str__()+ f"\nbase salarié;; {self.getb_s} \nprime de risque ;{self.__prim_ris}"
    

    def __eq__(self, other):
        if type(self)==type(other):
            return  self.salire()== other.salire() and self.getmatrucul==other.getmatrucul
        else:
            return 'is not the same type'
