# coding:utf-8

import unreal as u
import sys


def hi():
    u.log('hi, {}'.format(sys.version))

if __name__ == '__main__':
    hi()
