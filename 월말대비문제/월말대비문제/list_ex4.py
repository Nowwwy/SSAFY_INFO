# append는 뒤에 붙이기, pop은 맨뒷요소 제거 
nums = []
nums.append(100)
print(nums) # [100]
nums.append(50) 
print(nums) # [100, 50]

nums.append(1) 
nums.append(2) 
nums.append(3) 
nums.append(4) 
nums.append(5) # [100, 50, 1, 2, 3, 4, 5]
print(nums)
num = nums.pop()  # 맨마지막요소 제거 및 반환
print(num) # 5
print(nums) # [100, 50, 1, 2, 3, 4]

num = nums.pop(0)  # 맨마지막요소 제거 및 반환
print(nums)  # [50, 1, 2, 3, 4]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:    # 반복문 돌면서 원본 배열 바꾸면...계산이 안됩니다..어려워
    print(num)
    nums.pop(0)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(nums)):    # 반복문 돌면서 원본 배열 바꾸면...계산이 안됩니다..어려워
    print(nums[i])
    nums.pop(0)



