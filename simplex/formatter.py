from numpy import set_printoptions

def enable_formatting(precision=2):
    set_printoptions(precision=precision, floatmode="maxprec", suppress=True)
