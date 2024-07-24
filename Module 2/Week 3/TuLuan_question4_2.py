from TuLuan_question4_1 import train_data
import numpy as np
def compute_prior_probability(train_data):
    y_unique = ['no', 'yes']
    prior_probability = np.zeros(len(y_unique))

    total_samples = train_data.shape[0]
    for i, label in enumerate(y_unique):
        prior_probability[i] = np.sum(train_data[:, -1] == label) / total_samples

    return prior_probability


prior_probability = compute_prior_probability(train_data)
print("P(play tennis = No)", prior_probability[0])
print("P(play tennis = Yes)", prior_probability[1])
