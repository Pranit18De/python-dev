import json
import turtle
import urllib.request
import time

url1 = "http://api.open-notify.org/astros.json"
res1 = urllib.request.urlopen(url1)
result = res1.read()
print(result)

url2 = "http://api.open-notify.org/iss-now.json"
res2 = urllib.request.urlopen(url2)
result= json.loads(res2.read())
print(result)
location = result['iss_position']
lon =float(location['longitude'])
lat =float(location['latitude'])
print("longitude:"+str(lon))
print("latitude:"+str(lat))





#now pointing where the ISS is:

screen = turtle.Screen()
screen.title("The National Capital Region")
screen.setup(600,295)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.png')

#screen.register_shape('triangle')
iss = turtle.Turtle()
iss.shape('triangle')
iss.color('red')
iss.setheading(90)


iss.penup()
iss.goto(lon,lat)

#Satish Dhawan Space Centre, India
lat = 13.733
lon = 80.235
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)

location.dot(5)
location.hideturtle()


#date and time of passing

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat='+str(lat)+'&lon='+str(lon)
response = urllib.request.urlopen(url)
res= json.loads(response.read())
print(res)

dest = res['response'][1]['risetime']
print(dest)
style =('Arial',12,'bold')
location.write(time.ctime(dest),font=style)

turtle.done()




