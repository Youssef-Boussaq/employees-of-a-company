from Salarie import Sta
class caisiere(Sta):
    def __init__(self,nom,ssc,ec,adress,b_s,supervisor):
        super().__init__(nom,ssc,ec,adress,b_s,supervisor)


    def salire(self):
        return self.getb_s


    def __str__(self):
        return super().__str__()+f"  \nthe salarié;;{self.salire()} \n supervisor ;; {self.supervisor}"
    

    
    def __eq__(self, other):
        if type(self)==type(other):
            return  self.salire()== other.salire() and self.getmatrucul==other.getmatrucul
        else:
            return 'is not the same type'
