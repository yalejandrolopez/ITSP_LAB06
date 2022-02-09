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
  plt.plot(x_translated_eu[i], y_translated_eu[i], marker='x', color = "black")
