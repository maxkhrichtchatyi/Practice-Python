if __name__ == '__main__':
    items = [1, 2, 5, 24, 26, 30]
    divisor = 12

    for item in items:
        if item % divisor == 0:
            found = item
            break
    else:
        items.append(divisor)
        found = divisor

    print('{items} contains {found} with is multiple of {divisor}'.format(**locals()))
