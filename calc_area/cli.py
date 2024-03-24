import prompt
from rich import print
from calc_area.settings import FIGURES, COUNTS


def what_figure():
    figures = [f"'{x} ({FIGURES[x]['abbr']})'" for x in FIGURES.keys()]
    question = f"[cyan]The area of which figure we will calculate?\n"\
               f"Supported figures:[/cyan] {' / '.join(figures)}\n"\
               f"If select 'guess', let's try to determine "\
               f"the figure from the input data"
    print(question)
    figure = prompt.string("Enter figure: ")

    if figure in FIGURES:
        return figure

    elif len(figure) in (1, 2):
        for key in FIGURES:
            if FIGURES[key]['abbr'] == figure:
                return key

    print('[yellow]Not supported figure! Try again!\n')
    return what_figure()


def what_data(figure):
    data_block = FIGURES[figure]['data']
    if data_block['count'] > 1:
        supp = f"{data_block['count']} "
    else:
        supp = ''

    data = " ".join(
        prompt.string(f"Enter {supp}{data_block['name']}: ").split()
    )
    try:
        data = [float(x) for x in data.split()]

        if figure != 'guess'\
                and len(data) == data_block['count']:
            return data

        elif figure == 'guess'\
                and len(data) in COUNTS:
            return data

        print('[yellow]Incorrect amount of data! Try again!\n')
        return what_data(figure)

    # при вводе не числовых значений
    except ValueError:
        print('[yellow]Incorrect data! Try again!\n')
        return what_data(figure)
