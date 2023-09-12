restaurants = ["Raising Canes", "Chick fil a", "Taco Bell", "Mcdonalds", "Burger King"]

print("Welcome to your restaurant ranker! Your current ranking is ", restaurants, "! You can add and rank new restaurants!")
new_resturant = input("What resturant would you like to add?")

def rank_resturant(new_resturant, restaurants):
    for i in range(len(restaurants)):
        str = "Do you like A) " + new_resturant + " or B) " + restaurants[i] + " more? A/B"
        ranking = input(str)
        if ranking == "A":
            restaurants.insert(i, new_resturant)
            break
        elif ranking == "B":
            continue
    return restaurants

print("Your new ranking is", rank_resturant(new_resturant, restaurants))