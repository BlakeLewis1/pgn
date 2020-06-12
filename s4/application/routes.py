import random
from flask import request
from application import app, db
 
import requests
@app.route('/randomword', methods=['GET', 'POST'])
def password():
    animal = requests.get("http://service3:8002/animal").text
    fruit = requests.get("http://service2:8001/fruit").text
    colour = requests.get("http://service2:8001/colour").text # Gets the return from methods
    number = random.randrange(100) 
    num = str(number)

    words = [animal, fruit, colour, num] # makes an array to hold generated

    password = " "
    
    randWords = random.choices(words, k = 5) #new array of words in random order, k is number of items
    for i in range(len(randWords)): #
        password += randWords[i] # pulls each item from array and store it as password,
    
    return password