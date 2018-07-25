def get_ratios(vect1, vect2):
    """Assumes : vect1 and vect2 are equal lenght lists of numbers.
       Returns: s list containing the meaningful values of vect1[1]/vect2[2]."""
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad arguments')
    return ratios


def get_ratios_without_exception(vect1, vect2):
    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError('get_ratios called with bad arguments')
    for index in range(len(vect1)):
        vect1elem = vect1[index]
        vect2elem = vect2[index]
        if (type(vect1elem) not in (int, float)) \
            or (type(vect2elem) not in (int, float)):
            raise ValueError('get_ratios called with bad arguments')
        if vect2elem == 0.0:
            ratios.append(float('nan'))
        else:
            ratios.append(vect1elem/vect2elem)
    return ratios


def test_get_ratios():
    try:
        print(get_ratios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0]))
        print(get_ratios([], []))
        print(get_ratios([1.0, 2.0], [3.0]))
    except ValueError as msg:
        print(msg)


test_get_ratios()
