
import sys

def check(test, err):
    if not test:
        sys.exit(err)

cell_size=4 # bytes


dict_size=10000 # bytes
check( 2**(cell_size*8) >= dict_size,
      "dict size too big to be addressed")

cell_mask = (1<<(cell_size*8))-1
# I need this to simulate limited 
# integer size
def n2b(val):
    val &= cell_mask
    return val.to_bytes(cell_size, "little")
def b2n(val):
    return int.from_bytes(val, "little")
    
class Dict:
    def __init__(self):
        self.d = bytearray(dict_size)
    def __getitem__(self,index):
        return b2n(self.d[index:index+cell_size])
    def __setitem__(self,index,value):
        self.d[index:index+cell_size]=n2b(value)

d=Dict()

# memory layout (growing memory towards right)
# [ib|user|pad|...|ds|rs|block]

# Design choices i made
# input buffer length is also number of
# internal words
# stack pointers decrease then data entered
# stack pointer read then increased


# Offset of pad after latest defined word
pad_off=32 # bytes

# Input buffer, size
ib=50 * cell_size

# Return stack, size. grow downwards
rs=20 * cell_size

# Block buffer, size
block_size=1024 # bytes

# Pointers
block=dict_size-block_size
rsp=block
tos=rsp-rs
dsp=tos

# Structure of word
# [ref|len|chars|codeword|code]
# ref (cell_size bytes): address of last word
# len (1 byte): length of name
# chars: characters of the name
# codeword: address of codeword
# code to be interpreter, that ends with exit

def dspush(n):
    global dsp
    dsp-=1
    d[dsp]=n
def dspop():
    global dsp
    n=d[dsp]
    dsp+=1

internals=["+","-","*","/"]

def iword(n): # get index of internal word
    return internals.index(n)

def next():
    global pc,d
    d[rsp] += 1
    pc = d[d[rsp]]

def run_internal(w):
    if w==iword("+"):
        dspush(dspop()+dspop())
    elif w==iword("-"):
        dspush(dspop()-dspop())
        next()
    elif w==iword("*"):
        dspush(dspop()*dspop())
        next()
    elif w==iword("/"):
        dn=dspop()
        dspush(dspop()/dn)
        next()
dspush(4)
for i in range(dsp,tos,4):
    print(d[i])

pc = 0
while False:
    # Outer interpreter loop
    codeword = d[pc]
    run_internal(codeword)
    break


