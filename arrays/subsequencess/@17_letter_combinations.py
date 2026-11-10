

# 17. Letter Combinations of a Phone Number


# Example 1:

# Input:
# digits = "23"

# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input:
# digits = "2"

# Output: ["a","b","c"]

def letter(digits):
  phone = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
  }
  r =[]
  def combina(index, subset):
    if index == len(digits):
      r.append("".join())
      return 
    letters = phone[digits[index]]
    for ch in letters:

      subset.append(ch)
      combina(index+1, subset)
      subset.pop()
    combina(0, [])
    return r