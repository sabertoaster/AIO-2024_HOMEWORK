from TuLuan_question4_2 import train_data
import numpy as np


def compute_conditional_probability(train_data):
    y_unique = ['no', 'yes']
    conditional_probability = []
    list_x_name = []

    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for j, label in enumerate(y_unique):
            label_data = train_data[train_data[:, -1] == label]
            for k, value in enumerate(x_unique):
                x_conditional_probability[j, k] = np.sum(label_data[:, i] == value) / label_data.shape[0]

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


conditional_probability, list_x_name = compute_conditional_probability(train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])
