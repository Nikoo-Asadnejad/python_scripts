import time
import os

def pomodoro_timer(minutes=25):
    print(f"🍅 Pomodoro started: {minutes} minutes")
    for i in range(minutes * 60, 0, -1):
        mins, secs = divmod(i, 60)
        print(f"\rTime left: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
    print("\n🔔 Time's up! Take a break.")
    os.system('say "Time is up"')  # macOS voice alert

pomodoro_timer(25)
