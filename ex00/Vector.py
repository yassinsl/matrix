from typing import Generic, TypeVar, List

K = TypeVar("K")

class Vector(Generic[K]):
    def __init__(self, data: list[K]):
        self.data = list(data)
    def __str__(self) -> str:
        return "\n".join(f"[{v}]" for v in self.data)
    def add(self, v: "Vector[K]") -> None:
    # TODO: self = self + v  (in place, same size only)
        if self.size() !=  v.size():
              raise ValueError(
                    f"Lists must have the same length. Got {len(list1)} and {len(list2)}."
                    ) 
        self.data = [self.data[i] + v.data[i] for i in range(self.size())]
        
    def sub(self, v: "Vector[K]") -> None:
    # TODO: self = self - v  (in place, same size only)
        if self.size() !=  v.size():
              raise ValueError(
                    f"Lists must have the same length. Got {len(list1)} and {len(list2)}."
                    ) 
        self.data = [self.data[i] - v.data[i] for i in range(self.size())]
 
    def scl(self, a: K) -> None:
        # TODO: self = a * self  (in place)
        self.data = [new_content * a for new_content in self.data]

    def size(self) -> int:
        return len(self.data)
def main()-> int:
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    try:
        u.add(v)
        print(u)
    except ValueError as e:
        print(e)
    
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    try:
        u.sub(v)
        print(u)
    except ValueError as e:
        print(e) 
    u = Vector([2., 3.])
    u.scl(2.)
    print(u)
 

if __name__ == "__main__":
        main()