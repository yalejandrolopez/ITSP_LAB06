import City
import Point
import csv

print("Welcome Lab 6, Exercise 1")



paht="C:\\Users\\user\\Documents\\Msc\\Introduction Programming\\Task6\\Ex1\\"
# open the CSV file
lines_csv=[]
#part b
with open(paht+"data.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)

    # display the contents of the CSV file
    for lines in csvFile:
        lines_csv.append(lines)
        print(lines)
#part C
for i in range(1,4):
    print(lines_csv[i])

#Part e
cities=[]
with open(paht+"data.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)
    for lines in csvFile:
        if lines[0]=="name":
            continue
        cities.append(City.City(lines[0], Point.Point(float(lines[1].split()[0]), float(lines[1].split()[1])), float(lines[2]), int(lines[3]), float(lines[4]), float(lines[5]), int(lines[6])  ))

for cty in cities:
    print("------------")
    print("Name:", cty.getName() )
    print("Location: Long: {} Lat: {}".format(cty.getLocation().getX(), cty.getLocation().getY()))
    print("Area: ", cty.getArea() )
    print("Population: ", cty.getPopulation())
    print("Population Density: ", cty.getPop_den())
    print("GDP: ", cty.getGdp())
    print("Vaccinated: ", cty.getVacc())