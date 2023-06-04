import math

class Alakzat():

    def terfogat(self):
        pass

class Gomb(Alakzat):

    def __init__(self, radius):
        self.radius = radius
        self.atmero = 2 * radius
        self.kerulet = self.atmero * math.pi

    def terfogat(self):
        return 4*math.pi*self.radius**3 / 3

    def __str__(self) -> str:
        return f"Gomb: {self.radius}, {self.atmero}, {self.kerulet}"

class Henger(Alakzat):

    def __init__(self, radius, magassag):
        self.radius = radius
        self.atmero = 2 * radius
        self.magassag = magassag
        self.kerulet = self.atmero * math.pi

    def terfogat(self):
        return 2*math.pi*self.radius**2 * self.magassag

    def __str__(self) -> str:
        return f"Henger: {self.radius}, {self.atmero}, {self.kerulet}"



def main():
    g = Gomb(5)
    print(f"17 2-log: {math.log2(17)}")
    print(f"Gpont radius: {g.radius}")
    print(f'Gpont kerulete: {g.kerulet}')
    print(f"Terfogat: {g.terfogat()}")
    print(g)

    alakzatok = []
    for i in range(5):
        alakzatok.append(Gomb(i+1))
        # alakzatok += Gomb(i+1)
    alakzatok.append(Henger(7, 3))
    # Kiirjuk a listaelemeket
    for alakzat in alakzatok:
        print(alakzat)

    lekepzes = {
        "gomb1": Gomb(5),
        "labda": Gomb(3),
        "rud": Henger(1, 39)
    }
    print()
    print(lekepzes["gomb1"])
    print(lekepzes["rud"])
    lekepzes["dinnye"] = Gomb(89)
    print("dinnye" in lekepzes)
    print("bolygo" in lekepzes)
    if "dinnye" in lekepzes:
        print("Jo sokat eszünk")
    print(lekepzes.keys())
    print(lekepzes.values())



if __name__ == "__main__":
    main()