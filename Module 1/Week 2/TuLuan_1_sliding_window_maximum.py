# Find the maximum value in a sliding window of size k
def maxSlidingWindow(nums, k):
    if k < 1:
        return []
    for i in range(len(nums) - k + 1):  # Code for visualize and stuffs, yeah it's too good i know :D
        window = nums[i:i + k]
        max_val = max(window)
        before_window = nums[:i]
        after_window = nums[i + k:]
        print(f"{before_window}, [{', '.join(map(str, window))}], {', '.join(map(str, after_window))} => max {max_val}")
    return


if __name__ == "__main__":
    # Test 1
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    maxSlidingWindow(num_list, k)

    # Test 2
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 4
    maxSlidingWindow(num_list, k)

    # Test 3
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 5
    maxSlidingWindow(num_list, k)
