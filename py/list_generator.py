# list
def leap_years_lst(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years

# generator
def leap_years_gen(n=1000000):
    for year in range(1, n+1):
        if calendar.isleap(year):
            yield year

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(leap_years_lst, number=100))
    print(timeit.timeit(leap_years_gen, number=100))

