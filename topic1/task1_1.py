def get_max_and_min(data: typing.Set) -> collections.namedtuple:
    """Get a set of float(ex: 231.2312) and str data("1 \ 5" or "3.00000003") ->
     return namedtuple with attribute .max_value and .min_value """
    buff = list()
    for el in data:
        if type(el) is float:
            buff.append(el)
        elif type(el) is str:

            if '\\' in el:
                numerator_and_denominator = el.split('\\')
                num = fractions.Fraction(int(numerator_and_denominator[0].strip()),
                                         int(numerator_and_denominator[1].strip()))
                buff.append(num)
            else:
                num = decimal.Decimal(el)
                buff.append(num)
    min_val = min(buff)
    max_val = max(buff)
    min_max_tuple = collections.namedtuple('min_max_tuple', ['min_value', 'max_value'])
    result = min_max_tuple(min_val, max_val)
    return result
