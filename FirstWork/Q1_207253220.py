import math
import inspect

def calculateDistance(x1: float,y1: float,x2: float,y2: float) -> float:
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
class Circle:
    def __init__(self, a,b,r):
        self.a:float = a
        self.b:float = b
        self.r:float = r

    def area(self) -> float:
        return math.pi * self.r**2
    def perimeter(self) -> float :
        return math.pi * self.r * 2

    def test_belong(self,x: float,y: float) -> bool:
        # calculate distance between points
        
        print(self.__class__.__name__)
        distance = calculateDistance(self.a,self.b,x,y)
        if (self.r >= distance):
            print(f'The point A({x} {y}) belongs to the circle {self.get_my_name()}')
            return True
        print(f"The point A({x} {y}) doesn't belongs to the circle {self.get_my_name()}")


    def get_my_name(self) -> str:
        ans:list[str] = []
        frame = inspect.currentframe().f_back
        tmp:dict = {**frame.f_globals, **frame.f_locals}
        for k, var in tmp.items():
            if isinstance(var, self.__class__):
                if hash(self) == hash(var):
                    ans.append(k)
        if len(ans):
            return ans[0]
        return 'C'


if __name__ == '__main__':
    C = Circle(1, 2, 1)
    print ("the perimeter of the circle C is:", C.perimeter() )
    print ("the area of circle C is:", C.area())
    A = C.test_belong(1,1)
    print ("the point is in the circle:", A)