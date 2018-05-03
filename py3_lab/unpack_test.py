
def test_unpack():
    # Unpacking
    #
    # Given the tuple, ``person``, unpack
    # the values into name, age, and country.
    # ***********************************

    person = ('Candide', 30, 'France')
    name, age, country = person
    assert (name, age, country) == ('Candide', 30, 'France')

    # Extended Unpacking
    #
    # Use unpacking to get the first letter
    # of name. Store the result in ``first``
    # ***********************************
    (first, *d), *ignore = person 
    assert first == 'C'

    # Unpack the characters from ``name`` into a
    # list called ``letters``
    # ***********************************
    (*letters,), *ignore = person
    assert letters == ['C', 'a', 'n', 'd', 'i', 'd', 'e'] 

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
