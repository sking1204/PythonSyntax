def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    true_list =[]

    for el in lst:
        if el:
            true_list.append(el)

    return true_list


## Sprinboard Solution (shorter):

    # return [val for val in lst if val]