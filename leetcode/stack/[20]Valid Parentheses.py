# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  Every close bracket has a corresponding open bracket of the same type. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of parentheses only '()[]{}'. 
#  
# 
#  Related Topics String Stack 👍 22636 👎 1563


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        stack_dict = {')': '(', '}': '{', ']': '['}

        def check(stack_list, w):
            if stack_list[-1] != stack_dict[w]:
                return False
            else:
                stack_list.pop(-1)
                return True

        stack_list = []
        for w in list(s):
            if w in stack_dict.values():
                stack_list.append(w)
            if stack_list != []:
                if w in stack_dict.keys():
                    rst = check(stack_list, w)
                    if not rst:
                        return False
            else:
                return False
        if stack_list == []:
            return True
# leetcode submit region end(Prohibit modification and deletion)
