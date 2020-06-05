        animal = requests.get("http://service3:5002/animal").text
        fruit = requests.get("http://service3:5002/fruit").text
        colour = requests.get("http://service3:5002/colour").text # Gets the return from methods
        number = random.randint(100) 
        num = str(number)
        
        words = [animal, fruit, colour, num] # makes an array to hold generated
        
        password = ""
        randWords = random.choices(words, k = 5) # new array of words in random order, k is number of items
        for i in range(len(randWords)): # 
            password += randWords[i] # pulls each item from array and store it as password,
        return password