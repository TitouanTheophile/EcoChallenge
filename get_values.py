from config.config import conf as config
import vjoule_handler
import pandas as pd

#builtin_list = ['sum', 'hex', 'abs', 'len', 'divmod', 'enumerate', 'maps', 'filter', 'zip']
builtin_list = ['hex']


def main():
    for builtin in builtin_list:
        results = {
            "cpu_original": [],
            "cpu_custom": [],
            "ram_original": [],
            "ram_custom": [],
            "total_original": [],
            "total_custom": [],
        }

        builtin_scenarios = config[builtin]

        for scenario in builtin_scenarios:
            custom_builtin_path = f'custom/{builtin}.py'
            original_builtin_path = f'custom/{builtin}.py'

            cpu_original = []
            cpu_custom = []
            ram_original = []
            ram_custom = []
            total_original = []
            total_custom = []

            for i in range(5):
                custom_joule_results = vjoule_handler.eval_python(
                    filepath=custom_builtin_path,
                    *scenario
                )
                original_joule_results = vjoule_handler.eval_python(
                    filepath=original_builtin_path,
                    *scenario
                )
                cpu_original.append(original_joule_results['CPU'])
                cpu_custom.append(original_joule_results['CPU'])
                ram_original.append(original_joule_results['RAM'])
                ram_custom.append(original_joule_results['RAM'])
                total_original.append(original_joule_results['total'])
                total_custom.append(original_joule_results['total'])

            results['cpu_original'].append(cpu_original)
            results['cpu_custom'].append(cpu_custom)
            results['ram_original'].append(ram_original)
            results['ram_custom'].append(ram_custom)
            results['total_original'].append(total_original)
            results['total_custom'].append(total_custom)

            results_path = f'output/{builtin}.csv'

            df = pd.DataFrame(results, index=[f'scenario_{i}' for i in range(1, 6)])
            df.to_csv(results_path, index=False)


if __name__ == '__main__':
    main()
