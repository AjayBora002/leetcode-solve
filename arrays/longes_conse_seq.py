def cons(nums):
    if not nums:
        return 0
    set_nums = set(nums)
    long_streak = 0
    for i in set_nums:
        if i-1 not in set_nums:
            curr_nums = i
            curr_streak = 1
            while curr_nums+1 in set_nums:
                curr_nums+=1
                curr_streak+=1
                long_streak=max(curr_streak, long_streak)
    return long_streak

nums=[1,2,3,4,500,6000,5]
a = cons(nums)
print(a)






