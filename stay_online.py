import pyautogui
import time


def enter_time():
    time.sleep(1790)
    pyautogui.press('m')
    time.sleep(1790)
    pyautogui.hotkey('shift', 'm')

def main():
    print("Script is starting, make sure you have your curser in a private chat in Slack one Alt+Tab away.")

    num_hours = int(input("Enter the number of hours to sleep: "))

    time.sleep(1)

    # Perform the initial alt+tab to switch to the browser window
    pyautogui.hotkey('alt', 'tab')

    time.sleep(1)  # Wait a bit longer after switching windows

    for day in range(num_hours):
        enter_time()

    print("Sleep time is over!")

if __name__ == "__main__":
    main()
