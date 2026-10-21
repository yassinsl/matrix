from ex00.geometric_object import Matrix, Vector
 

def mul_mat(self, mat: "Matrix") -> "Matrix":
 
 
def main():
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    v = Vector([4., 2.])
    print(u.mul_vec(v))
 
    u = Matrix([
        [2., 0.],
        [0., 2.],
    ])
    v = Vector([4., 2.])
    print(u.mul_vec(v))
 
    u = Matrix([
        [2., -2.],
        [-2., 2.],
    ])
    v = Vector([4., 2.])
    print(u.mul_vec(v))
 
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    v = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    print(u.mul_mat(v))
 
    u = Matrix([
        [1., 0.],
        [0., 1.],
    ])
    v = Matrix([
        [2., 1.],
        [4., 2.],
    ])
    print(u.mul_mat(v))

    u = Matrix([
        [3., -5.],
        [6., 8.],
    ])
    v = Matrix([
        [2., 1.],
        [4., 2.],
    ])
    print(u.mul_mat(v))

if __name__ == "__main__":
    main()
 