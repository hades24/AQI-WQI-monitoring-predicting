#collecting data
import requests
karnataka={
    
"1":"Lal Bahadur Shastri Nagar, Kalaburagi, India",
"2":"Collector Office, Yadgir, India",
"3":"Ibrahimpur, Vijayapura, India",
"4":"Vidayagiri, Bagalkot, India",
"5":"Deshpande Nagar, Hubballi, India",
"6":"Kalyana Nagara, Chikkamagaluru, India",
"7":"Chikkaballapur Rural, Chikkaballapur, India",
"8":"Hebbal 1st Stage, Mysuru, India",
"9":"Vijay Nagar, Ramanagara, India",
"10":"Peenya, Bangalore, India",
"11":"SaneguravaHalli, Bangalore, India",
"12":"City Railway Station, Bangalore, India",
"13":"Hombegowda Nagar, Bengaluru, India",
"14":"Bapuji Nagar, Bengaluru, India",
"15":"Jayanagar 5th Block, Bengaluru, India",
"16":"BTM, Bangalore, India",
"17":"Silk Board, Bengaluru, India",
"18":"Hebbal, Bengaluru, India"
}
opt_avb=''' 
1 - Lal Bahadur Shastri Nagar, Kalaburagi, 
2 - Collector Office, Yadgir
3 - Ibrahimpur, Vijayapura
4 - Vidayagiri, Bagalkot
5 - Deshpande Nagar, Hubballi
6 - Kalyana Nagara, Chikkamagaluru
7 - Chikkaballapur Rural, Chikkaballapur
8 - Hebbal 1st Stage, Mysuru
9 - Vijay Nagar, Ramanagara
10 - Peenya, Bangalore
11 - SaneguravaHalli, Bangalore
12 - City Railway Station, Bangalore
13 - Hombegowda Nagar, Bengaluru
14 - Bapuji Nagar, Bengaluru
15 - Jayanagar 5th Block, Bengaluru
16 - BTM, Bangalore
17 - Silk Board, Bengaluru
18 - Hebbal, Bengaluru, India
'''
print(opt_avb)
Option=input("enter the option:")
city_name=karnataka[Option]
api_key="60f2dac8b282feffd464055f2be9039deccea0ea"
city_name="Thavakkara, Kannur"
url=f"https://api.waqi.info/feed/{city_name}/?token={api_key}"

response= requests.get(url)

json_data=response.json()

#Aqi = json_data['data']['aqi']

print(json_data)
#print(Aqi)

#quality
if Aqi>=0 and Aqi<=50 :
  print("good")
if Aqi>=51 and Aqi<=100:
  print("moderate")
if Aqi>=101 and Aqi<=150:
    print("Unhealthy for Sensitive Groups")
if Aqi>=151 and Aqi<=200: 
    print("Unhealthy")
if Aqi>=201 and Aqi<=300:
    print("Very Unhealthy")
if Aqi>300: 
   print("Hazardous")
#g-mail alert
