from TuLuan_question4_4 import get_index_from_value
from TuLuan_question4_5 import prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(X[0], list_x_name[0])
    x2 = get_index_from_value(X[1], list_x_name[1])
    x3 = get_index_from_value(X[2], list_x_name[2])
    x4 = get_index_from_value(X[3], list_x_name[3])

    p_no = prior_probability[0] * conditional_probability[0][0, x1] * conditional_probability[0][1, x2] * \
           conditional_probability[0][2, x3] * conditional_probability[0][3, x4]
    p_yes = prior_probability[1] * conditional_probability[1][0, x1] * conditional_probability[1][1, x2] * \
            conditional_probability[1][2, x3] * conditional_probability[1][3, x4]

    if p_no > p_yes:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']
pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)

if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")
