import struct

"""负数的处理"""
a = 1
b = -2
# 打包成字节流
aa = struct.pack('>i', a)
bb = struct.pack('>i', b)
print(aa, aa.hex())
print(bb, bb.hex())
# 从字节流中解包
aaa = struct.unpack('>i', aa)
(ccc,) = struct.unpack('>i', aa)
print(ccc)
bbb = struct.unpack('>i', bb)
print(aaa, aaa[0])
print(bbb, bbb[0])
print('打印正负255的2进制:', format(255, 'b'), format(-255, 'b'))  # 返回二进制字符串

# 举例2：
# 定义数据
data = (1, 2.5, b'hello')
# 打包数据
packed_data = struct.pack('if5s', data[0], data[1], data[2])
print(packed_data)
# 解包数据
unpacked_data = struct.unpack('if5s', packed_data)
print(unpacked_data)
# 计算结构大小
formatted_string='if5s'
size=struct.calcsize(formatted_string)
print(f'Size of formatted string: {size}')
