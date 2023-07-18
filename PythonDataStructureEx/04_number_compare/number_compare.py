def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """

    ##first attempt
    # if a==b:
    #     return "Numbers are equal"
    # if a < b:
    #     return "Second is greater"
    # if a > b:
    #     return "First is greater"

    ##It's better to use if, elif, else format:

    if a < b:
        return "Second is greater"
    elif a > b:
        return "First is greater"
    else:
        return "Numbers are equal"