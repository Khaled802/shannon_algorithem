from collections import Counter, defaultdict

def getProbOfEachChar(sentence: str)-> dict:
    '''
    get the propability of each char in the sentence
    :param sentence: the sentence
    :return: the propability of each char in the sentence
    
    '''
    frq = Counter(sentence)
    length = len(sentence)

    for char in frq:
        frq[char] /= length
    
    return frq


def reverse_dict(dictionary: dict)-> dict:
    '''
    it reverses the value with the key
    :param dictionary: the dictionary
    :return: the reversed dictionary
    example:
    input: {'a':1, 'b':2}
    output: {1: 'a', 2: 'b'}
    
    note:
    if there are two keys with the same value,
    the last key will be taken.
    
    example:
    input: {'a':1, 'b':1}
    output: {1: 'a'}
    '''
    reversed_dict = defaultdict(str)
    for key, value in dictionary.items():
        reversed_dict[value] = key
    return reversed_dict
