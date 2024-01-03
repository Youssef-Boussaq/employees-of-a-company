from Salarie import Sta
class Vendeur(Sta):
    def __init__(self,nom,ssc,ec,adress,b_s,comise ,supervisor):
        super().__init__(nom,ssc,ec,adress,b_s,supervisor)
        self.__comise=comise
    


    @property
    def getcomise(self):
        return self.__comise


    #stter of comise attri
    def setcomise(self,new):
        self.__comise=new

    def salire(self):
        return self.getb_s + self.__comise


    def __str__(self):
        return super().__str__()+f"\nbase salarié;{self.getb_s} \ncomistion;{self.__comise} \nsupervisor; {self.supervisor}"
    

    
    def __eq__(self, other):
        if type(self)==type(other):
            return  self.salire()== other.salire() #and self.getmatrucul==other.getmatrucul
        else:
            return 'is not the same type'
