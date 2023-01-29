from abc import ABC, abstractclassmethod


class ICryptographAlghorytm(ABC):
    '''
    Interface of cryptograpth alghorytm class.
    Need to relize:
        - init
        - str
        - len
        - encode
    '''
    
    @abstractclassmethod
    def __init__(self, clear_string: str) -> None:
        pass 

    @abstractclassmethod
    def __str__(self) -> str: 
        pass

    @abstractclassmethod
    def __len__(self) -> str:
        pass 

    @abstractclassmethod
    def encode(self, ) -> None:
        pass


class ChangingAlghorythm(ICryptographAlghorytm):
    '''
    Changing alghorythm class. Just change symbols on numbers.
    '''
    def __init__(self, clear_string: str) -> None:
        self.clear_string: str = clear_string
        self.coded_string: str = ''
        self.alphabet: dict = {
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

    def __str__(self, ) -> str: 
        return self.coded_string

    def __len__(self, ) -> str:
        return len(self.coded_string)

    def encode(self, ) -> None:
        for i in range(len(self.clear_string)):
            if self.clear_string[i] in self.alphabet:
                self.coded_string += str(self.alphabet[self.clear_string[i]])
            else:
                self.coded_string += self.clear_string[i]

            self.coded_string += ' '

class Node:
    '''Node of haffman`s alg tree'''
    def __init__(self, probability=None, symbol=None, left_branch=None, right_branch=None):
        self.probability = probability
        self.symbol = symbol
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.code = ''
    
    def set_probability(self, current_probability) -> None:
        self.probability = current_probability
    
    def set_symbol(self, current_symbol):
        self.symbol = current_symbol

    def set_left_branch(self, current_left_branch) -> None:
        self.left_branch = current_left_branch

    def set_right_branch(self, current_right_branch) -> None:
        self.right_branch = current_right_branch
    
    def set_code(self, current_code) -> None:
        self.code = current_code

class HaffmanAlghorythm(ICryptographAlghorytm):
    '''Haffman alghorythm. Return only coded string'''
    def __init__(self, clear_string: str) -> None:
        self.clear_string = clear_string
        self.coded_string = ''
        self.codes: dict = {}
        super().__init__(clear_string)
    
    def __str__(self) -> str: 
        return self.coded_string

    def __len__(self) -> str:
        return len(self.coded_string)

    def _calculate_code(self, node: Node, value='') -> dict:
        new_value = value + str(node.code)

        if node.left_branch:
            self._calculate_code(node.left_branch, new_value)
        if node.right_branch:
            self._calculate_code(node.right_branch, new_value)

        if not node.left_branch and not node.right_branch:
            self.codes[node.symbol] = new_value
            
        return self.codes        

    def _calculate_probability(self, data: str) -> dict:
        symbols = dict()

        for element in data:
            if symbols.get(element) == None:
                symbols[element] = 1
            else: 
                symbols[element] += 1
        return symbols

    def _form_final_string(self, data: str, coding: dict) -> str:
        encoding_output = []

        for symbol in data:
            encoding_output.append(coding[symbol])
            
        string = ' '.join([str(item) for item in encoding_output])    
        return string

    def _formairate_start_nodes(self, data: str) -> list:
        symbols = self._calculate_probability(data)
        nodes = []
        
        for symbol in symbols.keys():
            nodes.append(Node(symbols.get(symbol), symbol))

        return nodes

    def _building_binary_tree_and_return_root(self, nodes: list) -> Node:
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.probability)
            left_node, right_node = nodes[1], nodes[0]
            left_node.code, right_node.code = 1, 0
            newNode = Node(
                left_node.probability+right_node.probability, 
                left_node.symbol+right_node.symbol, 
                left_node, 
                right_node)
            nodes.remove(left_node)
            nodes.remove(right_node)
            nodes.append(newNode)

        return nodes[0]

    def encode(self,) -> str:
        self.coded_string = self._form_final_string(
            self.clear_string, self._calculate_code(
                self._building_binary_tree_and_return_root(
                    self._formairate_start_nodes(
                        self.clear_string))))
