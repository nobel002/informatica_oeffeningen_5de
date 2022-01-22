def shift(array, spaces: int = 1):  # Shifts an array spaces spaces to the right AND wraps around
    return [array[(i + spaces) % len(array)] for i, _ in enumerate(array)]


# Last suitcase has index  √
# Suitcase is dropped on the third empty space of the carrousel √
# Shift the array
def carousel(carousel_length, sequence):
    bagage_carousel = [None for _ in range(carousel_length)]
    empty_spaces = 2
    while sequence != '':
        if bagage_carousel[0] is None and empty_spaces >= 2:
            bagage_carousel[0] = sequence[:1]
            sequence = sequence[1:]
            empty_spaces = 0
        elif bagage_carousel[0] is None and empty_spaces < 2:
            empty_spaces += 1
        bagage_carousel = shift(bagage_carousel)
    return shift(bagage_carousel, -1)


def rotated(carousel_a, carousel_b):
    if len(carousel_a) == len(carousel_b):
        for i in range(len(carousel_a)):
            if carousel_a == shift(carousel_b, i):
                return True
    return False


#Testing
if __name__ == "__main__":
    print("---TESTING---")
    print("--shifting--")
    expected_output = ["B", "C", "A"]
    received_output = shift(['A', 'B', 'C'])
    if expected_output != received_output:
        raise Exception(f'TEST FAILED: expected {expected_output} but received {received_output}')
    else:
        print("PASSED")

    print("---carousel---")
    expected_output = ['E', 'A', None, 'D', 'B', None, None, 'C']
    received_output = carousel(8, 'ABCDE')

    if expected_output != received_output:
        raise Exception(f'TEST FAILED: expected {expected_output} but received {received_output}')
    else:
        print("PASSED")

    expected_output = ['E', 'C', 'B', 'D', 'A']
    received_output = carousel(5, 'ABCDE')

    if expected_output != received_output:
        raise Exception(f'TEST FAILED: expected {expected_output} but received {received_output}')
    else:
        print("PASSED")

    print('---rotated---')
    expected_output = True
    received_output = rotated(['E', 'A', None, 'D', 'B', None, None, 'C'], ['B', None, None, 'C', 'E', 'A', None, 'D'])

    if expected_output != received_output:
        raise Exception(f'TEST FAILED: expected {expected_output} but received {received_output}')
    else:
        print("PASSED")

    expected_output = False
    received_output = rotated(['E', 'A', None, 'D', 'B', None, None, 'C'], ['B', None, None, 'A', 'E', 'C', None, 'D'])

    if expected_output != received_output:
        raise Exception(f'TEST FAILED: expected {expected_output} but received {received_output}')
    else:
        print("PASSED")

    expected_output = False
    received_output = rotated(['E', 'A', None, 'D', 'B', None, None, 'C'], ['C', 'E', 'A', None, 'D', 'B'])

    if expected_output != received_output:
        raise Exception(f'TEST FAILED: expected {expected_output} but received {received_output}')
    else:
        print("PASSED")
