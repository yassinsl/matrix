from geometric_object import Vector

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
