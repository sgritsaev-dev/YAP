"""ID 114608683"""


def decoder(encoded_msg: str) -> str:
    """
    Decodes the string.
    >>> decoder('2[cp]3[a2[b]c]g')
    'cpcpabbcabbcabbcg'
    """
    result = []
    for i in range(len(encoded_msg)):
        if encoded_msg[i] != ']':
            result.append(encoded_msg[i])
        else:
            substring = ''
            while result[-1] != '[':
                substring = result.pop() + substring
            result.pop()

            multiplier = ''
            while result and result[-1].isdigit():
                multiplier = result.pop() + multiplier
            result.append(int(multiplier)*substring)
    return ''.join(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(decoder(input()))
