def sum_floats(nums,default=0):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    res = []

    for num in nums:
        if isinstance(num,float):
            res.append(num)
    for el in res:
        return sum(res)
    return 0
    
    

        
  
#springboard solution:

    # return sum([num for num in nums if isinstance(num,float)])
    
