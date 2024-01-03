from abc import ABC, abstractmethod
class Sta(ABC):
    _count=0
    def __init__(self,nom,ssc,ec,adress,b_s=0,supervisor=None):
        self.__nom = nom
        self.__ssc = ssc
        self.__ec =ec
        self.__adress = adress
        self.__b_s= b_s
        Sta._count+=1
        self.__matricule=Sta._count
        self.supervisor = supervisor  # Ajout du supérieur hiérarchique
    



    @property
    def getnom(self):
        return self.__nom
    

    @property
    def getssc(self):
        return self.__ssc
    

    
    @property
    def getec(self):
        return self.__ec
    


    @property
    def getadress(self):
        return self.__adress
    
    @property
    def getb_s(self):
        return self.__b_s
    

    @property
    def getmatrucul(self):
        return self.__matricule

#setter 
    def setmatrucul(self,new):
        self.__matricule=new



#sterre of b_s
    def setb_s(self,new):
        self.__b_s=new


#settre of nom
    def setnom(self,new):
        self.__nom = new



#settre of ssc
    def setssc(self,new):
        self.__ssc = new

#settre of ec

    def setec(self,new):
        self.__ec = new

#settre of adress

    def setadress(self,new):
        self.__adress = new


# def of abstrait salire
    @ abstractmethod
    def salire(self):

        pass



#def of equal
    @ abstractmethod
    def __eq__(self,other):
        pass

                


#def of to string
    def __str__(self) :
        return f"nom;;{self.__nom} ; \nson numéro de sécurité sociale;;{self.__ssc}; \neatat civil;;{self.__ec}; \nadress;;{self.__adress}"

