bits = [''.join(['01'[i&(1<<b)>0] for b in range(7,-1,-1)]) for i in range(256)]

def pack_7bit(data: bytearray):
    buffer = 0
    bitcount = 0
    out = bytearray()

    while True:
        if bitcount < 7:
            buffer <<= 8
            buffer |= data[0]
            data = data[1:]
            bitcount += 8
        out += bytearray((buffer >> (bitcount - 7),))
        buffer &= (1 << (bitcount - 7)) - 1
        bitcount -= 7

        if len(data) == 0: break

    return out + bytearray((buffer << (7 - bitcount), ))


def unpack_7bit(data: bytearray):
    buffer = 0
    bitcount = 0
    out = bytearray()

    while True:
        if bitcount < 8:
            buffer <<= 7
            buffer |= data[0]
            data = data[1:]
            bitcount += 7

        if bitcount >= 8:
            out += bytearray((buffer >> (bitcount - 8), ))
            buffer &= (1 << (bitcount - 8)) - 1
            bitcount -= 8

        if len(data) == 0:
            break

    return out
