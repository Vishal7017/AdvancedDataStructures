def get_ratios(L1, L2):
    """Assume: L1 and L2 are lists of equal lenght of numbers
       Returns: a list containinng L1[i]/L2[i]"""
    ratios = []
    for index in range(len(L1)):
        try: 
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) # nan-not a number
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios

#ZeroDivisionError
# L1 = [4, 16, 32, 64, 128]
# L2 = [3, 0, 12, 32, 12]
# print(get_ratios(L1, L2))

#ValueError
L3 = [4, 16, 32, 64, 128]
L4 = [3, 0, 12, "3", 12]
print(get_ratios(L3, L4))