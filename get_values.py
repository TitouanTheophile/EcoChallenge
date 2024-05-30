config = {
    "sum": {

    },
    "hex": {

    },
    "abs": {
        "nb_exec": 2,
        "scenarios": [
            {"x": 1},
            {"x": 10},
            {"x": -10},
            {"x": 20}
        ]
    },
    "len": {

    },
    "divmod": {

    },
    "enumerate": {

    },
}

builtin_list = ['sum', 'hex', 'abs', 'len', 'divmod', 'enumerate']


def main():
    for builtin in builtin_list:
        results = {
            'joule_ram': [],
            'joule_cpu': [],
        }

        builtin_scenarios = config[builtin]

        custom_builtin_path = f'custom/{builtin}.py'
        original_builtin_path = f'custom/{builtin}.py'



