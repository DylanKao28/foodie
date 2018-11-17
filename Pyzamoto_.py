from pyzomato import Pyzomato

import json

from urllib import request

p = Pyzomato("0037bd86fc45f5201beebaa204099f72")
G = p.getCityDetails(q = "Orange County")   #orange county ID = 484
#print(x)
#print(city_id)
#print(p.getCategories())
y = p.getEstablishments(484)
#print(y)
x= p.getCuisines(484)
#print(x)

z= p.getCollectionsViaCityId(484)
print(z)





