import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "Place your api key here"
headers = {
    "Authorization": "Bearer " + api_key
}
# here we are setting up the parameters to look for the location and the types of businesses we want to find
params = {
    "term": "Food",
    "location": "Deltona"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
# we are requesting to get all of the businesses with above 4.5 stars
names = [business["name"]
         for business in businesses if business["rating"] == 5]
print(names)
print("___________________________")
# We are going to loop and filer out the name of the business only
for business in businesses:
    print(business["name"])
