#! /home/jbjeong/.conda/envs/myenv/bin/python

import dis
from types import CodeType

def myfunc():
    a = 6
    b = 2
    return a / b

# Hacking the code object
# (a = 6, b = 2) -> (a = 10, b = 2)
# (divide) -> (add)
# return -> 12 !

co = myfunc.__code__
myconsts = (None, 10, 2)
bcode = co.co_code
bcode = list(bcode)
bcode[12] = 23
bcode = bytes(bcode)

co2 = CodeType(co.co_argcount,
               co.co_kwonlyargcount,
               co.co_nlocals,
               co.co_stacksize,
               co.co_flags,
               bcode,
               myconsts,
               co.co_names,
               co.co_varnames,
               co.co_filename,
               co.co_name,
               co.co_firstlineno,
               co.co_lnotab)

# Injecting the modified code object

myfunc.__code__ = co2
print(myfunc())

#dis.dis(myfunc)
#dis.disassemble(co)

#code = co.co_code
#state = 'opcode'
#
#for op in code:
#    #op = ord(op)
#
#    if state == 'opcode':
#        print('%02X' % op, dis.opname[op])
#        if op > dis.HAVE_ARGUMENT:
#            state = 'arg1'
#
#    elif state == 'arg1':
#        print('%02X' % op)
#        state = 'opcode'



