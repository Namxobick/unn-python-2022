class Array(object):

    def __init__(self, *args):
        self._data = args

    def __str__(self):
        return str(self._data)

    def __add__(self, other):
        if not isinstance(other, Array):
            print(f"Warning, expected type Array (type {other} is {type(other)})")
            new_array = Array(*self._data, other)
        else:
            new_array = Array(*self._data, *other._data)
        return new_array

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, item: int):
        if not isinstance(item, int):
            print(f"Error, expected type int (type {item} is {type(item)})")
        elif item < -len(self._data) or item >= len(self._data):
            print("Error,index out of range")
        else:
            return self._data[item]
        return

    def __setitem__(self, key: int, value):
        if not isinstance(key, int):
            print(f"Error, expected type int (type {key} is {type(key)})")
            return

        if key < 0:
            key = len(self) + key

        if key < 0 or key >= len(self):
            print("Error, index out of range")
            return

        self._data = Array(*self._data[:key], value, *self[key + 1:])

    def __eq__(self, other):
        if not isinstance(other, Array):
            return False
        if self._data == other._data:
            return True
        else:
            return False

    def append(self, new_element):
        self._data = Array(*self._data, new_element)

    def index(self, searched_element):
        try:
            return self._data.index(searched_element)
        except ValueError:
            return -1