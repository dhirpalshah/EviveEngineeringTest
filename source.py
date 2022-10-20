#! /usr/bin/python

"""
breakfast
Main (1): Eggs
Side (2): Toast
Drink (3): Coffee

lunch
Main (1): Sandwich
Side (2): Chips
Drink (3): Soda

dinner
Main (1): Steak
Side (2): Potatoes
Drink (3): Wine
Dessert (4): Cake

Rules:
1. An order consists of a meal and collection of comma separated item Ids.
2. The system should return the name of the items ordered
3. The system should always return items in the following order: meal, side, drink
4. If multiple items are ordered, the number of items should be indicated
5. Each order must contain a main and a side
6. If no drink is ordered, water should be returned
7. At breakfast, multiple cups of coffee can be ordered
8. At lunch, multiple sides can be ordered
9. At dinner, dessert must be ordered
10. At dinner, water is always provided

Sample Input/Output:

In: Breakfast 1,2,3
Out: Eggs, Toast, Coffee

In: Breakfast 2,3,1
Out: Eggs, Toast, Coffee

In: Breakfast 1,2,3,3,3
Out: Eggs, Toast, Coffee(3)

In: Breakfast 1
Out: Unable to process: Side is missing

In: Lunch 1,2,3
Out: Sandwich, Chips, Soda

In: Lunch 1,2
Out: Sandwich, Chips, Water

In: Lunch 1,1,2, 3
Out: Unable to process: Sandwich cannot be ordered more than once

In: Lunch 1,2,2
Out: Sandwich, Chips(2), Water

In: Lunch
Out: Unable to process: Main is missing, side is missing

In: Dinner 1,2,3,4
Out: Steak, Potatoes, Wine, Water, Cake

In: Dinner 1,2,3
Out: Unable to process: Dessert is missing
"""

breakfast = {
    1:"Eggs",
    2:"Toast",
    3:"Coffee"
} 

lunch = {
    1:"Sandwich",
    2:"Chips",
    3:"Soda"
}

dinner = {
    1:"Steak",
    2:"Potatoes",
    3:"Wine",
    4:"Cake"
}

err = "Unable to process: "


def menu_ordering_system(order):
    result = []
    temp = order.split()
    #print(temp)
    meal = temp[0]
    if len(temp) == 1:
        print(err + "Main is missing, side is missing")
        return

    items = temp[1]
    #items = items.split(",")
    items = [eval(i) for i in items.split(",")]
    items.sort()
    #print(meal)
    #print(items)

    '''match meal:
        case "Breakfast"
    # I would use a match switch but that is only in py3.10 or newer
    '''
    
    
    if 1 not in items:
        print(err + "Main is missing.")
        return
    if 2 not in items:
        print(err + "Side is missing.")
        return

    if (meal == "Breakfast"):
        for num in set(items):
            if items.count(num) > 1:
                result.append("{food}({freq})".format(food = breakfast.get(num), freq = items.count(num)))
            else:
                result.append("{food}".format(food = breakfast.get(num)))
        if 3 not in items:
            result.append("Water")

    elif (meal == "Lunch"):
        for num in set(items):
            if items.count(num) > 1:
                result.append("{food}({freq})".format(food = lunch.get(num), freq = items.count(num)))
            else:
                result.append("{food}".format(food = lunch.get(num)))
        if 3 not in items:
            result.append("Water")

    elif (meal == "Dinner"):
        if 4 not in items:
            print(err + "Dessert is missing")
            return
        for num in set(items):
            if items.count(num) > 1:
                result.append("{food}({freq})".format(food = dinner.get(num), freq = items.count(num)))
            else:
                result.append("{food}".format(food = dinner.get(num)))

    else:
        print(err + "Bad mealtime.")
        return


    print(",".join(result))

if __name__ == "__main__":
    menu_ordering_system("Breakfast 1,2,3")
    menu_ordering_system("Breakfast 2,3,1")
    menu_ordering_system("Breakfast 1,2,3,3,3")
    menu_ordering_system("Breakfast 1")
    menu_ordering_system("Lunch 1,2,3")
    menu_ordering_system("Lunch 1,2")
    #menu_ordering_system("Lunch 1,1,2, 3")
    menu_ordering_system("Lunch 1,2,2")
    menu_ordering_system("Lunch 2,3,1")
    menu_ordering_system("Lunch")
    menu_ordering_system("Dinner 1,2,3")
    menu_ordering_system("Dinner 1,2,3,4")

    # insert water for dinner
    # garbage input (work on splicing)
