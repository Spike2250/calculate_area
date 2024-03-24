#!/usr/bin/env python3
from calc_area.cli import what_figure, what_data
from calc_area.calc import calc_area
from rich import print


START_MSG = '[cyan]Welcome to "Calculate Area"!'


def starting():
    print(START_MSG)

    figure = what_figure()
    print(f'[cyan]Figure selected: [green]{figure}')

    data = what_data(figure)
    print(f'[cyan]Data accepted: [green]{";  ".join([str(x) for x in data])}')

    result = calc_area(figure, data)
    try:
        print(f'[cyan]Result: [green]{round(result, ndigits=2)}')
    except TypeError:
        print(f'[cyan]Result: [green]{result}')


def main():
    starting()


if __name__ == '__main__':
    main()
