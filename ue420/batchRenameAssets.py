# coding:utf-8

import unreal as u

def rename_assets():
    system_lib = u.SystemLibrary()
    editor_util = u.EditorUtilityLibrary()
    string_lib = u.StringLibrary()

    print('{}, {}, {}'.format(system_lib, editor_util, string_lib))


if __name__ == '__main__':
    rename_assets()