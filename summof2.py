def summof2(nums, n):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i] + nums[j] ==n:
                return [i,j]

#а теперь отсортирванный

def sumof2_sort(nums, n):
    left, right =0, len(nums)-1
    while left<right:
        if n>nums[right] + nums[left]:
            left+=1
        elif n< nums[right] + nums[left]:
            right-=1
        else:
            return [left, right]