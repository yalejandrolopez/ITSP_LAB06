## PART A
import Point
#from Shape import Shape

class City():
    def __init__(self, name, location, area, population, pop_den, gdp, vacc ):
        self.name=name
        self.location=location
        self.area=round(area,2)
        self.population = int(population)
        self.pop_den = round(pop_den,2)
        self.gdp = round(gdp, 2)
        self.vacc = round(vacc, 2)

    def getName(self):
        return self.name

    def getLocation(self):
        return self.location

    def getPopulation(self):
        return self.population

    def getArea(self):
        return self.area

    def getPop_den(self):
        return self.pop_den

    def getGdp(self):
        return self.gdp

    def getVacc(self):
        return self.vacc

    def setLocation(self, point):
        self.location=point

    def setName(self, name):
        self.name=name

    def setPopulation(self, population):
        self.population = int(population)

    def setArea(self, area):
        self.area = area

    def setPop_den(self, pop_den):
        self.pop_den = pop_den

    def setGdp(self, gpd):
        self.gpd = gpd

    def setVacc(self, vacc):
        self.vacc = vacc