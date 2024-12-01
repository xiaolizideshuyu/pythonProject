print("welcome")

while True:
    exp = input('\n\n请输入一个数学运算式 [输入quit退出]：')
    if exp == 'quit':
        break
    try:
        result = eval(exp)
    except:
        print('\n！！无效的运算式')
        continue

    print(f'结果为: {result}')

if __name__ == '__main__':
    pass
    # 在cmd窗口， cd进入到该代码文件所在的目录下面，执行如下的命令
    # pyinstaller    byhy.py - -workpath    d:\pybuild - -distpath    d:\pybuild\dist
    # 注意：
    # 参数 - -workpath,    指定了制作过程中临时文件的存放目录
    # 参数 - -distpath    指定了最终的可执行文件目录所在的父目录
    # 上面的命令执行结束后，我们进入到    目录    d:\pybuild\dist    中，就会发现有一个目录叫byhy （和我们的入口文件byhy同名），该目录中包含了如下文件
