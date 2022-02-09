import City
import Point
import csv
import Rectangle
import matplotlib.pyplot as plt

print("Welcome Lab 6, Exercise 2")



paht="C:\\Users\\user\\Documents\\Msc\\Introduction Programming\\Task6\\Ex1\\"
# open the CSV file
#Reading file
cities=[]
with open(paht+"data.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)
    for lines in csvFile:
        if lines[0]=="name":
            continue
        cities.append(City.City(lines[0], Point.Point(float(lines[1].split()[1]), float(lines[1].split()[0])), float(lines[2]), int(lines[3]), float(lines[4]), float(lines[5]), int(lines[6])  ))

#a Bounding box
longs=[]
lats=[]
for cty in cities:
    longs.append(cty.getLocation().getX())
    lats.append(cty.getLocation().getY())

bbox = Rectangle.Rectangle(Point.Point(min(longs), max(lats)), max(longs)-min(longs), max(lats)-min(lats)  )


##B scale definition
scale = 900/max(bbox.getHeight(), bbox.getWidth())

##C scale method
citiesB=cities
for cty in range(len(citiesB)):
    citiesB[cty].setLocation( Point.Point( cities[cty].getLocation().getX()*scale,  cities[cty].getLocation().getY()*scale)    )

##D centroid
bbb_cenx = bbox.centroid().getX()
bbb_ceny = bbox.centroid().getY()

##E Finding the right trasnlation
xTranslation = 500 - bbox.centroid().getX()*scale
yTranslation = 500 - bbox.centroid().getY()*scale

##F Translated objects
x_translated=[]
y_translated=[]
for city in citiesB:
    x_translated.append(city.getLocation().getX() + xTranslation)
    y_translated.append(city.getLocation().getY() + yTranslation)
##G City plottin
for i in range(len(citiesB)):
  plt.plot(x_translated[i], y_translated[i], marker='x', color = "black")
  plt.text(x_translated[i], y_translated[i], citiesB[i].name)

