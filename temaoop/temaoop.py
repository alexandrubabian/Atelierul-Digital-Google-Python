#ce este mai jos este prima parte
# class catalog:
#     def __init__(self,nume,prenume):
#         self.nume=nume
#         self.prenume=prenume
#         self.materii={}
#         self.absente=0
#
#     def __str__(self):
#         return f"{self.nume} {self.prenume} are {self.absente}"
#
#     def incrementare(self):
#         self.absente += 1
#
#     def motivare(self,numar):
#         if isinstance(numar,int) and numar>0:
#             self.absente=self.absente-numar
#         if self.absente < 0:
#             self.absente=0
#
# class Extensie1(catalog):
#     def note(self, materie : str, note : list):
#         self.materii[materie]=note
#
#     def materiile(self):
#         print("Elevul {} {} are urmatoarele materii:".format(self.nume, self.prenume))
#         for key, value in self.materii.items():
#             print(key)
#
#     def medie(self):
#         print("Elevul {} {} are mediile:".format(self.nume, self.prenume))
#         for key, value in self.materii.items():
#             print(key)
#             suma=0
#             for i in range(len(value)):
#                 if isinstance(value[i],int) and value[i] > 0:
#                     suma=suma+value[i]
#             print(suma)
#
# elev=Extensie1("Roata", "Ion")
# elev.incrementare()
# elev.incrementare()
# elev.incrementare()
# elev.motivare(2)
# elev.note("Python",[3, 5 ,9])
# elev.materiile()
# elev.medie()
# ce este mai jos este a doua parte a temei

from operator import attrgetter
class catalogprajituri:
    lista=[]
    def __init__(self, nume :str, pret:int, gramaj:int):
        self.nume=nume
        self.pret=pret
        self.gramaj=gramaj
        catalogprajituri.lista.append(self)

    def sortaregramaj(self):
        sortategramaj=sorted(catalogprajituri.lista,key=attrgetter('gramaj'))
        for i in sortategramaj:
            print(i.nume +"-{} lei -{} gramaj".format(i.pret,i.gramaj))

    def sortarepret(self):
        sortatepret = sorted(catalogprajituri.lista, key=attrgetter('pret'))
        for i in sortatepret:
            print(i.nume + "-{} lei -{} gramaj".format(i.pret, i.gramaj))

catalog=catalogprajituri("pancake",100,10)
catalog1=catalogprajituri("clatite",120,6)
catalog.sortaregramaj()
catalog.sortarepret()