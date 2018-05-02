def test():
    # Get the contents of the current directory
    # using the ``path`` module.
    # Store the results in ``cur``.
    # ***********************************
    from pathlib import Path
    p = Path('.')
    cur = p.glob('*')
    assert 'path_test.py' in list(map(str,cur))

    # Make a path with a file named ``test.txt``
    # Store it in ``test_file``.
    # ***********************************

    test_file = Path('test.txt')
    assert test_file.suffix == '.txt'

    # Write 'hello world' to
    # the test_file.
    # ***********************************

    with open(test_file, 'w') as f:
        f.write('hello world')
    assert test_file.exists()
    assert test_file.name == 'test.txt'
    with test_file.open() as fin:
        assert 'hello world' in fin.read()

    # Delete test_file
    # ***********************************
    test_file.unlink()
    assert not test_file.exists()



if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

