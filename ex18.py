def print_two(*args):
    arg1,arg2 = args
    print "arg1:%r,arg2:%r"%(arg1,arg2)


def print_two_again(arg1 , arg2):
    print "arg1:%r,arg2:%r" % (arg1, arg2)


def print_one(arg1):
    print "arg1:%r"%arg1


def print_none():
    print "I got nothing"


print_two('Zed','Shaw')
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# 函数定义是以def开始的吗？
# 函数名称是以字符下划线组成的吗？
# 函数名称后面是不是紧跟着括号？
# 括号里面是不是包含着参数，多个参数是不是以逗号隔开
# 参数的名称是否可以重复
# 紧跟着参数的是不是括号和冒号
# 紧跟着函数定义的代码是不是使用了4个空格的缩进
# 函数结束后是否取消了缩进