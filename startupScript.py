def runStartupScript():
    print('Hello, UE4')

if __name__ == '__main__':
    runStartupScript()

    # test using other lib
    import sys
    import os
    myLibPath = os.path.join(os.path.dirname(__file__), 'test_lib')
    print(myLibPath)
    sys.path.append(myLibPath)
    import _myLibs
    print('dynamic import other function lib succuss!')
    _myLibs.sayHi('Jason.Li')
    print(_myLibs.add(100, 100))
    print('startup script done.')