# ITSP_LAB06
Python script solution for lab 06 of the course introduction to software programming, Msc Geoinformatics and spatial datascience.


# ITSP_LAB06

These scripts contains the solution of the lab 6 of the class of introduction of software programming.
They used two files

-data.csv, which a text file format that contains information of cities in europe, with the columns as follows:<br />
```plain

- name: (string) name of the city
- lat long (string), contains coordinates decimal degrees in WGS86 of every city, with a blanck space separator in between
- area (float), area in square kilometers
- population (int), number of inhabitants
- population_density (float), population density of the city, (inhabitants / area)
- GRP (float): Gross domestic product, given in billions of EU
- vaccinated (int): number of inhabitants with full vaccionation with covid 19, (https://support.google.com/websearch/answer/9814707?p=cvd19_statistics&hl=es-419&visit_id=637800463070597691-1199711788&rd=1), it was calculated from the national average rate by the inhabitants of every city.
  
```

```plain

- London: https://en.wikipedia.org/wiki/London
- Madrid: https://en.wikipedia.org/wiki/Madrid
- Paris: https://en.wikipedia.org/wiki/Paris
- Vienna: https://en.wikipedia.org/wiki/Vienna
- Berlin: https://en.wikipedia.org/wiki/Berlin
- Zürich: https://en.wikipedia.org/wiki/Z%C3%BCrich
- Athens: https://en.wikipedia.org/wiki/Athens
- Prague: https://en.wikipedia.org/wiki/Prague
- Copenhagen: https://en.wikipedia.org/wiki/Copenhagen
- Rome: https://en.wikipedia.org/wiki/Rome
  
```



<br />
-europe.geojson, contains the polyline of the costline of europe, with its coordinates in degrees WGS84. File provided by the proffesor of the course.

