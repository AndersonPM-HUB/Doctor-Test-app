# from django.shortcuts import render

# Create your views here.
import requests

url = "https://priaid-symptom-checker-v1.p.rapidapi.com/symptoms"

querystring = {"language":"en-gb","format":"json"}

headers = {
	"X-RapidAPI-Host": "priaid-symptom-checker-v1.p.rapidapi.com",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)