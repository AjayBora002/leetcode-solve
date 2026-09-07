def flip(start, goal):
    ans = start ^ goal
    count = 0
    while ans:
        ans = ans &(ans-1)
        count+=1
    return count



def flip(start, goal):
    return (start^goal).bit_count()




