import nltk.sem.logic as logic
lgp = logic.LogicParser()


class Var(object):
    def __init__(self, v):
        assert isinstance(v, str)
        self.v = v

    def __str__(self):
        return self.v

    def free(self):
        return {self.v}

    def bound(self):
        return {}

    def sub(self, v, exp):
        if self.v == v:
            return exp
        return self

    def beta(self):
        return Var(self.v)


class Const(object):
    def __init__(self, c):
        assert isinstance(c, str)
        self.c = c

    def __str__(self):
        return self.c

    def free(self):
        return {}

    def bound(self):
        return {}

    def sub(self, v, exp):
        return self


class Comb(object):
    def __init__(self, s, t):
        self.s = s
        self.t = t

    def __str__(self):
        return "( {} {} )".format(self.s, self.t)

    def free(self):
        return self.s.free() | self.t.free()

    def bound(self):
        return self.s.bound() | self.t.bound()

    def sub(self, v, exp):
        return Comb(self.s.sub(v, exp), self.t.sub(v, exp))

    def beta(self):
        if isinstance(self.s, Comb):
            return Comb(self.s.beta(), self.t)

        if isinstance(self.s, Abst):
            return self.s.s.sub(self.s.x, self.t)

        if isinstance(self.t, Abst) or isinstance(self.t, Comb):
            return Comb(self.s, self.t.beta())
        return self

    def alpha(self, x, y):
        if isinstance(self.t, Var):
            if str.find(self.s, x) == -1:
                return self.s.replace(x, y)
            return self

        if isinstance(self.t, Abst) or isinstance(self.t, Comb):
            return Comb(self.s, self.t.alpha(x, y))


class Abst(object):
    def __init__(self, x, s):
        self.x = x
        self.s = s

    def __str__(self):
        return "\\{} -> {}".format(self.x, self.s)

    def free(self):
        return self.s.free() - {self.x}

    def bound(self):
        return {self.x} | self.s.bound()

    def sub(self, v, exp):
        if v == self.x: return self
        return Abst(self.x, self.s.sub(v, exp))

    def beta(self):
        return Abst(self.x, self.s.beta())

    def alpha(self, x, y):
        return Abst(self.x, self.s.alpha(x, y))


zero = Abst('f', Abst('x', Var('x')))
one = Abst('f', Abst('x', Comb(Var('f'), Var('x'))))
two = Abst('f', Abst('x', Comb(Var('f'), Comb(Var('f'), Var('x')))))
three = Abst('f', Abst('x', Comb(Var('f'), Comb(Var('f'), Comb(Var('f'), Var('x'))))))
four = Abst('f', Abst('x', Comb(Var('f'), Comb(Var('f'), Comb(Var('f'), Comb(Var('f'), Var('x')))))))
five = Abst('f', Abst('x', Comb(Var('f'), Comb(Var('f'), Comb(Var('f'), Comb(Var('f'), Comb(Var('f'), Var('x'))))))))


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


def sum(m, n):
    return Abst('f', Abst('x', Comb(Comb(m, Var('f')), Comb(Comb(n, Var('f')), Var('x')))))


def succ(n):
    return Abst('f', Abst('x', Comb(Var('f'), Comb(Comb(n, Var('f')), Var('x')))))


def mult(m, n):
    return Abst('f', Abst('x', Comb(Comb(m, Comb(n, Var('f'))), Var('x'))))


def lambda_true():
    return Abst('u', Abst('v', Var('u')))


def lambda_false():
    return Abst('u', Abst('v', Var('v')))


def iszero(n):
    return Comb(Comb(Abst('n', n), Abst('x', lambda_false())), lambda_true())


def pred(n):
    return Abst('f', Abst('x', Comb(
        Comb(Comb(n, Abst('g', Abst('h', Comb(Var('h'), Comb(Var('g'), Var('f')))))), Abst('u', Var('x'))),
        Abst('u', Var('u')))))


def Y1(p):
    return Abst('f', Comb(
        Comb(Abst('x', Comb(Var('f'), Comb(Var('x'), Var('x')))), Abst('x', Comb(Var('f'), Comb(Var('x'), Var('x'))))),
        p))


def Y():
    return Abst('f', Abst('x', Comb(Comb(Var('f'), Var('f')), Var('x'))))


def F(n):
    return Abst('f', Abst('n', Comb(Comb(iszero(n), one), mult(n, Comb(Var('f'), pred(n))))))


def fact(z):
    return Comb(Y(), F(z))


# def fact(n):
#     T=Abst('f',Abst('x',Comb(Comb(Var('f'),Var('f')),Var('x'))))
#     G=Abst('g',Abst('n',Comb(Comb(n,Abst('g',mult(n,Comb(Comb(Var('g'),Var('g')),pred(n))))),one)))
#     return Comb(T,G)


# x=fact(two)
# print(x)
# for _ in range(30):
#     x = x.beta()
#     print(x)

x = iszero(one)
for _ in range(5):
    x = x.beta()
print(x)
