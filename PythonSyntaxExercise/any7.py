#Approach 1:

def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    for num in nums:
        if num ==7:
            return('should be true')
    else:
        return('should be false')
        
#Approach 2:


def any7_2(nums):
    """Are any of these numbers a 7? (True/False)"""

    for num in nums:
        if num == 7:
            return True

    return False