from shannon import getMapper, decode, encode
from efficiency import EncodeStanderd, calc_efficiency

def main():
    sentence = input("Enter a sentence: ")
    mapper = getMapper(sentence)
    print(mapper)
    encoded = encode(sentence, mapper)
    print(encoded)
    decoded = decode(encoded, mapper)
    print(decoded)
    efficiency = calc_efficiency(sentence, encoded, EncodeStanderd.ASCII)
    print(efficiency)

    

if __name__=='__main__':
    main()