from typing import TypeVar, Generic

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
    def size(self) -> int:
        return len(self.data)
    def scl(self, a: K) -> None:
        # TODO: self = a * self  (in place)
        self.data = [new_content * a for new_content in self.data]

def linear_combination(u: list[Vector[K]], coefs: list[K]) -> Vector[K]:
    if len(u) != len(coefs):
        raise ValueError(
            f"Lists must have the same length. Got {len(u)} and {len(coefs)}."
        )
    for i in range(len(u)):
            u[i].scl(coefs[i])
    result = Vector([0. for _ in range(u[0].size())])
    for vector in u:
        result.add(vector)
    return result
   # return Vector(u[i].add(u[i + 1]) for i in range(len(coefs) - 1))
    #return Vector([sum(v.data[i] for v in u) for i in range(u[0].size())])


def main():
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])

    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])

    print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
   # print(linear_combination([v1, v2], [10., -2.]))

if __name__ == "__main__":
    main()