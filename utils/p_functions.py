import math

# Available probability functions for p
p_functions = {
    "1/n^n": lambda n: 1 / (n ** n),
    "1/n^3": lambda n: 1 / (n ** 3),
    "1/n^2": lambda n: 1 / (n ** 2),
    "1/n": lambda n: 1 / n,
    "2/n": lambda n: 2 / n,
    "log(n) / n": lambda n: math.log(n) / n,
    "1/n^(2/3)": lambda n: 1 / (n ** (2 / 3)),
    "1/sqrt(n)": lambda n: 1 / math.sqrt(n),
    "1 / log(n)": lambda n: 1 / math.log(n)
}
