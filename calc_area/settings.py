from calc_area.calculations import (
    triangle,
    circle,
    rectangle,
    square,
    sphere,
)


FIGURES = {
    'triangle': {
        'abbr': 'T',
        'data': {
            'name': 'sides',
            'count': 3,
        },
        'calc': triangle,
    },

    'circle': {
        'abbr': 'C',
        'data': {
            'name': 'radius',
            'count': 1,
        },
        'calc': circle,
    },

    'rectangle': {
        'abbr': 'R',
        'data': {
            'name': 'sides',
            'count': 2,
        },
        'calc': rectangle,
    },

    'square': {
        'abbr': 'Sq',
        'data': {
            'name': 'side',
            'count': 1,
        },
        'calc': square,
    },

    'sphere': {
        'abbr': 'Sp',
        'data': {
            'name': 'radius',
            'count': 1,
        },
        'calc': sphere,
    },

    'guess': {
        'abbr': 'G',
        'data': {
            'name': 'data',
            'count': 0,
        },
    },
}


COUNTS = {FIGURES[x]['data']['count'] for x in FIGURES if x != 'guess'}
