# matrix

A from-scratch linear algebra library in pure Python: vectors, matrices, and the
operations between them, built one exercise at a time with no NumPy or other
dependencies. The exercises follow the 42 school *matrix* ("Enter the Matrix") subject.

## Requirements

- Python 3.9 or newer (the code uses built-in generics such as `list[K]`)
- Nothing else to install

## Project layout

```
matrix/
├── ex00/
│   ├── geometric_object.py      # Vector and Matrix classes (the core library)
│   ├── Vector.py                # demo: vector add / sub / scl
│   └── matrix.py                # demo: matrix add / sub / scl
├── ex01/Linear_combination.py   # linear_combination(vectors, coefs)
├── ex02/linear_interpotion.py   # lerp(u, v, t)
├── ex03/DotProduct.py           # Vector.dot
├── ex04/Norm.py                 # Vector.norm_1, norm, norm_inf
├── ex05/cosing.py               # angle_cos(u, v)
├── ex06/CrossProduct.py         # cross_product(u, v)
└── ex07/matrix_multiplacation.py  # Matrix.mul_vec, Matrix.mul_mat
```

## Exercises

| Ex   | Topic                       | What it does                                              |
|------|-----------------------------|-----------------------------------------------------------|
| ex00 | Add, subtract, scale        | `add`, `sub`, `scl` on `Vector` and `Matrix`, in place    |
| ex01 | Linear combination          | `a₁·u₁ + a₂·u₂ + … + aₙ·uₙ`                               |
| ex02 | Linear interpolation        | `lerp(u, v, t) = (1 − t)·u + t·v` for scalars, vectors, matrices |
| ex03 | Dot product                 | `u · v = Σ uᵢ·vᵢ`                                         |
| ex04 | Norms                       | Manhattan (`norm_1`), Euclidean (`norm`), supremum (`norm_inf`) |
| ex05 | Cosine                      | `cos(θ) = (u · v) / (‖u‖ · ‖v‖)`                          |
| ex06 | Cross product               | 3D cross product `u × v`                                  |
| ex07 | Linear map, matrix multiply | `Matrix.mul_vec` (`y = A·x`) and `Matrix.mul_mat` (`C = A·B`) |

## Usage

```python
from ex00.geometric_object import Vector, Matrix

u = Vector([2., 3.])
v = Vector([5., 7.])
u.add(v)            # in place: u is now [7., 10.]
print(u.dot(v))     # 105.0

m = Matrix([[1., 0.], [0., 1.]])
print(m.mul_vec(Vector([4., 2.])))
```

Operations like `add`, `sub` and `scl` modify the object in place and return it,
so they can be chained: `u.scl(1 - t).add(v.scl(t))`.

## Running the exercises

Each exercise file has a `main()` with example inputs. Run them from the repository
root as modules:

```bash
python3 -m ex01.Linear_combination
python3 -m ex02.linear_interpotion
python3 -m ex03.DotProduct
python3 -m ex04.Norm
python3 -m ex05.cosing
python3 -m ex06.CrossProduct
python3 -m ex07.matrix_multiplacation
```

The ex00 demos import `geometric_object` directly, so run them from inside `ex00/`:

```bash
cd ex00
python3 Vector.py
python3 matrix.py
```

## Status

Work in progress: ex00 to ex07 are written, later exercises are not started yet.
