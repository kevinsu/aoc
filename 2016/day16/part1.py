import sys
from common.perf import profiler


@profiler
def main(argv):
    input = '00111101111101000'
    target_length = 35651584
    a = get_array_from_input(input)
    while len(a) < target_length:
        b = process_input(a)
        a = a + [False] + b
    print(get_checksum(a[:target_length]))


def get_array_from_input(input):
    return list(map(lambda x: x == '1', list(input)))

def process_input(input):
    b = input.copy()
    b.reverse()
    return list(map(lambda x: not x, b))

def get_string_output(input):
    return ''.join(map(lambda x: '1' if x else '0', input))

def get_checksum(input):
    checksum = input
    while len(checksum) % 2 == 0:
        new_checksum = []
        for i in range(0, len(checksum), 2):
            new_checksum.append(checksum[i] == checksum[i+1])
        checksum = new_checksum
    return get_string_output(checksum)


if __name__ == "__main__":
    main(sys.argv[1:])
