class D:
    x = 2
    pass


class B(D):
    x = 1
    pass


class C(D):
    pass


class E(B, C):
    pass


class A(E):
    pass
