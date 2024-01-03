from Salarie import Sta
from patron import Patron
from vendeur import Vendeur
from caisiere import caisiere



# Création d'un objet Patron
patron = Patron("Patron1", "123-45-6789", "Marié", "123 Rue Principale", 100000, 10000)

# Création d'un objet Vendeur avec le patron comme supérieur
vend = Vendeur("Vendeur1", "987-65-4321", "Célibataire", "456 Rue Elm", 50000, 5000,patron.getnom)

# Création d'un objet Caissier avec le patron comme supérieur
caissier = caisiere("Caissier1", "456-78-9123", "Divorcé", "789 Rue Pine", 30000, patron.getnom)

# Affichage des informations de chaque employé
print(patron)
print("#"*50)
print(vend)
print("#"*50)
print(caissier)
