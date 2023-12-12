def find_sum_of_three(nums, target):

    nums.sort()

    for index in range(len(nums)):
        left = index + 1
        right = len(nums) - 1

        while left < right:
            iteration_sum = nums[index] + nums[left] + nums[right]

            if iteration_sum == target:
                return True

            if iteration_sum < target:
                left += 1
            else:
                right -= 1

    return False


if __name__ == "__main__":
    numbers_target_list = [([1, 2, 3, 4], 8), ([10, 10, 2, 8, 10], 20), ([1, 2, 3], 10)]

    for number_target in numbers_target_list:
        find_sum_of_three_status = (
            "has" if find_sum_of_three(number_target[0], number_target[1]) else "hasn't"
        )
        print(f"{number_target[0]} {find_sum_of_three_status} sum {number_target[1]}")
