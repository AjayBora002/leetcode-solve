n = [1, 1, 2, 2, 3, 4, 5, 6, 6]
y = [1, 2, 3, 4, 5]
f = {}

# Fix 1: Loop directly over the items, not the range
for item in n:
    if item in f:
        f[item] += 1
    else:
        f[item] = 1

# f is now {1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 2}

for j in y:
    if j in f:
        # Fix 2: Use 'j' (the current item), not 'i'
        print(f"Number {j} appears {f[j]} times")





from collections import Counter

n = [1, 1, 2, 2, 3, 4, 5, 6, 6]
y = [1, 2, 3, 4, 5]

# This one line does all the counting logic for you
f = Counter(n) 

# Print results
for j in y:
    print(f"{j}: {f[j]}")



