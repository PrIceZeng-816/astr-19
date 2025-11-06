class planet:
    def __init__(self, name, temp, num_moons, num_rings, gas, habitable):
        self.name = name
        self.temp = temp
        self.num_moons = num_moons
        self.num_rings = num_rings
        self.gas = gas
        self.habitable = habitable

    def name(self):
        return self.name

    def temp(self):
        return self.temp

    def num_moons(self):
        return self.num_moons

    def num_rings(self):
        return self.num_rings

    def gas(self):
        return self.gas

    def habitable(self):
        return self.habitable

    def print(self):
        print(f"{self.name}: The temperature of the planet is {self.temp}C. It has {self.num_moons} moons and {self.num_rings}. "
              f"The dominate gas is {self.gas}. habitable: {self.habitable}")

earth = planet("Earth",15, 1,0,"nitrogen",True)

if __name__ == "__main__":
    earth.print()