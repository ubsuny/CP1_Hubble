def get_vals(data):
    """This function takes the data set generated from the
    numpy genfromtxt function of the three desired columns
    and returns a list of three lists: the times, CH4 levels,
    and uncertainties.

    Parameters:

    data: numpy.ndarry

        The set of data that you wish to rearrange into a list of its
        columns in each list.

    Returns:

    master_list: list

        A list containing a list for each column in the inputed data set
        with the elements of said column.

    """
    time_list = []
    inc_list = []
    master_list = []
    for i in data:
        time_list.append(i[0])
        inc_list.append(i[1])
    master_list.append(time_list)
    master_list.append(inc_list)
    return master_list


def computeSigma(x_list, y_list):
    """"Takes a list of x and y values. Returns the sigma squared value,
    the a value, and the b value for the data set
    
    Parameters:

    x_list: List

        List of x values for the fit

    y_list: List

        List of y values for the fit

    Returns:

    returnList: List

        A list containing a, b, and sigma^2, the fit parameters

    """
    x_length = len(x_list)
    y_length = len(y_list)
    s_x = 0
    s_y = 0
    s_xx = 0
    s_xy = 0
    sigma2 = 0
    if x_length != y_length:
        print("Error: X and Y lengths not equal")
        return None
    n = x_length
    if n < 2:
        print("Error: Not enough data points")
        return None
    for i in range(0, n):
        s_x += x_list[i]
        s_y += y_list[i]
        s_xx += x_list[i]**2
        s_xy += x_list[i]*y_list[i]
    den = n * s_xx - s_x*s_x
    if abs(den) < 0.0000001:
        print("Error: Denominator is zero")
        return None
    a = (s_xx * s_y - s_x * s_xy) / den
    b = (n*s_xy - s_x * s_y) / den
    for i in range(0, n):
        sigma2 += (y_list[i] - (a*x_list[i]+b))**2
    sigma2 = sigma2 / (n-2)
#    print(s_x, s_y, s_xx, s_xy, n,a,b,sigma2)
    returnList = []
    returnList.append(sigma2)
    returnList.append(a)
    returnList.append(b)
    return returnList