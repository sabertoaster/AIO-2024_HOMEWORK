# Viết function lựa chọn regression loss function để tính loss:
import math
import random


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


if __name__ == "__main__":
    calculate_loss()
