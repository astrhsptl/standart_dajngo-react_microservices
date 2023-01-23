class ICryptographAlghorytm:
    '''
    Interface of cryptograpth alghorytm class.
    Need to relize:
        - init
        - str
        - len
        - encode
    '''
    def __init__(self, clear_string: str) -> None:
        pass 

    def __str__(self) -> str: 
        pass

    def __len__(self) -> str:
        pass 

    def encode(self, clear_string: str) -> str:
        pass


class ChangingAlghorythm(ICryptographAlghorytm):
    '''
    Changing alghorythm class. Just change symbols on numbers.
    '''
    def __init__(self, clear_string: str) -> None:
        self.clear_string: str = clear_string
        self.coded_string = ''
        self.alphabet = {
            'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7,
            'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13,
            'м': 14, 'н': 15, 'о': 16, 'п': 17, 'с': 18, 'т': 19,
            'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25,
            'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32,
            'a': 33, 'b': 34, 'c': 35, 'd': 36, 'e': 37, 'f': 38, 'g': 39,
            'h': 40, 'i': 41, 'j': 42, 'k': 43, 'l': 44, 'm': 45, 'n': 46,
            'o': 47, 'p': 48, 'q': 49, 'r': 50, 's': 51, 't': 52, 'u': 53,
            'v': 54, 'w': 55, 'x': 56, 'y': 57, 'z': 58,
            '{': 59, '}': 60, '!': 86, '@': 62, '#': 63, '$': 64, '%': 89,
            '^': 66, '&': 67, '*': 68, '(': 69, ')': 70, '"': 71, "'": 72,
            '\\': 73, '<': 74, '>': 75, '/': 76, ',': 77, '.': 78, '|': 79,
            '-': 80, '_': 81, '=': 82, '+': 83, '`': 84, '~': 85, '№': 87,
            ';': 88, ':': 90, '?': 91, ' ':  92,
        }

    def __str__(self) -> str: 
        return self.coded_string

    def __len__(self) -> str:
        return len(self.coded_string)

    def encode(self, clear_string: str) -> str:
        pass



class Cryptograph:
    def __init__(self, clear_string: str) -> None:
        self.clear_string = clear_string
        self.coded_string = ''
        self.alphabet = {
            'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7,
            'ж': 8, 'з': 9, 'и': 10, 'й': 11, 'к': 12, 'л': 13,
            'м': 14, 'н': 15, 'о': 16, 'п': 17, 'с': 18, 'т': 19,
            'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25,
            'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29, 'э': 30, 'ю': 31, 'я': 32,
            'a': 33, 'b': 34, 'c': 35, 'd': 36, 'e': 37, 'f': 38, 'g': 39,
            'h': 40, 'i': 41, 'j': 42, 'k': 43, 'l': 44, 'm': 45, 'n': 46,
            'o': 47, 'p': 48, 'q': 49, 'r': 50, 's': 51, 't': 52, 'u': 53,
            'v': 54, 'w': 55, 'x': 56, 'y': 57, 'z': 58,
            '{': 59, '}': 60, '!': 86, '@': 62, '#': 63, '$': 64, '%': 89,
            '^': 66, '&': 67, '*': 68, '(': 69, ')': 70, '"': 71, "'": 72,
            '\\': 73, '<': 74, '>': 75, '/': 76, ',': 77, '.': 78, '|': 79,
            '-': 80, '_': 81, '=': 82, '+': 83, '`': 84, '~': 85, '№': 87,
            ';': 88, ':': 90, '?': 91, ' ':  92,
        }
    
