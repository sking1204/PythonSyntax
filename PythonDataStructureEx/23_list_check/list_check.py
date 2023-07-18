def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for list_el in lst:
        if not isinstance(list_el,list):
            return False
    return True


    
   
   
   
  # Question for mentor, why doesn't this approach work?
  #  
    # for item in lst:
    #     if isinstance(item, list):
    #         return True
    
    # return False
   

   


