def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
# use a dictionary so we can keep track of key value pairs
## return count so we can see what the dictionary looks like
## then return num to show the number that has the highest count
    count ={}

    for num in nums:
        count[num] = count.get(num,0) + 1

    most_frequent = max(count.values()) 

                    
    
    for(num,freq) in count.items():
        if freq == most_frequent:
            # return count
            return num
        

##Research: how can I return num has count of (whatever count is of the key value pair) using an f string?
        

   
             
