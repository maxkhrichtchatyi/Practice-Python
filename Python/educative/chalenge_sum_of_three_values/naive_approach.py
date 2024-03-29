def find_sum_of_three(nums, target):

    for i in range(len(nums)):
        for j in range(len(nums) - 2):
            j += 1
            for k in range(len(nums) - 2):
                k += 1
                if nums[i] + nums[j] + nums[k] == target:
                    return True
    return False


if __name__ == "__main__":
    numbers_target_list = [([1, 2, 3, 4], 8), ([10, 10, 2, 8, 10], 20), ([1, 2, 3], 10)]

    for number_target in numbers_target_list:
        find_sum_of_three_status = (
            "has" if find_sum_of_three(number_target[0], number_target[1]) else "hasn't"
        )
        print(f"{number_target[0]} {find_sum_of_three_status} sum {number_target[1]}")
