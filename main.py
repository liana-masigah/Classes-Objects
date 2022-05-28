
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
        pass
    
    def change_name(self, new_name):
        self.name = new_name
        print("You're name is " + self.name)

    def change_age(self, new_age):
        self.age = new_age
        print("You're " + str(self.age) + " years old")

    def add_track(self, new_track):
        self.tracks = new_track
        print("You're in " + str(self.tracks) + " track")
        
        
    def get_score(self):
        print("You have " + str(self.score) + " points")

Bob = Student("Bob", 26, ["FE","BE"], 20.90)


# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
