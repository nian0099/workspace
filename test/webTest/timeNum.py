#coding:utf-8
import time

def time_me(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        end = time.clock()
        fn(*args, **kwargs)
        print u'%s cost %s second'%(fn.__name__, end - start)
    return _wrapper

@time_me
def test(x,y):
    time.sleep(2.5)
#
# @time_me
# def test2(x):
#     time.sleep(0.5)

test(1,2)