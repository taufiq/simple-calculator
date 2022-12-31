def get_function_operation(operation: str):
    if operation == "ADD":
        return lambda x, y: x + y
    elif operation == "SUB":
        return lambda x, y: x - y
    elif operation == "MUL":
        return lambda x, y: x * y


class Lit:
    def __init__(self, value) -> None:
        self.value = value
        pass

    def Add(self, lit_or_exp):
        return Expr(self, lit_or_exp, "ADD")

    def Sub(self, lit_or_exp):
        return Expr(self, lit_or_exp, "SUB")

    def Mul(self, lit_or_exp):
        return Expr(self, lit_or_exp, "MUL")

    def simplify(self):
        return self

    def __str__(self) -> str:
        return f'{self.value}'

    def __repr__(self) -> str:
        return f'{self.value}'


class Expr:
    def __init__(self, lhs, rhs, op) -> None:
        self.lhs = lhs
        self.rhs = rhs
        self.op = op
        pass

    def simplify(self):
        if not isinstance(self.lhs, Var):
            self.lhs = self.lhs.simplify()

        if not isinstance(self.rhs, Var):
            self.rhs = self.rhs.simplify()

        if not isinstance(self.rhs, Var) and not isinstance(self.lhs, Var) and isinstance(self.lhs, Lit) and isinstance(self.rhs, Lit):
            operation_func = get_function_operation(self.op)
            return Lit(operation_func(self.lhs.value, self.rhs.value))

        return self

    def Add(self, lit_or_exp):
        return Expr(self, lit_or_exp, "ADD")

    def Sub(self, lit_or_exp):
        return Expr(self, lit_or_exp, "SUB")

    def Mul(self, lit_or_exp):
        return Expr(self, lit_or_exp, "MUL")

    def __str__(self):
        return f'({self.lhs} {self.op} {self.rhs})'

    def __repr__(self):
        return self.__str__()


class Var(Lit):
    def __init__(self, value) -> None:
        super().__init__(value)
