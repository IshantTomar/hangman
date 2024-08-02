Animal = ["Cat", "Dog", "Cow", "Pig", "Fox", "Bear", "Lion", "Wolf", "Frog", "Fish", "Bird", "Bat", "Ant", "Bee", "Rat"]
Color = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Orange", "Pink", "Purple", "Brown"]
Country = ["USA", "Canada", "Mexico", "Brazil", "China", "India", "Japan", "France", "Germany", "Italy"]
Fruit = ["Apple", "Banana", "Grape", "Lemon", "Mango", "Orange", "Peach", "Pear", "Plum", "Kiwi"]
Sport = ["Soccer", "Tennis", "Baseball", "Basketball", "Cricket", "Golf", "Hockey", "Rugby", "Swimming", "Boxing"]
Vegetable = ["Carrot", "Potato", "Lettuce", "Tomato", "Onion", "Peas", "Corn", "Cucumber", "Broccoli", "Spinach"]
Vehicle = ["Car", "Bike", "Bus", "Truck", "Boat", "Plane", "Train", "Scooter", "Van", "Motorcycle"]

category = [Animal, Color, Country, Fruit, Sport, Vegetable, Vehicle]


def variable_name(var):
    for name, value in globals().items():
        if value is var:
            return name
