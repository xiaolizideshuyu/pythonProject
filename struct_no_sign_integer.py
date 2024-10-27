import struct

"""负数的处理"""

a = 1
b = -2

# 打包
aa = struct.pack('>i', a)
bb = struct.pack('>i', b)
print(aa, aa.hex())
print(bb, bb.hex())

# 解包
aaa = struct.unpack('>i', aa)
bbb = struct.unpack('>i', bb)
print(aaa)
print(bbb)
print('22222222222222222')

print(format(255, 'b') ,format(-255, 'b')) #返回二进制字符串