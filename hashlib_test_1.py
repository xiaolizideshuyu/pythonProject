import hashlib

# 使用 md5 算法
m = hashlib.md5()

# 要计算的源数据必须是字节串格式
# 字符串对象需要encode转化为字节串对象
m.update("张三，学费已交|13ty8ffbs2v".encode())

# 产生哈希值对应的bytes对象
resultBytes = m.digest()
# 产生哈希值的十六进制表示
resultHex   = m.hexdigest()
print(resultHex)

# 如果你想使用别的哈希算法，比如， sha256 算法，只需要修改为对应的函数 sha256()即可
m = hashlib.sha256()
resultBytes = m.digest()
resultHex   = m.hexdigest()
print(resultHex)