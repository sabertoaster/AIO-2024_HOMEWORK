import math


# Exercise 2: Viết function mô phỏng theo 3 activation function.
# Given
def is_number(n):
    try:
        float(n)  # Type - casting the string to
    # If string is not a valid ‘float ‘ ,
    # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


# Sigmoid, ReLU, ELU
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def elu(x, alpha=1):
    return x if x > 0 else alpha * (math.exp(x) - 1)


def exercise2():
    x = int(input("Enter a number: "))
    if not is_number(x):
        print("x must be a number")
        return None
    func_type = input("Input activation Function (sigmoid|relu|elu)")
    if func_type.lower() not in ["sigmoid", "relu", "elu"]:
        print(f"{func_type} is not supported")
        return None

    if func_type.lower() == "sigmoid":
        print(f"Sigmoid({x}) = {sigmoid(x)}")
    elif func_type.lower() == "relu":
        print(f"ReLU({x}) = {relu(x)}")
    else:
        print(f"ELU({x}) = {elu(x)}")


if __name__ == "__main__":
    exercise2()
