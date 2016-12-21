from django.shortcuts import render
import unirest
import json

def index(request):
    r = unirest.get("https://trailapi-trailapi.p.mashape.com/?&limit=500&q[state_cont]=California", headers={"X-Mashape-Key": "1u15iOxcOamshAqge8yv6lHqQptQp1QMZh1jsn5z4nFcYcRRzd","Accept": "text/plain"})
    s = r.body
    myarray=s['places']
    context = {
        'myarray':myarray
    }
    return render (request, "galavantapp/index.html", context)


def trail(request, id):
    r = unirest.get("https://trailapi-trailapi.p.mashape.com/?&limit=500&q[state_cont]=California", headers={"X-Mashape-Key": "1u15iOxcOamshAqge8yv6lHqQptQp1QMZh1jsn5z4nFcYcRRzd","Accept": "text/plain"})
    s = r.body
    myarray=s['places']
    wantedplace = "Not found"
    for place in myarray:
        if int(place['unique_id']) == int(id):
            wantedplace = place
            break
    print wantedplace
    context = {
        'place':wantedplace
    }
    return render(request, "galavantapp/trail.html", context)
