import os


def check_str_by_regex(regex):
    import re
    pattern = re.compile(regex)
    return lambda string: pattern.match(string) != None


def is_bool(string):
    if string == 'true' or string == 'True' or string == 'yes' or string == 'y' or string == 'Yes':
        return True
    elif string == 'false' or string == 'False' or string == 'no' or string == 'No' or string == 'n':
        return False
    raise ValueError


is_letters_only = is_words_only = check_str_by_regex("^[A-Za-z]+$")

is_words_only = check_str_by_regex("^([A-Za-z]+ )+\w+$")

is_float = check_str_by_regex("^\d+[.]\d+$")

is_int = check_str_by_regex("^0$|^[1-9]\d+$")


class ConditionError(Exception):
    pass


def while_input_for(converter):
    def while_loop(message, more_conditions_func):
        checker = False
        while checker is False:
            try:
                input_from_user = input(message)
                converted_input = convert(input_from_user)
                if more_conditions_func is not None:
                    result = more_conditions_func(converted_input)
                    if result is not True:
                        raise ConditionError
                checker = True
                return converted_input
            except ValueError:
                print(f'this input is not an instance of {converter.__name__} object:{input_from_user}')
            except ConditionError:
                print('This input does not meet all the required conditions ')

    try:
        convert = converter
    except ValueError:
        print(f'does not recognize {converter} as type')

    return while_loop


int_input = while_input_for(int)
bool_input = while_input_for(is_bool)
float_input = while_input_for(float)

SCORES_FILE_NAME = 'Scores.txt'
