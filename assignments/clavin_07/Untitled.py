#Author: Andrew Clavin

#7.2.9 pg 339

def decayC14(originalAmount, years, dt):
    """
    Precondition: originalAmount is an integer
    and years is a positive integer
    and dt is an integer and is not zero

    Postcondition: amount is an integer
    """
    assert years > 0, 'Years must be more than zero'
    assert isinstance(originalAmount, int), 'Original amount must be an integer'
    assert dt != 0, 'dt cannot be zero'
    amount = originalAmount
    k = -0.0012096809434
    numIterations = int(years / dt) + 1
    for i in range(1, numIterations):
        amount = amount + k * amount * dt
    return amount
