class Rectangle:
    width: float
    height: float
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, value) -> None:
        self.width = value
        
    def set_height(self, value) -> None:
        self.height = value
        
    def get_area(self) -> float:
        return self.width * self.height
    
    def get_perimeter(self) -> float:
        return  (2 * self.width + 2 * self.height)
    
    def get_diagonal(self) -> float:
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
            
        w = "*" * self.width
        return ''.join(map(lambda r: f"{w}\n", range(self.height)))
        
    def get_amount_inside(self, shape) -> int:
        area_1 = self.get_area()
        area_2 = shape.get_area()
        return int(area_1 / area_2)
        
    
class Square(Rectangle):
    side: float
    
    def __init__(self, side) -> None:
        super().__init__(side, side)
        self.side = side
        
    def __str__(self) -> str:
        return f"Square(side={self.side})"
    
    def set_side(self, side) -> None:
        self.side = side
        super().set_height(side)
        super().set_width(side)
        
    def set_width(self, value) -> None:
        self.side = value
        return super().set_width(value)
    
    def set_height(self, value) -> None:
        self.side = value
        return super().set_height(value)
    