import struct
"""负数的处理"""

a = 1
b = -1

# 打包
aa = struct.pack('>i', a)
bb = struct.pack('>i', b)
print(aa, aa.hex())
print(bb, bb.hex())

# 解包
aaa=struct.unpack('>i' , aa)
bbb=struct.unpack('>i',bb)
print(aaa)
print(bbb)