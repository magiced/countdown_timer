#! python3

import tkinter as tk
import simpleaudio as sa
import time
import os

""" VARIABLES """

root = tk.Tk()
b_timer_running = False
delay_time = 10
target_time = 0.0
time_string_last = ""
b_tick = tk.BooleanVar()
b_noise = tk.BooleanVar()
b_end_signal = tk.BooleanVar()

tick_file_path = os.getcwd() + '/tick.wav'
noise_file_path = os.getcwd() + '/brown_noise.wav'
alarm_file_path = os.getcwd() + '/klaxon.wav'

tick_wave_obj = sa.WaveObject.from_wave_file(tick_file_path)
alarm_wave_obj = sa.WaveObject.from_wave_file(alarm_file_path)
noise_wave_obj = sa.WaveObject.from_wave_file(noise_file_path)

""" FUNCTIONS """
def toggle_timer():
    global b_timer_running
    global delay_time
    global target_time
    global noise_wave_obj

    if b_timer_running is False:
        # target_time = time.time() + delay_time + 1
        target_time = time.time() + scl_time.get() + 1
        b_timer_running = True
        btn_start["text"] = "STOP"
        if b_noise.get():
            print("I'm Playing a NOISE!!!!")
            noise_play_obj = noise_wave_obj.play()
    else:
        b_timer_running = False
        btn_start["text"] = "START"
        if noise_play_obj.is_playing():
            noise_play_obj.stop()   


def reset_timer():
    global b_timer_running
    b_timer_running = False
    target_time = 0

def update_display():
    global b_timer_running
    global target_time
    global time_string_last
    global tick_wave_obj
    global alarm_wave_obj

    if b_timer_running:
        time_left = target_time - time.time()
        time_string = time.strftime("%H:%M:%S",time.gmtime(time_left))
        if (target_time > time.time()):
            if time_string != time_string_last:
                clock['text'] = time_string
                if b_tick.get():
                    tick_play_obj = tick_wave_obj.play()
        else:
            toggle_timer()
            if b_end_signal.get():
                alarm_play_obj = alarm_wave_obj.play()
        time_string_last = time_string
    else:
        clock['text'] = '00:00:00'

    clock.after(200,update_display) # after x time update the display

""" GUI """
root.title("TIMER")
clock = tk.Label(root, font=('times', 40, 'bold'), fg='green',bg='black')
scl_time = tk.Scale(root, from_=0, to_=60, orient="horizontal")
btn_start = tk.Button(root, text='START', command=toggle_timer)
chk_tick = tk.Checkbutton(root, text="TICK", variable=b_tick)
chk_noise = tk.Checkbutton(root, text="PLAY NOISE", variable=b_noise)
chk_end_signal = tk.Checkbutton(root, text="END NOISE", variable=b_end_signal)

clock.pack()
scl_time.pack()
btn_start.pack()
chk_noise.pack()
chk_tick.pack()
chk_end_signal.pack()

update_display()  # first call so that after time tick is recalled
root.mainloop()
