pre_fix = "PREFIX"


def encode(original_key: int) -> str:
    """
    original: current use for a auto increment id
    generate a 6 bit random digital str
    return: str(ints)
    """
    t_string = '7083416592'
    key_len = 6
    total_str = t_string
    str_len = len(total_str)
    new_key = ""
    for _ in range(key_len):
        tmp_index = original_key % str_len
        original_key = int(original_key / str_len)
        new_key = "{}{}".format(total_str[tmp_index], new_key)
    return new_key


def gen_cn(s_code: str) -> str:
    """
    generate a big check bit number
    :return check number
    """
    i = 1
    tmp_sum = 0
    for num in s_code:  # number 为0-9
        if 0 == i % 2:
            tmp = int(num) * 2 % 10  # tmp 这种
        else:
            tmp = int(num) * 3 % 10
        tmp_sum += tmp
        i += 2
    if 0 == tmp_sum % 10:
        bit = 0
    elif tmp_sum > 100:
        bit = 10 - tmp_sum % 100 % 10
    else:
        bit = 10 - tmp_sum % 10
    return str(bit)


def check_cn(code_str: str) -> bool:
    """"""
    original_num = code_str[:-1]
    return code_str[-1] == gen_cn(original_num)


def check_code(issue_code: str) -> bool:
    prefix = "PREFIX"  # TODO: global config
    if issue_code[:6] != prefix:
        return False
    tail = issue_code[6:]
    if len(tail) != 8:
        return False
    real_code = tail[0] + tail[1] + tail[2] + tail[4] + tail[6] + tail[7]
    return check_cn(real_code + tail[3]) or check_cn(real_code + tail[3] + tail[5])


def str_ins(s: str, ins: str, index: int) -> str:
    """ insert a char into a immutable string
        index start of 0
    """
    return s[:index] + ins + s[index:]


def gen_code(issue_id) -> str:
    code = encode(issue_id)

    return "PREFIX" + str_ins(str_ins(code, gen_cn(code), 3), gen_cn(code + gen_cn(code)), 5)


if __name__ == '__main__':
    d = dict()
    for i in range(1000000):
        if d.get(i) is None:
            co = gen_code(i)
            d[i] = co
            print(co)
            res = check_code(co)
            if not res:
                print("check code error: ", co)
                break
        else:
            print("duplicate key:", i)
            break
