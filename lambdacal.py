from math import factorial


def x_():
    return 0


def f_(x=None):
    return lambda: 1 + x()


def interpret(f):
    # the natural value of a function
    return f(f_)(x_)()


def predicate(f):
    # the bool value of a function
    if f(f_)(x_)() == 0:
        return False
    else:
        return True


Church_0 = lambda f: lambda x: x
Church_1 = lambda f: lambda x: f(x)
Church_2 = lambda f: lambda x: f(f(x))
Church_3 = lambda f: lambda x: f(f(f(x)))
Church_4 = lambda f: lambda x: f(f(f(f(x))))
Church_5 = lambda f: lambda x: f(f(f(f(f(x)))))

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

PLUS = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))

MULT = lambda m: lambda n: m(PLUS(n))(Church_0)
PRED = lambda n: lambda f: lambda x:\
    n(lambda g: lambda h: h(g(f)))(lambda u: x)(lambda u: u)

Church_True = lambda u: lambda v: u
Church_False = lambda u: lambda v: v
AND = lambda p: lambda q: p(q)(p)
OR = lambda p: lambda q: p(p)(q)
# NOT = λ p.p FALSE TRUE
NOT = lambda p: p(Church_False)(Church_True)

ISZERO = lambda n: n(lambda x: Church_False)(Church_True)

FACT_ = lambda n: n(lambda u: MULT(n)(FACT_(PRED(n))))(Church_1)

T = lambda f: lambda x: f(f)(x)
G = lambda g: lambda n: n(lambda u: MULT(n)(g(g)(PRED(n))))(Church_1)
FACT = T(G)
