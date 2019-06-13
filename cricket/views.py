from rest_framework.decorators import api_view
from pymongo import MongoClient
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime,timedelta

from rest_framework.response import Response



# Create your views here.

client=MongoClient()
db= client['cricket']

#players count (country-wise).
@api_view(['GET'])
def get_first_cric(request):
    collection=db['players']
    cursor=collection.aggregate([{"$group":{"_id":"$country","count":{"$sum":1}}}])
    data=list(cursor)
    return JsonResponse(data,safe=False)

#players whose is captain and also is keeper
@api_view(['GET'])
def get_capkeep(request):
    collection = db['players']
    cursor = collection.find({"is_keeper":True, "is_captain":True})
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)


#all captains with their country
@api_view(['GET'])
def get_cap(request):
    collection = db['players']
    cursor = collection.find({"is_captain":True})
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)

#right-hand batsman (country-wise)
@api_view(['GET'])
def get_right(request):
    collection = db['players']
    cursor = collection.find({"batting_hand" : "Right_Hand"})
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)

#get added player 
@api_view(['GET'])
def get_fav(request):
    collection = db['players']
    cursor = collection.find({"fav":"dhoni"})
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)
    
#players who born in the year 1987
@api_view(['GET'])
def get_dat(request):
    collection=db['players']
    from_date = datetime(1987,1,1,0,0)
    to_date= datetime(1987,12,31,0,0)
    
    cursor=collection.find({"dob":{"$gte":from_date,"$lt":to_date}})
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)


#players whose age is between 30 and 40
@api_view(['GET'])
def get_btw(request):
    collection=db['players']
    from_date = datetime(1979,1,1,0,0)
    to_date= datetime(1989,1,1,0,0)
    
    cursor=collection.find({"dob":{"$gte":from_date,"$lt":to_date}})
    data = []
    for doc in cursor:
        doc.pop("_id")
        data.append(doc)
    return JsonResponse(data,safe=False)

# @api_view(['POST'])
# def post_fav(request):
#     collection = db['players']

#     cursor = collection.insert({})
#     return JsonResponse(data,safe=False)

@api_view(['POST'])
def post_fav(request):
    print(request.data)
    collection = db['players']
    data= []
    # cursor=collection.insert(request.data)
    cursor=collection.insert({"player_id" : request.data['player_id'], "player_name" :request.data['player_name'],"dob":request.data["$datetime"],"batting_hand":request.data['batting_hand'],"bowling_skill":request.data['bowling_skill'],"country":request.data["country"],"is_umpire":request.data["is_umpire"],"is_keeper":request.data["is_keeper"],"is_captain":request.data["is_captain"]})
    return JsonResponse({"data":"success"},safe=False)
