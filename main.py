from shannon import getMapper, decode, encode
from efficiency import EncodeStanderd, calc_efficiency

longLine = '=' * 35
shortLine = '-' * 10

def main():
    sentence = input("Enter a sentence: ")
    
    mapper = getMapper(sentence)
    print(f'Code Table\n{shortLine}\n' + '\n'.join(f'{key} : {value}' for key, value in mapper.items()))
    print(longLine)

    encoded = encode(sentence, mapper)
    print(f'After Compression\n{shortLine}\n' + encoded)
    print(longLine)

    decoded = decode(encoded, mapper)
    print(f'After Decompression\n{shortLine}\n' + decoded)
    print(longLine)

    efficiency = calc_efficiency(sentence, encoded, EncodeStanderd.ASCII)
    print('Efficiency = ' + str(efficiency))
    
    

if __name__=='__main__':
    main()
