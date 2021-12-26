def get_stats(class_list):
    new_stats = []
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats

def avg(grades):
    return sum(grades)/len(grades)

class_list = [[['peter', 'parker'], [80.0, 70.0, 85.0]],
             [['bruce',' wayne'], [100.0, 80.0, 74.0]]]

        
print(get_stats(class_list))