from camera.camera import Sample


def my_sum(x,y):
    """print:hahhaaS

    Parameters:
    ----------
    x : int
        operand1 of addition
    y : int
        operand2 of addition

    Returns:
    ----------
    int
        sum of x and y
    """
    print(x+y)

# main関数
if __name__ == '__main__':
    out = my_sum(1,2)
    print(out)