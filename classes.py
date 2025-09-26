class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circule(Shapes) :
    def __init__ (self, color, is_filled, radius) :
        super().__init__(color, is_filled)
        self.radius = radius

    def display_info(self) :
        print("Circule info-->")
        print(f"color:{self.color}")
        print(f"is_filled:{self.is_filled}")
        print(f"radius:{self.radius}")

    def area(self) :
        print(f"Area :{3.14*self.radius**2}")     

class Square(Shapes) :
    def __init__ (self, color, is_filled, side) :
        super().__init__(color, is_filled)
        self.side = side

    def display_info(self) :
        print("Square info-->")
        print(f"color:{self.color}")
        print(f"is_filled:{self.is_filled}")
        print(f"side:{self.side}")

    def area(self) :
        print(f"Area :{self.side**2}")         

class Rectangle(Square) :
    def __init__ (self, color, is_filled, side, tall) :
        super().__init__(color, is_filled, side)
        self.tall = tall
    
    def display_info(self) :    
        print("Square info-->")
        print(f"color:{self.color}")
        print(f"is_filled:{self.is_filled}")
        print(f"side:{self.side}")
        print(f"tall:{self.tall}")
    def area(self) :
        print(f"Area :{self.side*self.tall}")              

class Triangle(Shapes) :
    pass        