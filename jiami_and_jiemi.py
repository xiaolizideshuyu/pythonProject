# 加解密算法，是对源数据 进行运算产生加密数据，以及反向过程，对加密数据反算出 源数据。
# 加解密算法 和 hash算法 不同点有：
# 加解密算法 是可逆的，hash算法是不可逆的。
# hash算法可以对很大的数据产生比较小的哈希值，而加密算法源数据很大，加密后的数据也会很大
# 加解密算法 可以分为 对称加密 以及 不对称加密
# 对称加密 指 加密和解密 使用相同的 密钥 。
# 而 不对称加密 指 加密和解密 使用不同的 密钥，通常是一对密钥，称之为公钥（用来加密）和私钥（用来解密）。
# 比较常见的 对称加密算法有： AES, RC4, DES, 3DES, IDEA 等。
# 其中安全等级较高的是 AES。 关于加密算法安全性可以参考这篇文章
# 而最知名的 不对称加密系统 就是 RSA (Rivest–Shamir–Adleman) 。

# 计算哈希值， Python有内置的库。
# 但是，加解密的库，Python 没有内置的。我们需要安装使用第三方开发的库。
# 目前口碑比较好的Python加解密库有 cryptography 和 PyNaCl
# 这里，我们以使用比较广泛的 cryptography 为例（Paramiko就使用该库作为底层加解密计算），展示如何进行加解密。
# 首先，我们执行命令 pip install cryptography 安装该库。

# 注意：由于Paramiko就使用该库作为底层加解密计算，如果你已经安装了Paramiko，cryptography库肯定已经安装好了。 就会显示 Requirement already satisfied
# 下面是一个使用 该库进行 AES 加解密运算的例子

from cryptography.fernet import Fernet

# 产生密钥， 密钥是加密解密必须的
key = Fernet.generate_key()
f = Fernet(key)

src = "白月黑羽网站学习Python真好啊"
# 源信息，必须是字节串对象
# 字符串对象需要encode一下
srcBytes = src.encode()

# 生成加密字节串
token = f.encrypt(srcBytes)
print(token)

# 解密，返回值是字节串对象
sb = f.decrypt(token)
print(sb.decode())