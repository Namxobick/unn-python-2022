import math


def call_system_exit():
    try:
        exit()
    except SystemExit:
        print('SystemExit')


def call_generator_exit():
    def generate():
        values = [0, 1]
        for value in values:
            try:
                yield value

            except GeneratorExit:
                print('GeneratorExit')
                raise

    my_generator = generate()
    next(my_generator)
    my_generator.close()


def call_runtime_error():
    def generate():
        values = [0, 1]
        for value in values:
            try:
                yield value

            except RuntimeError:
                print('RuntimeError')

    my_generator = generate()
    next(my_generator)
    my_generator.close()


def call_stop_iteration():
    def generate():
        for value in [0]:
            yield value
        return

    my_generator = generate()
    for i in range(2):
        try:
            next(my_generator)
        except StopIteration:
            print("StopIteration")


def call_overflow_error():
    results = []
    for i in range(1000):
        try:
            results.append(math.exp(i))
        except OverflowError:
            print("OverflowError")
            return


def call_zero_division_error():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("ZeroDivisionError")


def call_assertion_error():
    try:
        assert 0 == 1
    except AssertionError:
        print("AssertionError")


def call_attribute_error():
    my_str = 'my'
    try:
        my_str.noattr
    except AttributeError:
        print("AttributeError")


def call_value_error():
    try:
        chr(-100)
    except ValueError:
        print("ValueError")


def call_index_error():
    a = []
    try:
        a[1]
    except IndexError:
        print("IndexError")


def call_key_error():
    my_dict = {0: 0}
    try:
        my_dict[1]
    except KeyError:
        print("KeyError")


def call_file_not_found_error():
    try:
        f = open('')
    except FileNotFoundError:
        print('FileNotFoundError')


def call_memory_error():
    try:
        x = list(range(10000000000))
    except MemoryError:
        print('MemoryError')


def call_type_error():
    try:
        x = 'a' + 5
    except TypeError:
        print('TypeError')


def call_recursion_error():
    try:
        call_recursion_error()
    except RecursionError:
        print('RecursionError')


def call_unicode_decoder_error():
    try:
        b'\xd0'.decode('utf-8')
    except UnicodeDecodeError:
        print('UnicodeDecodeError')


call_system_exit()
call_generator_exit()
call_runtime_error()
call_stop_iteration()
call_overflow_error()
call_zero_division_error()
call_assertion_error()
call_attribute_error()
call_value_error()
call_index_error()
call_key_error()
call_file_not_found_error()
call_memory_error()
call_type_error()
call_recursion_error()
call_unicode_decoder_error()
