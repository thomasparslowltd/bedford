# SEE README
FB_ACCESS_CODE = "CAAC2eZAjyRZBgBABxU1IvSTw3MHiaueXY7WXlEjSPGWwlb7HaNhdiyFpG9gu4gZB1hVZBzxTG5P2ExHZCJZBfrzZC1lyAVj4Six46AXsQY4CmGoPCTI5TB8U8KDtff2EHKHbHWTwnZBz3MqjumV0H2w6ZAAYAGkYlijMHtJayHEKK7F69NCdHcVjSXylsZCzbAX5IOeoPGeKpmRePP7ttcfAhG"

import requests, json, time

def fbget(path, **params):
    params = dict(params)
    params["access_token"] = FB_ACCESS_CODE
    return requests.get("https://graph.facebook.com" + path, params=params).json()

def lookupadgeolocation(q, type="city", country="GB"):
    data = fbget("/search", type="adgeolocation", q=q, location_types=json.dumps([type]), country_code=country)
    # print data
    assert isinstance(data["data"], list), "Data should be a list of places"
    assert len(data["data"]) != 0, "No locations found"
    assert len(data["data"]) == 1, "Location ambiguous, more than 1 result found"
    return data["data"][0]

def mobiledevices(q):
    return fbget("/search", type="adTargetingCategory",q=q, **{"class": "user_device"})

def getaddaccount():
    # Requesting user must have an ad account
    return fbget("/me/adaccounts")["data"][0]["id"]


def reachestimate(ad_account_id, targeting_spec):
    data = fbget("/%s/reachestimate" % (ad_account_id,), targeting_spec=json.dumps(targeting_spec))
    try:
        return data["users"]
    except:
        print data
        raise
    

def reach(city, age_min=None, age_max=None, gender="all", device_type="all"):
    ad_account_id = getaddaccount()
    location = lookupadgeolocation(city)
    gender = {"male": 1, "female": 2, "all": 0}[gender]
    page_types = {"mobile": ["mobile"], "desktop": ["desktop"], "all": None}[device_type]
    assert not age_min or age_min >= 13
    assert not age_max or age_max <= 65
    targeting_spec = {
        "genders": [gender],
        "geo_locations": {
            "cities": [{"key": location["key"], "radius": 0, "distance_unit": "mile"}]
        }
    }
    if page_types:
        targeting_spec["page_types"] = page_types
    if age_min:
        targeting_spec["age_min"] = age_min
    if age_max:
        targeting_spec["age_max"] = age_max
    return reachestimate(ad_account_id, targeting_spec)
    
    

import csv,sys
writer = csv.writer(sys.stdout)
writer.writerow(["city", "device", "gender", "age_min", "age_max", "age_bracket", "count"])

# "bedford", "maidstone", "reading", "chelmsford", "oxford", "canterbury", "colchester"]):
        
for city in ["reading"]:
    for device in ["all", "desktop", "mobile"]:
        for gender in ["all", "male", "female"]:
            for (age_min, age_max) in [(None, None), (13, 17), (18, 24), (25, 34), (35, 44), (45,54), (55,64), (65,None)]:
                if age_min is None and age_max is None:
                    bracket = "all"
                elif age_max is None:
                    bracket = "65+"
                else:
                    bracket = "%d-%d" % (age_min, age_max)
                writer.writerow([city, device, gender, age_min, age_max, bracket, reach(city, age_min=age_min, age_max=age_max, gender=gender, device_type=device)])
                time.sleep(1)
        

# def mobile_vs_
# print json.dumps(reachestimate(ad_account_id, {
#     "page_types": ["mobile"],
#     "geo_locations": {"cities": [{"key":  bedford["key"], "radius": 0, "distance_unit": "mile"}]}}))
# print json.dumps(reachestimate(ad_account_id, {
#     "page_types": ["desktop"],
#     "geo_locations": {"cities": [{"key":  bedford["key"], "radius": 0, "distance_unit": "mile"}]}}))
