nums = [3, 12, 45, 7, 23, 56, 89, 34]
# 최소값과 최대값 찾기 
# 리스트 요소 접근하기
# 반복문으로 접근가능
# [7] [3] [1] [8] [2] [3]
8
for num in nums:
    print(num,end=' ') # 12 45 7 23 56 89 34 
print()

max_num = nums[0]
min_num = nums[0]
for i in range(len(nums)):   # 여러개가 있는데 하나씩 보는 반복문
    # print(nums[i],end=' ')
    if max_num < nums[i]:  # 현재 숫자가 내가 알고 있는 최대값 보다 크면 바꿔라
        max_num = nums[i]
    elif min_num > nums[i]: # 현재 숫자가 내가 알고 있는 최솟값 보다 작으면 바꿔라
        min_num = nums[i]

print(max_num)
print(min_num)
