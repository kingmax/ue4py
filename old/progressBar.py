import unreal
import time

total_frames = 90
text_label = 'Working...'
with unreal.ScopedSlowTask(total_frames, text_label) as slow_task:
    slow_task.make_dialog(True)
    for i in range(total_frames):
        if slow_task.should_cancel():
            break
        slow_task.enter_progress_frame(1)
        time.sleep(1)
        print(i)
