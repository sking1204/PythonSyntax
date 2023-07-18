def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

##Ask Mentor for help understanding sprinboard solution:
##Tried creating a function to convert list to tuple
## Seems to work ok. 


    diff_calculated =[]
    
    for num in nums:
        difference = goal -num

        if difference in diff_calculated:
            return(difference, num)
        
        diff_calculated.append(num)
    return ()

    list_tuple=convert_list_to_tuple(diff_calculated)

def convert_list_to_tuple(lst):
    tuple_result =()
    for el in list:
        tuple_result += (el,)
    return tuple_result


##springboard solution

    # already_visited = set()

    # for i in nums:
    #     difference = goal - i

    #     if difference in already_visited:
    #         return (difference, i)

    #     already_visited.add(i)

    # return ()


#resources: https://www.geeksforgeeks.org/python-convert-a-list-into-a-tuple/
        
