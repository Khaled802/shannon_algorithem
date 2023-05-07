
class EncodeStanderd:
    ASCII = 8
    UNICODE = 16

def calc_efficiency(sentence: str, encoded: list, encode_standard: int)-> float:
    totalSizeBefore = len(sentence) * encode_standard
    encodedSizeAfter = sum([len(x) for x in encoded])
    return (1 - (encodedSizeAfter / totalSizeBefore)) * 100
