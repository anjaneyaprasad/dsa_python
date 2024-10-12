
def output_bool(argument):
    if argument is None:
        sys.stderr.write("Return value contains None where boolean is expected")
        exit()
    if type(argument) is not bool:
        sys.stderr.write(f"Return value contains {type(argument).__name__} '{argument}' where boolean is expected")
        exit()
    sys.stdout.write(f'{int(argument)}')


def output_list_bool(argument):
    if argument is None:
        sys.stderr.write("Return value contains None where list is expected")
        exit()
    if type(argument) is not list:
        sys.stderr.write(f"Return value contains {type(argument).__name__} '{argument}' where list is expected")
        exit()
    count = 0
    sys.stdout.write('[')

    for i in argument:
        output_bool(i)
        if count < len(argument) - 1:
            sys.stdout.write(',')
            sys.stdout.write(' ')
        count = count + 1

    sys.stdout.write(']')


def output_list_list_bool(argument):
    if argument is None:
        sys.stderr.write("Return value contains None where list is expected")
        exit()
    if type(argument) is not list:
        sys.stderr.write(f"Return value contains {type(argument).__name__} '{argument}' where list is expected")
        exit()
    count = 0
    sys.stdout.write('[')
    sys.stdout.write('\n')

    for i in argument:
        output_list_bool(i)
        if count < len(argument) - 1:
            sys.stdout.write(',')
        count = count + 1
        sys.stdout.write('\n')

    sys.stdout.write(']')


def input_int32(data):
    argument = int(data)
    return argument


def input_list_int32(data):
    argument = []
    for json_array_item in data:
        argument.append(input_int32(json_array_item))
    return argument


def input_list_list_int32(data):
    argument = []
    for json_array_item in data:
        argument.append(input_list_int32(json_array_item))
    return argument


if __name__ == '__main__':
    try:
        data = json.load(sys.stdin)
        n = input_int32(data['n'])
        edges = input_list_list_int32(data['edges'])
    except Exception as ex:
        sys.stderr.write('reading-input-failed-json\n')
        traceback.print_exc()
        raise ex

    original_out = sys.stdout
    sys.stdout = sys.stderr
    result = convert_edge_list_to_adjacency_matrix(n, edges)
    sys.stdout = original_out
    output_list_list_bool(result)
    sys.stdout.write('\n')
