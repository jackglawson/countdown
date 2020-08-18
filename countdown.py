from copy import copy


def add(a, b):
    return a + b


def subtract(a, b):
    assert a > b
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    assert a % b == 0
    return int(a / b)


operators = {'+': add,
             '-': subtract,
             '*': multiply,
             '/': divide}


def perms_of_two(n):
    assert n > 1
    p = (0, 1)
    while max(p) <= n-1:
        yield p
        if p[1] == n-1:
            p = (p[0]+1, p[0]+2)
        else:
            p = (p[0], p[1]+1)


def possible_operations(v):
    """
    returns an operation in the form (number_1, number_2, operator)
    negative numbers are not allowed to be created as the subtraction operator makes them redundant
    """
    n = len(v)
    assert n > 1
    for i1, i2 in perms_of_two(n):

        # addition
        yield (v[i1], v[i2], '+')

        # subtraction
        if v[i1] > v[i2]:
            yield (v[i1], v[i2], '-')
        elif v[i2] > v[i1]:
            yield (v[i2], v[i1], '-')

        if v[i1] != 1 and v[i2] != 1:
            # multiplication

            yield (v[i1], v[i2], '*') if v[i1] >= v[i2] else (v[i2], v[i1], '*')

            # division
            if v[i1] % v[i2] == 0:
                yield (v[i1], v[i2], '/')
            elif v[i2] % v[i1] == 0:
                yield (v[i2], v[i1], '/')


def apply_operation(v, operation):
    """
    accepts: the remaining numbers, v, and an operation, (n1, n2, operator)
    returns: the updated remaining numbers, the new number
    """
    n1, n2, operator_flag = operation
    operator = operators[operator_flag]
    new_number = operator(n1, n2)

    w = list(v)
    w.remove(n1)
    w.remove(n2)
    w.append(new_number)

    return tuple(w), new_number


class CountdownSolver:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
        self.num_solutions = 0
        self.solutions = []
        self.route = []

    def solve(self):
        self.dfs(self.root())

    def dfs(self, c):
        """search algorithm"""
        if self.accept(c):
            self.output()
            return
        if self.reject(c):
            return

        for operation in possible_operations(c):
            next_c, new_number = apply_operation(c, operation)
            self.route.append(operation + (new_number,))
            self.dfs(next_c)
            self.route = self.route[:-1]

    def root(self):
        """the root of the backtracking tree"""
        return self.numbers

    def reject(self, c):
        """return true only if the partial candidate c is not worth completing"""
        return True if len(c) == 1 else False

    def accept(self, c):
        """return true if c is a solution of P, and false otherwise"""
        return True if self.target in c else False

    def output(self):
        """is called once a valid solution is found"""
        self.solutions.append(copy(self.route))
        self.num_solutions += 1


def remove_redundant_solutions(solutions):
    """
    removes solutions which are redundant by order
    e.g. 1+2=3, 4*5=20 is redundant with 4*5=20, 1+2=3
    """
    solution_signatures = set()
    unique_solutions = []

    for s in solutions:
        signature = tuple(sorted(s))
        if signature not in solution_signatures:
            solution_signatures.add(signature)
            unique_solutions.append(s)

    return unique_solutions


def display_solution(solution):
    for operation in solution:
        n1, n2, operator_flag, new_number = operation
        print('{} {} {} = {}'.format(n1, operator_flag, n2, new_number))
    print('\n')


def countdown(numbers, target):
    solver = CountdownSolver(numbers, target)
    solver.solve()
    solutions = solver.solutions

    if not solutions:
        print('No solutions')
        return

    solutions = remove_redundant_solutions(solutions)
    quickest_solution = min(solutions, key=len)
    print('{} solution{} found. One possible solution is:'.format(len(solutions), 's' if len(solutions) > 1 else ''))
    display_solution(quickest_solution)


numbers = (75, 100, 50, 25, 10, 2)
target = 317
countdown(numbers, target)
