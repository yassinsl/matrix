from typing import Generic, TypeVar, List
import math

K = TypeVar("K")

class Vector(Generic[K]):
    def __init__(self, data: list[K]):
        self.data = list(data)
    def __str__(self) -> str:
        return "\n".join(f"[{round(v, 1)}]" for v in self.data)
    def add(self, v: "Vector[K]") -> "Vector[K]":
    # TODO: self = self + v  (in place, same size only)
        if self.size() !=  v.size():
              raise ValueError(
                    f"Lists must have the same length. Got {len(list1)} and {len(list2)}."
                    ) 
        self.data = [self.data[i] + v.data[i] for i in range(self.size())]
        return self
    def sub(self, v: "Vector[K]") -> "Vector[K]":
    # TODO: self = self - v  (in place, same size only)
        if self.size() !=  v.size():
              raise ValueError(
                    f"Lists must have the same length. Got {len(list1)} and {len(list2)}."
                    ) 
        self.data = [self.data[i] - v.data[i] for i in range(self.size())]
        return self
 
    def scl(self, a: K) -> "Vector[K]":
        # TODO: self = a * self  (in place)
        self.data = [new_content * a for new_content in self.data]
        return self

    def size(self) -> int:
        return len(self.data)
    def dot(self, v: "Vector[K]") -> K:
        if self.size() !=  v.size():
              raise ValueError(
                    f"Lists must have the same length. Got {len(list1)} and {len(list2)}."
                    ) 
        return sum(self.data[i] * v.data[i] for i in range(self.size())) 

    def norm_1(self) -> float: 
        return round(sum(abs(value) for value in self.data), 1)

    def norm(self) -> float:
        return round(math.sqrt(sum(value **2 for value in self.data)), 1)

    def norm_inf(self) -> float:
        return round(max(abs(value) for value in self.data), 1)
                
class Matrix(Generic[K]):
    def __init__(self, rows: list[list[K]]):
        self.rows = [list(r) for r in rows]
 
    def __str__(self) -> str:
        return "\n".join("[" + " ".join(str(round(v, 1)) for v in row) + "]" for row in self.rows)
 
    def add(self, v: "Matrix[K]") -> "Matrix[K]":
        try :
            if self.size() != v.size():
                raise ValueError("Matrices must have the same shape.")
            self.rows = [[self.rows[i][j] + v.rows[i][j] for j in range(len(self.rows[0]))] for i in range(len(self.rows))]
        except ValueError as e:
            print(e)
        # TODO: self = self + v  (in place, same shape only)
        return self
 
    def sub(self, v: "Matrix[K]") -> "Matrix[K]":
        # TODO: self = self - v  (in place, same shape only)
        try :
            if self.size() != v.size():
                raise ValueError("Matrices must have the same shape.")
            self.rows = [[self.rows[i][j] - v.rows[i][j] for j in range(len(self.rows[0]))] for i in range(len(self.rows))]
        except ValueError as e:
            print(e)
        return self

    def scl(self, a: K) ->  "Matrix[K]":
        # TODO: self = a * self  (in place)
        try:
            self.rows = [[self.rows[i][j] * a for j in range(len(self.rows[0]))] for i in range(len(self.rows))]
        except ValueError as e:
            print(e)
        return self

    def size(self)-> tuple[int, int]:
        return len(self.rows), len(self.rows[0]) if self.rows else 0