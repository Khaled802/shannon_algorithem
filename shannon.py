from collections import Counter, defaultdict
from helpers import getProbOfEachChar, reverse_dict


def divide(prob: list, start: int, end: int)-> int:
    '''
    divide the list into two parts depend on the propability of each character
    :param prob: the list
    :param start: the start index
    :param end: the end index (excluded)
    :return: the index of the middle part of the list
    '''
    probs_values = [pair[1] for pair in prob[start:end]]
    probs_values_sum = sum(probs_values)
    perv_sum = 0
    for index, value in enumerate(probs_values):
        cur_sum = perv_sum + value
        if cur_sum >= probs_values_sum/2:
            if probs_values_sum/2 - perv_sum <= cur_sum - probs_values_sum/2:
                return start + index - 1
            return start + index
        
        perv_sum = cur_sum

    try:
        return end - 2
    except Exception as e:
        return end - 1

    


def getCodeOfEachChar(prob: list, start: int, end: int, out: defaultdict, _code=''):
    '''
    get dictionary of each char and its code
    the out: is the final result
    :param prob: it is list of pair ('char', probability(float))
    :param start: the start index
    :param end: the end index (excluded)
    _code: the code of each char (don't touch plz) 🙏
    :return: the dictionary of each char and its code
    '''
    if end - start == 1:
        out[prob[start][0]] = _code
        return
    
    if end <= start:
        return
    print(prob, start, end)
    mid = divide(prob, start, end)
    print(mid)
    getCodeOfEachChar(prob, start, mid+1, out, _code+'0')
    getCodeOfEachChar(prob, mid+1, end, out, _code+'1')
    


def getMapper(sentence: str)-> dict:
    '''
    get the code of each character from the senstence
    :param sentence: the sentence
    :return: the dictionary of each char and its code
    '''
    prob = getProbOfEachChar(sentence)
    codeMap = defaultdict(str)
    getCodeOfEachChar(sorted(list(prob.items()),  key=lambda x: x[1], reverse=True), 0, len(prob), codeMap)
    return codeMap


def test(prob: dict):
    codeMap = defaultdict(str)
    getCodeOfEachChar(sorted(list(prob.items()),  key=lambda x: x[1], reverse=True), 0, len(prob), codeMap)
    return codeMap
    



# print(test({'a': 0.22, 'b': 0.28, 'c': 0.15, 'd': 0.3, 'e': 0.05}))


def encode(sentence: str, codeMap: dict)-> list:
    '''
    encode the sentence
    :param sentence: the sentence
    :param codeMap: the dictionary of each char and its code
    :return: the encoded sentence
    '''
    encoded = []
    for char in sentence:
        encoded.append(codeMap[char])
    return ''.join(encoded)


def decode(encoded: str, codeMap: dict)-> str:
    '''
    decode the encoded sentence
    :param encoded: the encoded sentence with codeMap
    :param codeMap: the dictionary of each char and its code
    :return: the encoded sentence
    '''
    decode = []
    decodeMap = reverse_dict(codeMap)
    code = ''
    for char in encoded:
        code = code + char
        if(code in decodeMap):
            decode.append(decodeMap[code])
            code = ''
            
    return ''.join(decode)

    
