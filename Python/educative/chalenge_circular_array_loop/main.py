def next_step(pointer, value, size):
    total_value = (pointer + value) % size
    if total_value < 0:
        total_value += size

    return total_value


def is_not_cycle(nums, prev_direction, pointer):
    current_direction = nums[pointer] >= 0
    if (prev_direction != current_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    return False


def circular_array_loop(nums):
    size = len(nums)

    for num_index in range(size):
        slow = num_index
        fast = num_index
        forvard = nums[num_index] > 0

        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forvard, slow):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forvard, fast):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forvard, fast):
                break

            if slow == fast:
                return True

    return False


def main():
    input = (
        [-2, -3, -9],
        [-5, -4, -3, -2, -1],
        [-1, -2, -3, -4, -5],
        [2, 1, -1, -2],
        [-1, -2, -3, -4, -5, 6],
        [1, 2, -3, 3, 4, 7, 1],
        [2, 2, 2, 7, 2, -1, 2, -1, -1],
    )
    num = 1

    for i in input:
        print(f"{num}.\tCircular array = {i}")
        print(f"\n\tFound loop = {circular_array_loop(i)}")
        print("-" * 100, "\n")
        num += 1


if __name__ == "__main__":
    main()
