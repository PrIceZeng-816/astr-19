"""
Write a Python program that declares a class describing your favorite animal.
Have the data members of the class represent the following physical parameters of the animal:
length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool),
is it furry? (bool). Write an initialization function that sets the values of the data members when an instance of
the class is created. Write a member function of the class to print out and describe the data members representing the
physical characteristics of the animal.
"""

class cat():
    def __init__(self, arm_length, leg_length, eyes_num, tail, furry):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.eyes_num = eyes_num
        self.tail = tail
        self.furry = furry

    def arm(self):
        return self.arm_length

    def leg(self):
        return self.leg_length

    def eyes(self):
        return self.eyes_num

    def tail(self):
        return self.tail

    def furry(self):
        return self.furry

    def print(self):
        print("A cat usually has:")
        print(random_cat.arm(),"inch arms")
        print(random_cat.leg(),"inch legs")
        print(random_cat.eyes(),"eyes")
        if self.tail == True:
            print("A tail")
        else:
            print("No tail")
        if self.furry == True:
            print("Furry")
        else:
            print("No  Fur")



random_cat = cat(9.0,9.0,2,True,True)
random_cat.print()