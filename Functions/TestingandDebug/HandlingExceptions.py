def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    """Option 1: Flag the Error by printing a message"""
    # try:
    #     return sum(grades)/len(grades)
    # except ZeroDivisionError:
    #     print('warning: no grades data')

    # return sum(grades)/len(grades)

    """Option 2: Change the Policy"""
    # try:
    #     return sum(grades)/len(grades)
    # except ZeroDivisionError:
    #     print('warning: no grades data')
    #     return 0.0

    """Option 3: AssertionError"""
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)

class_list = [[['peter', 'parker'], [10.0, 70.0, 85.0]],
             [['bruce',' wayne'], [10.0, 80.0, 74.0]],
             [['caption','america'], [80.0, 10.0, 96.0]],
             [['deadpool'], []]]

        
print(get_stats(class_list))