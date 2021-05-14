import json
import requests
import csv
import pandas as pd
import os


#API CALL FOR BUSINESSES
def api_call(params, key):
    url = 'https://api.yelp.com/v3/businesses/search'
    SEARCH_LIMIT = 20
    headers = {
            'Authorization': 'Bearer {}'.format(key),
        }
    
    response = requests.get(url, headers=headers, params=url_params)
    print(response.status_code)
    return response.json()

#PARSING DATA 
def parse_results(results):
    parsed_results={}
    parse=[]

    for data in results["businesses"]:
      
        idee = data.get("id",None)
        name = data.get("name",None)
        alias = data.get("alias",None)
        price=data.get('price', None)
        is_closed = data.get("is_closed",None)
#         coordinates = data.get("coordinates",None)
        Longitude=data["coordinates"]["longitude"]
        Latitude = data["coordinates"]["latitude"]
        review_count = data.get("review_count",None)
        rating = data.get("rating", None)
        
        parsed_results={"id":idee, "name":name, "alias":alias, "is_closed":is_closed, "longitude":Longitude, "latitude":Latitude, "price":price, "review_count":review_count, "rating":rating}
        parse.append(parsed_results)
        
    return parse
       

#SAVING THE PARSED DATA
def df_safe(filepath, parsed):
    
    # your code to open the csv file, concat the current data, and save the data. 
    with open(filepath, "a") as business:
        if len(parsed)!=0:
            keys = parsed[0].keys()
            writer = csv.DictWriter(business, keys)
            writer.writerows(parsed)
        
    print("open")
 
    
#API CALL FOR REVIEWS

#GETTING BUSINESS IDS FROM BUSINESS FILES
def get_ids(filepath):
    aidee=[]
    with open(filepath) as business:
        writer = csv.reader(business)
        for row in writer:
            aidee.append(row[0])
    
    return aidee

#MAKING THE CALL TO THE API FOR REVIEWS
def review_call(business_id, key):
    url = 'https://api.yelp.com/v3/businesses/'+business_id+"/reviews"
    headers = {
            'Authorization': 'Bearer {}'.format(key),
        }
    req = requests.get(url, headers=headers)
#     print(req.status_code)
    return req.json()


#PARSING THE REVIEWS
def parse_reviews(reviews, businessid):
    parse_results={}
    parse=[]
    
    for review in reviews["reviews"]:
        Businessid = businessid

        text = review.get("text",None)
        rating = review.get("rating",None)
        user_name=review["user"].get("name", None)
        
        parse_results={"businessid":Businessid, "user_name":user_name, "text": text, "rating":rating}
        parse.append(parse_results)
    
    return parse

#SAVING THE PARSED RESULTS TO A FILE
def df_safe(filepath, parsed):
    
    # your code to open the csv file, concat the current data, and save the data. 
    with open(filepath, "a") as reviews:
        if len(parsed)!=0:
            keys = parsed[0].keys()
            writer = csv.DictWriter(reviews, keys)
            writer.writerows(parsed)
            
    print("open")
