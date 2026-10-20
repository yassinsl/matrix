from geometric_object import Matrix

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
