def threeSum(nums):
    List = []
    s_nums = sorted(nums)
    for i in range(len(s_nums) - 2):
        if (i > 0 and s_nums[i] == s_nums[i - 1]):
            continue
        j, k = i + 1, len(s_nums) - 1
        while (j < k):
            sum = s_nums[i] + s_nums[j] + s_nums[k]
            if sum == 0:
                List.append([s_nums[i], s_nums[j], s_nums[k]])
                j += 1
                k -= 1
                while (s_nums[j] == s_nums[j - 1] and j < k):
                    j += 1
                while (s_nums[k] == s_nums[k + 1] and j < k):
                    k -= 1
            elif sum < 0:
                j += 1
            else:
                k -= 1
    return List


nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
print(threeSum(nums))
