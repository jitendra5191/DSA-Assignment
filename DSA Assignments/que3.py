"""
Question 3: Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.
Must be done in-place without making a copy of the array.
"""


def move_zeroes(nums: list[int]) -> None:
    write_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[write_pos] = nums[i]
            write_pos += 1

    while write_pos < len(nums):
        nums[write_pos] = 0
        write_pos += 1


if __name__ == "__main__":
    nums1 = [0, 1, 0, 3, 12]
    print(f"Input : {nums1}")
    move_zeroes(nums1)
    print(f"Output: {nums1}")

    nums2 = [0]
    print(f"\nInput : {nums2}")
    move_zeroes(nums2)
    print(f"Output: {nums2}")

    nums3 = [1, 2, 3]
    print(f"\nInput : {nums3}")
    move_zeroes(nums3)
    print(f"Output: {nums3}")

    nums4 = [0, 0, 0]
    print(f"\nInput : {nums4}")
    move_zeroes(nums4)
    print(f"Output: {nums4}")

    nums5 = [1, 3, 5, 0, 0]
    print(f"\nInput : {nums5}")
    move_zeroes(nums5)
    print(f"Output: {nums5}")
