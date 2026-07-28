nums = [12, 45, 7, 23, 56, 89, 34]
# 정렬
# sorted(arg) : 내장함수 , 정렬된 리스트 반환, 원본은 바뀌지 않음
# list.sort() : 메서드, 반환값 없음, 원본이 바뀜
sorted_nums = sorted(nums)
print(sorted_nums)
print(nums)
# [7, 12, 23, 34, 45, 56, 89]
# [12, 45, 7, 23, 56, 89, 34]

result = nums.sort() # nums.sort() 만 쓰는게 맞다.
print(result)   # none
print(nums) # [7, 12, 23, 34, 45, 56, 89]



