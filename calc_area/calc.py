from calc_area.settings import FIGURES as FIGS


def calc_area(figure, data):
    match figure:
        case 'guess':
            figs = [x for x in FIGS if FIGS[x]['data']['count'] == len(data)]

            strs = []
            for fig in figs:
                result = FIGS[fig]['calc'].calc_area(*data)
                if not isinstance(result, str):
                    result = round(result, ndigits=2)
                text = f"\tit could be a '{fig}', with "\
                       f"{FIGS[fig]['data']['name']} "\
                       f"{', '.join([str(x) for x in data])}, "\
                       f"and its area is equal to '{result}'"
                strs.append(text)
            return '\n' + '\n'.join(strs)

        case _:
            return FIGS[figure]['calc'].calc_area(*data)
