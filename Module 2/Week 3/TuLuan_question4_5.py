from TuLuan_question4_2 import compute_prior_probability
from TuLuan_question4_3 import compute_conditional_probability, train_data
import numpy as np

def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probability(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(train_data)

    return prior_probability, conditional_probability, list_x_name


prior_probability, conditional_probability, list_x_name = train_naive_bayes(train_data)
