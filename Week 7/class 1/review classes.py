class Shape:
    colour = ""

    def __init__(self, input_colour):
        self.colour = input_colour

    def declare_yourself(self):
        print("i am a shape and my color is " + self.colour)

triangle1 = Shape("green")
triangle1.declare_yourself()
