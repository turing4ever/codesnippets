def test_nums():
    # There are 102 floors in the Empire State Building.
    # If you have walked up a seventh of them, how many
    # (whole) floors have you walked up? Store the result
    # in ``floors``.
    # ***********************************
    floors = 102 // 7
    assert hex(floors) == '0xe'

    # What percentage of the floors have you climbed?
    # Store the result as a string ("53.2%") with 1
    # decimal of precision in variable ``per``
    # ***********************************
    per = f'{7/102:.1%}'
    assert per[::-1] == '%9.6'


    # I have (2^64)-1 satoshis. Can I divide them
    # wholly by 3?
    # How many would each person get? Store the
    # result in ``coins``.
    # ***********************************
    satoshis = (2**64) - 1
    coins = satoshis // 3
    
    assert coins * 3 == satoshis

    # The US population is around 326,979,681.
    # How many *whole* coins would each US
    # citizen get? Store the result in ``us_coins``
    # (Use _ to make population easier to read)
    # ***********************************
    us_coins =  satoshis // 326_979_681    
    assert us_coins == 56_415_566_916
    

    # I have .5 pumpkin pies and 1.5 apple pies.
    # I want to use Python to round the number
    # of each pie. Store the result in
    # ``pumpkin`` and ``apple``
    # ***********************************
    pumpkin = round(0.5)
    apple = round(1.5)
    assert pumpkin + apple == 2
    


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
