import City
import Point
import csv
import Rectangle
import json
import matplotlib.pyplot as plt
import Polyline

print("Welcome Lab 6, Exercise 3")

path="C:\\Users\\user\\Documents\\Msc\\Introduction Programming\\Task6\\"
cost_line = []
with open(path+"europe.geojson", mode = 'r') as file:
    gjFile = json.load(file)
    for entry in gjFile['features']:
        polyline = entry['geometry']['coordinates']
        for i in range(len(polyline)):
            cost_line.append(Point.Point(polyline[i][0], polyline[i][1]))

longs_eu=[]
lats_eu=[]
for p in cost_line:
    longs_eu.append(p.getX())
    lats_eu.append(p.getY())

bbox_eu = Rectangle.Rectangle(Point.Point(min(longs_eu), max(lats_eu)), max(longs_eu)-min(longs_eu), max(lats_eu)-min(lats_eu)  )
##B
scale_eu = 900/max(bbox_eu.getHeight(), bbox_eu.getWidth())
cost_line_p=cost_line
for p in range(len(cost_line)):
    cost_line_p[p].setPosition( longs_eu[p]*scale_eu,  lats_eu[p]*scale_eu )

ex = []
for p in range(len(cost_line)):
    #print(cost_line_p[p].getX())
    ex.append(cost_line_p[p].getY())

##D
bbox_eu_cenx = bbox_eu.centroid().getX()
bbox_eu_ceny = bbox_eu.centroid().getY()

##E
xTranslation_eu = 500 - bbox_eu.centroid().getX()*scale_eu
yTranslation_eu = 500 - bbox_eu.centroid().getY()*scale_eu

##F
x_translated_eu=[]
y_translated_eu=[]
for p in cost_line_p:
    x_translated_eu.append(p.getX() + xTranslation_eu)
    y_translated_eu.append(p.getY() + yTranslation_eu)
##G
for i in range(len(cost_line_p)):
  plt.plot(x_translated_eu[i], y_translated_eu[i], marker='x', color = "black", markersize=5)


##
paht="C:\\Users\\user\\Documents\\Msc\\Introduction Programming\\Task6\\Ex1\\"
# open the CSV file
lines_csv=[]

#Part e
cities=[]
with open(paht+"data.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)
    for lines in csvFile:
        if lines[0]=="name":
            continue
        cities.append(City.City(lines[0], Point.Point(float(lines[1].split()[1]), float(lines[1].split()[0])), float(lines[2]), int(lines[3]), float(lines[4]), float(lines[5]), int(lines[6])  ))

##################
#longs=[]
#lats=[]
#for cty in cities:
#    longs.append(cty.getLocation().getX())
#    lats.append(cty.getLocation().getY())

#bbox = Rectangle.Rectangle(Point.Point(min(longs), max(lats)), max(longs)-min(longs), max(lats)-min(lats)  )

citiesB=cities

##C
for cty in range(len(citiesB)):
    citiesB[cty].setLocation( Point.Point( cities[cty].getLocation().getX()*scale_eu,  cities[cty].getLocation().getY()*scale_eu)    )

##D
#bbb_cenx = bbox.centroid().getX()
#bbb_ceny = bbox.centroid().getY()

##E
xTranslation = 500 - bbox_eu.centroid().getX()*scale_eu
yTranslation = 500 - bbox_eu.centroid().getY()*scale_eu

##F
x_translated=[]
y_translated=[]
for city in citiesB:
    x_translated.append(city.getLocation().getX() + xTranslation)
    y_translated.append(city.getLocation().getY() + yTranslation)
##G
for i in range(len(citiesB)):
  plt.plot(x_translated[i], y_translated[i], marker='x', color = "black")
  plt.text(x_translated[i], y_translated[i], citiesB[i].name)
for i in range(len(cost_line_p)):
  plt.plot(x_translated_eu[i], y_translated_eu[i], marker='x', color = "blue", markersize=3)
