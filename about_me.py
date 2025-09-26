class Student:
    def __init__(self, name, pronouns, movie, food):
        self.name = name
        self.pronouns = pronouns
        self.fav_movie = movie
        self.fav_food = food


me = Student("Lingchen Zeng", "He/Him", "The Wandering Earth 2", "Sauerkraut fish")

print(me.name, "(",me.pronouns, ")")
print("")
print("My favourite movie is", me.fav_movie,"\nIt was a chinese blockbuster that tells a touching story about humanity's"
                    "strive toward survival by pushing the earth out of the solar system")
print("")
print("The food that I like the most is",me.fav_food,"\nIt is a dish that is popular all over China. The fish is cut into thin “veneer”, and then cooked in a "
                   "Sauerkraut Fish stock for a few seconds.")
