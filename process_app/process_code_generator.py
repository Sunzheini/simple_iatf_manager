def display_processes_formatter(info):
    result = []
    for i in info:
        result.append(i[0])
    return result


def specific_results_formatter(info):
    result = ''
    for i in info:
        result += i[0] + '\n'
    return result.strip()

