from typing import Sequence
from .lz77 import LZ77


def is_string_attractors(
    text: str, index_list: Sequence[int]
) -> bool:
    '''
    index_list が指すインデックス集合が
    text の string attractors になっているかどうかを判定します
    '''
    return all([
        matches_any_string_attractors(text, index_list, text[begin:end])
        for begin in range(len(text))
        for end in range(begin + 1, len(text) + 1)
    ])


def matches_any_string_attractors(
    text: str, index_list: Sequence[int], subtext: str,
) -> bool:
    '''
    subtext にマッチする text の部分文字列のうちのいずれかに
    index_list が指すインデックスのいずれかが
    含まれているかどうかを判定します
    '''
    begin = 0
    while True:
        index = text[begin:].find(subtext)
        if index == -1:
            return False

        begin = begin + index
        end = begin + len(subtext)
        if any([index in range(begin, end) for index in index_list]):
            return True

        begin += 1


def print_string_attractors(
    text: str, index_list: Sequence[int]
) -> None:
    '''
    string attractor の位置の文字を [] で囲んで text を表示します
    '''
    print(''.join([
        f'[{ch}]' if index in index_list else ch
        for index, ch in enumerate(text)
    ]))


if __name__ == '__main__':
    text = 'CDABCCDABCCA'
    sa_list = [3, 6, 10, 11]
    print_string_attractors(text, sa_list)
    print('is_valid: {}'.format(is_string_attractors(text, sa_list)))

    text_list = [
        'abracadabra',
        'みるみるミルキィ',
        'ケアルケアルラケアルダケアルガケアルジャ',
        '働きたくない私は働きたくない私の働きたくない気持ちを大切にして働きたくない',
    ]

    for text in text_list:
        sa_list = LZ77(text).string_attractor_list
        print_string_attractors(text, sa_list)
        print('is_valid: {}'.format(is_string_attractors(text, sa_list)))
