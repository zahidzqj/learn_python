# import sendmsg
# import recvmsg
# sendmsg.test1()
# sendmsg.test2()
# recvmsg.test1()


#from sendmsg import test1,test2
#from sendmsg import test2

#from sendmsg import *
#from recvmsg import *

#test1()
#test2()

#测试多个文件调用
import sys
sys.path.append('src')
from src import test
test.test1()


# import sys
# print(sys.path)