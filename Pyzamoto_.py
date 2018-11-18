from pyzomato import Pyzomato

import json

from urllib import request

p = Pyzomato("0037bd86fc45f5201beebaa204099f72")

er = p.getLocationDetails(484, "city")

final = []
for k in er["best_rated_restaurant"]:
    for k2 in k:
        if "American" in k[k2]["cuisines"] and "Latin American" not in k[k2]["cuisines"]:
            d = {}
            d["name"] = k[k2]["name"]
            d["address"] = k[k2]["location"]["address"]
            d["cuisines"] = k[k2]["cuisines"]
            d["rating"] = k[k2]["user_rating"]["aggregate_rating"]
            d["votes"] = k[k2]["user_rating"]["votes"]
            d["photo_url"] = k[k2]["photos_url"]
            d["menu_url"] = k[k2]["menu_url"]
            final.append(d)



final = sorted(final, key=lambda k: k["rating"], reverse = True)
for x in final:
    print(x)





