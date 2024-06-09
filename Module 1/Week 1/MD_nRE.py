# Viết function thực hiện Mean Difference of nth Root Error:
def mean_difference_of_nth_root_error(y_true, y_pred, power_root, exponent):
    return abs(y_true ** (1 / power_root) - y_pred ** (1 / power_root))


if __name__ == "__main__":
    # Test cases
    print(mean_difference_of_nth_root_error(y_true=100, y_pred=99.5, power_root=2, exponent=1))
    print(mean_difference_of_nth_root_error(y_true=50, y_pred=49.5, power_root=2, exponent=1))
    print(mean_difference_of_nth_root_error(y_true=20, y_pred=19.5, power_root=2, exponent=1))
    print(mean_difference_of_nth_root_error(y_true=0.6, y_pred=0.1, power_root=2, exponent=1))
