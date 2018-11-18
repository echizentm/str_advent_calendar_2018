from typing import List, Optional, Tuple


class LZ77:
    __slots__ = ['directive_list']

    def __init__(self, text: str) -> None:
        self.directive_list = self._make_directive_list(text)

    @property
    def string_attractor_list(self) -> List[int]:
        '''
        string attractor のリストを取得します
        '''
        index = 0
        string_attractor_list = []
        for begin, end, ch in self.directive_list:
            string_attractor_list.append(index)
            index += end - begin
        return string_attractor_list

    def factorize(self) -> List[str]:
        '''
        元のテキストを factor のリストにしたものを返します
        '''
        text = ''
        factor_list = []
        for begin, end, ch in self.directive_list:
            factor = ch if ch else text[begin:end]
            factor_list.append(factor)
            text += factor
        return factor_list

    def decode(self) -> str:
        '''
        元のテキストを復元して返します
        '''
        return ''.join(self.factorize())

    def _make_directive_list(self, text: str) -> List[Tuple[int, int, Optional[str]]]:
        directive_list: List[Tuple[int, int, Optional[str]]] = []
        begin = 0
        while begin < len(text):
            index = begin
            subtext = text[begin]
            ch: Optional[str] = text[begin]
            for end in range(begin + 1, len(text) + 1):
                new_subtext = text[begin:end]
                new_index = text.find(new_subtext)
                if new_index == -1 or new_index + len(new_subtext) > begin:
                    break

                index = new_index
                subtext = new_subtext
                ch = None

            directive_list.append((index, index + len(subtext), ch))
            begin += len(subtext)

        return directive_list


if __name__ == '__main__':
    text = 'CDABCCDABCCA'
    lz77 = LZ77(text)

    print('text: {}'.format(text))
    print('is_valid: {}'.format(lz77.decode() == text))
    print('factor_list: {}'.format(lz77.factorize()))
    print('directive_list: {}'.format(lz77.directive_list))
    print('string_attractor_list: {}'.format(lz77.string_attractor_list))
