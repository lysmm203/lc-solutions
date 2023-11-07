


if __name__ == '__main__':
    nums = [1]

    for k in range(2,2):
        print("AA")

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                print("True")

    print("False")

