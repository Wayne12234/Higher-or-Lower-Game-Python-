data = [
    {
        "name": "Cristiano Ronaldo",
        "description": "Footballer",
        "country": "Portugal",
        "followers": 630
    },
    {
        "name": "Lionel Messi",
        "description": "Footballer",
        "country": "Argentina",
        "followers": 505
    },
    {
        "name": "Virat Kohli",
        "description": "Cricketer",
        "country": "India",
        "followers": 270
    },
    {
        "name": "MrBeast",
        "description": "YouTuber",
        "country": "USA",
        "followers": 250
    },
    {
        "name": "Babar Azam",
        "description": "Cricketer",
        "country": "Pakistan",
        "followers": 6
    }
]
import random
score = 0

while True:
    def get_input():
        p1 = random.choice(data)
        p2 =  random.choice(data)
        while p1==p2:
            p2 = random.choice(data)
        return p1,p2    

    p1,p2 = get_input()
    print(f"{p1["name"]} and {p2["name"]} , Who have more followers?")
    user_answer = input("Type 'A' or 'B' for answer : ").lower()
    

    if user_answer=="a" or user_answer=="b":
        if p1["followers"] > p2 ["followers"]:
            correct = "a"
        else:
            correct = "b"
        if user_answer==correct:
            score +=1 
            print(f"Correct Guess ! , Your score is {score}")
        else:
            exit(f"Wrong answer , finsl score is : {score}")      

                         

 


    












