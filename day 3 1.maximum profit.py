def count_good_pairs(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                count+=1
    return count
print(count_good_pairs([10,22,5,75,65,80]))
