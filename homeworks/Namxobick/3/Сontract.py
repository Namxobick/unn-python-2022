class ContractError(Exception):
    """We use this error when someone breaks our contract."""


#: Special value, that indicates that validation for this type is not required.
Any = object()


def contract(arg_types=None, return_type=None, raises=None):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if arg_types is not None:
                for index, arg_type in enumerate(arg_types):
                    if arg_type is not Any and arg_type != type(args[index]):
                        raise ContractError('Invalid argument type') from TypeError

            try:
                result = function(*args, **kwargs)
            except (raises if raises is not None and Any not in raises else Exception) as ex:
                raise ex
            except Exception:
                raise ContractError from Exception

            if return_type is not None and not isinstance(result, return_type):
                raise ContractError('Invalid return type') from TypeError

            return result
        return wrapper
    return decorator
