def mean(list):
    '''
    Takes list of numbers and returns the mean
    '''
    if len(list)<=0:
        return "Empty list"
    
    total=0
    
    for item in list:
        total+=item
    return total/len(list)