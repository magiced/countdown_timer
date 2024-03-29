#! python3

import tkinter as tk
from tkinter import ttk
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
    global noise_play_obj

    if b_timer_running is False:
        # target_time = time.time() + delay_time + 1
        # target_time = time.time() + scl_time.get() + 1
        delay_time = float(cbo_time.get())*60
        print(delay_time)
        target_time = time.time() + delay_time + 1
        b_timer_running = True
        btn_start["text"] = "STOP"
        if b_noise.get():
            noise_play_obj = noise_wave_obj.play()
    else:
        b_timer_running = False
        btn_start["text"] = "START"
        try:
            noise_play_obj.stop()
        except:
            pass   


def reset_timer():
    global b_timer_running
    b_timer_running = False
    target_time = 0

def jump_to_front():
    root.attributes('-topmost', True)
    root.attributes('-topmost', False)

def update_display():
    global b_timer_running
    global delay_time
    global target_time
    global time_string_last
    global tick_wave_obj
    global alarm_wave_obj

    if b_timer_running:
        time_left = target_time - time.time()
        time_percentage = (time_left/delay_time) * 100
        # calc percentage time left here
        time_string = time.strftime("%H:%M:%S",time.gmtime(time_left))
        if (target_time > time.time()):
            if time_string != time_string_last:
                clock['text'] = time_string
                root.title(time_string)
                # update progress bar here
                progressbar['value'] = time_percentage
                if b_tick.get():
                    tick_play_obj = tick_wave_obj.play()
        else:
            toggle_timer()
            # progressbar is zero
            jump_to_front()
            if b_end_signal.get():
                alarm_play_obj = alarm_wave_obj.play()
        time_string_last = time_string
    else:
        clock['text'] = '00:00:00'
        root.title("TIMER")

    clock.after(200,update_display) # after x time update the display

""" GUI """
root.title("TIMER")
clock = tk.Label(root, font=('times', 40, 'bold'), fg='green',bg='black')
# scl_time = tk.Scale(root, from_=0, to_=60, orient="horizontal")
progressbar = ttk.Progressbar(root, orient='horizontal', length=100, mode='determinate')

# start button and time frame
frame_start = tk.Frame(root)
cbo_time = ttk.Combobox(frame_start,values=(0.01,0.1,1,2,3,4,5,10,15,20,25,30))
btn_start = ttk.Button(frame_start, text='START', command=toggle_timer)
cbo_time.grid(row=0, column=0, )
cbo_time.current(8)
btn_start.grid(row=0, column=1, columnspan=2, sticky="EW")

# checkbox frame
frame_chkbx = tk.Frame(root)
chk_tick = tk.Checkbutton(frame_chkbx, text="TICK", variable=b_tick)
chk_noise = tk.Checkbutton(frame_chkbx, text="NOISE", variable=b_noise)
chk_end_signal = tk.Checkbutton(frame_chkbx, text="ALARM", variable=b_end_signal)
chk_noise.grid(     row=0, column=0,    sticky="E")
chk_tick.grid(      row=0, column=1,    sticky="EW")
chk_end_signal.grid(row=0, column=2,    sticky="W")

# Main window layout
clock.grid(         row=0,  column=0, columnspan=3, sticky="EW")
progressbar.grid(   row=1,  column=0, columnspan=3, sticky="EW")
frame_start.grid(   row=2,  column=0, columnspan=3, sticky="EW")
frame_chkbx.grid(   row=3,  column=0, columnspan=3, sticky="EW")

update_display()  # first call so that after x time the display is updated
root.mainloop()
