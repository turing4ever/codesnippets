import dis
import pytest
import asyncio

def test_async_import():
    # use pip to install pytest-asyncio
    # ************************************
    import pytest_asyncio



@pytest.mark.asyncio
async def test_async():
    # Write a coroutine, add2, that accepts two parameters,
    # adds them, then calls ``asyncio.sleep(0)``.
    # Finally it returns the sum.
    # ************************************
    async def add2(a1, a2):
        sum = a1 + a2
        await asyncio.sleep(0)
        return sum

    res = await add2(2, 3)
    assert res == 5
    code = dis.Bytecode(add2)
    assert 'sleep' in code.dis()

    # Write a coroutine, avg, that accepts two parameters,
    # ``coroutines`` and ``size``.
    # It loops over coroutines and
    # gets values from them. When
    # it has pulled out size values,
    # it returns the average of those
    # values.
    # (Make sure you put an await call in it)
    # ************************************
    async def avg(coroutines, size):
        sum = 0
        for c in coroutines[:size]:
            sum += await c
        return sum/size

    res3 = await avg([add2(1, 3),
                     add2(1, 4),
                     add2(1, 6),
                     ], 2)
    assert res3 == 4.5


if __name__ == '__main__':
    import pytest
    pytest.main([__file__])
