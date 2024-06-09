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


if __name__ == "__main__":
    # Test cases
    exercise1(tp=2, fp=3, fn=4)
    exercise1(tp='a', fp=3, fn=4)
    exercise1(tp=2, fp='a', fn=4)
    exercise1(tp=2, fp=3, fn='a')
    exercise1(tp=2, fp=3, fn=0)
    exercise1(tp=2.1, fp=3, fn=0)
