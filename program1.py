class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # HashMap to store the mappings of closing to opening brackets
        bracket_map = {')': '(', ']': '[', '}': '{'}
        
        # Iterate over each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop from the stack, if it's empty set top_element to a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket in the map doesn't match the top of the stack
                if bracket_map[char] != top_element:
                    return False
            else:
                # It is an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, return True, otherwise False
        return not stack






    



  

