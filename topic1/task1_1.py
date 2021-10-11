def get_max_and_min(data: typing.Set[typing.Union[decimal.Decimal,
                                                  fractions.Fraction]]) -> collections.namedtuple:
    """Get a set of float(ex: 231.2312) and str data("1 \ 5" or "3.00000003") ->
     return namedtuple with attribute .max_value and .min_value """
    buff = list()
    for el in data:
        if isinstance(el, float):
            buff.append(el)
        elif isinstance(el, str):
            if '\\' in el:
                numerator_and_denominator = el.split('\\')
                num = fractions.Fraction(
                    int(numerator_and_denominator[0].strip()),
                    int(numerator_and_denominator[1].strip()))
                buff.append(num)
            elif '.' in el:
                num = decimal.Decimal(el)
                buff.append(num)
            else:
                pass
        else:
            pass
    min_val = min(buff)
    max_val = max(buff)
    min_max_tuple = collections.namedtuple('min_max_tuple',
                                           ['max_value', 'min_value'])
    result = min_max_tuple(max_val, min_val)
    return result

# if __name__ == '__main__':
#     data = {
#         1.21312,
#         32.231,
#         23.41,
#         1.0,
#         "1 \ 4",
#         "1 \\ 2",
#         "1 \ 1",
#         "20.13",
#         "23.231",
#         "100.00",
#         "131.123",
#     }
#     test = get_max_and_min(data)
#     print(test.min_value)
#     print(test.max_value)
