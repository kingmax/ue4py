# coding:utf-8
# testing for startupScript dynamic import this lib

def sayHi(n=''):
    print('Hi, %s'%n)

def add(a, b):
    return a+b;

if __name__ == '__main__':
    print('run myLibs.py')

    try:
        print(ab)
    except Exception as ex:
        print(ex.message)