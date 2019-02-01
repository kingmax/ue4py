import unreal

obj = unreal.MediaPlayer()
with unreal.ScopedEditorTransaction('My Transaction Test') as trans: # 支持undo, redo
    obj.set_editor_property('play_on_open', True)
    obj.set_editor_property('vertical_field_of_view', 60)

    print(obj.play_on_open)
    # print(obj.vertical_field_of_view)
    # LogPython: Error: Traceback (most recent call last):
    # LogPython: Error:   File "D:/git/ue4py/undo_history.py", line 9, in <module>
    # LogPython: Error:     print(obj.vertical_field_of_view)
    # LogPython: Error: AttributeError: 'MediaPlayer' object has no attribute 'vertical_field_of_view'

    # 更改属性时推荐的做法：
    print(obj.get_editor_property('play_on_open'))
    print(obj.get_editor_property('vertical_field_of_view'))