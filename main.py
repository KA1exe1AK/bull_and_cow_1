class Vehicle(object):


    def __init__(self, color, doors, tires, vtype):

        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):

        return "%s braking" % self.vtype

    def drive(self):

        return "I'm driving a %s %s!" % (self.color, self.vtype)


if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

truck = Vehicle("red", 3, 6, "truck")
print(truck.drive())
print(truck.brake())


class Neuron:

    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        sum = 0
        self.x = x
        for i in range(len(self.w)):
            sum += self.w[i] * x[i]
        return self.f(sum)

    def backlog(self):
        try:
            return self.x
        except:
            return None
n = Neuron([1,2,3,4],f = lambda x: x * 1)
print(n.backlog())
n1 = Neuron([0.1,0.2,0.3,0.4],f=lambda x: 1 * (x>0.5))
print(n1.forward([5,6,7,8]))
n2 = Neuron(None)
print(n1.backlog())

# получить все вхождения нужного слова
word_occurences = [ i for i, word in enumerate(data["dog"]) if word.lower() == target_word ]
data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)