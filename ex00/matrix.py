from typing import Generic, TypeVar, List
K = TypeVar("K")

class Matrix(Generic[K]):
    def __init__(self, rows: list[list[K]]):
        self.rows = [list(r) for r in rows]
 
    def __str__(self) -> str:
        return "\n".join("[" + " ".join(str(v) for v in row) + "]" for row in self.rows)
 
    def add(self, v: "Matrix[K]") -> None:
        try :
            if self.size() != v.size():
                raise ValueError("Matrices must have the same shape.")
            self.rows = [[self.rows[i][j] + v.rows[i][j] for j in range(len(self.rows[0]))] for i in range(len(self.rows))]
        except ValueError as e:
            print(e)
        # TODO: self = self + v  (in place, same shape only)
 
    def sub(self, v: "Matrix[K]") -> None:
        # TODO: self = self - v  (in place, same shape only)
        try :
            if self.size() != v.size():
                raise ValueError("Matrices must have the same shape.")
            self.rows = [[self.rows[i][j] - v.rows[i][j] for j in range(len(self.rows[0]))] for i in range(len(self.rows))]
        except ValueError as e:
            print(e)
 
    def scl(self, a: K) -> None:
        # TODO: self = a * self  (in place)
        try:
            self.rows = [[self.rows[i][j] * a for j in range(len(self.rows[0]))] for i in range(len(self.rows))]
        except ValueError as e:
            print(e)

    def size(self)-> tuple[int, int]:
        return len(self.rows), len(self.rows[0]) if self.rows else 0
def main() -> int:
    m1 = Matrix([[8., 6.], [1., 6.]])
    m2 = Matrix([[5., 7.], [2., 3.]])
    try:
        m1.add(m2)
        print(m1)
    except ValueError as e:
        print(e)
    
    m1 = Matrix([[8., 6.], [1., 6.]])
    m2 = Matrix([[5., 7.], [2., 3.]])
    try:
        m1.sub(m2)
        print(m1)
    except ValueError as e:
        print(e) 
    m1 = Matrix([[8., 6.], [1., 6.]])
    m1.scl(2.)
    print(m1)

if __name__ == "__main__":
    main()
