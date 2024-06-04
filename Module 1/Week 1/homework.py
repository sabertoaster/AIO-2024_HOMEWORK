import math
import random


# Exercise1: F1 Score evaluation
def exercise1(tp, fp, fn):
    if type(tp) != int or type(fp) != int or type(fn) != int:
        print("Input type must be int")
        return None
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return None
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)
    print(f"F1 Score: {f1_score}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


# Test cases
exercise1(tp=2, fp=3, fn=4)
exercise1(tp='a', fp=3, fn=4)
exercise1(tp=2, fp='a', fn=4)
exercise1(tp=2, fp=3, fn='a')
exercise1(tp=2, fp=3, fn=0)
exercise1(tp=2.1, fp=3, fn=0)


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


exercise2()


# Viết function lựa chọn regression loss function để tính loss:

def mae(predictions, targets):
    return sum(abs(p - t) for p, t in zip(predictions, targets)) / len(predictions)


def mse(predictions, targets):
    return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)


def rmse(predictions, targets):
    return math.sqrt(mse(predictions, targets))


def calculate_loss():
    num_samples = input('Input number of samples (integer number) which are generated: ')

    if not num_samples.isnumeric():
        print('Number of samples must be an integer number.')
        return

    num_samples = int(num_samples)
    loss_name = input('Input loss name (MAE|MSE|RMSE): ')

    loss_functions = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse
    }

    if loss_name not in loss_functions:
        print(f'{loss_name} is not a supported loss function.')
        return

    loss_function = loss_functions[loss_name]

    for i in range(num_samples):
        prediction = random.uniform(0, 10)
        target = random.uniform(0, 10)
        loss = loss_function([prediction], [target])
        print(f'Sample-{i}, Predict: {prediction}, Target: {target}, {loss_name}: {loss}')


calculate_loss()


# Viết 4 functions để ước lượng các hàm số sau sin x, cos x, sinh x, cosh x

def factorial(n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sin(x, n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    return sum(((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(n))


def cos(x, n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    return sum(((-1) ** i) * (x ** (2 * i)) / factorial(2 * i) for i in range(n))


def sinh(x, n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    return sum((x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(n))


def cosh(x, n):
    if n <= 0:
        raise ValueError("n must be greater than 0")
    return sum((x ** (2 * i)) / factorial(2 * i) for i in range(n))


# Viết function thực hiện Mean Difference of nth Root Error:

def mean_difference_of_nth_root_error(y_true, y_pred, power_root, exponent):
    return abs(y_true ** (1 / power_root) - y_pred ** (1 / power_root))

print(mean_difference_of_nth_root_error(y_true=100, y_pred=99.5, power_root=2, exponent=1))
print(mean_difference_of_nth_root_error(y_true=50, y_pred=49.5, power_root=2, exponent=1))
print(mean_difference_of_nth_root_error(y_true=20, y_pred=19.5, power_root=2, exponent=1))
print(mean_difference_of_nth_root_error(y_true=0.6, y_pred=0.1, power_root=2, exponent=1))
