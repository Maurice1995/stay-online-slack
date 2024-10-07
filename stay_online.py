import pyautogui
import time
from datetime import datetime, timedelta

# Constants
INTERVAL = 1790  # 29 minutes and 50 seconds in seconds
HOURS_TO_SECONDS = 3600

def simulate_activity(is_shift=False):
    """
    Simulate user activity by pressing 'm' or 'shift+m'.
    """
    if is_shift:
        pyautogui.hotkey('shift', 'm')
    else:
        pyautogui.press('m')

def switch_to_slack():
    """
    Attempt to switch to the Slack window using Alt+Tab.
    """
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)  # Wait for window switch to complete

def format_time(seconds):
    """
    Format seconds into a string of hours, minutes, and seconds.
    """
    return str(timedelta(seconds=int(seconds)))

def maintain_active_status(duration_hours):
    """
    Maintain active status on Slack for the specified duration.

    Args:
    duration_hours (int): Number of hours to maintain active status
    """
    total_intervals = int((duration_hours * HOURS_TO_SECONDS) / INTERVAL)
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=duration_hours)
    
    for interval in range(total_intervals):
        next_action_time = datetime.now() + timedelta(seconds=INTERVAL)
        is_shift = interval % 2 != 0  # Alternate between 'm' and 'shift+m'

        while datetime.now() < next_action_time:
            remaining_seconds = (next_action_time - datetime.now()).total_seconds()
            action_char = 'M' if is_shift else 'm'
            status_line = f"\rNext '{action_char}' in: {format_time(remaining_seconds)} | Progress: {interval+1}/{total_intervals}"
            print(status_line, end='', flush=True)
            time.sleep(0.5)  # Update every half second

        simulate_activity(is_shift)
        print(f"\nPressed {'shift+m' if is_shift else 'm'}")

    print("\nActive status maintenance completed!")

def main():
    """
    Main function to run the Slack active status script.
    """
    print("Slack Active Status Script")
    print("==========================")
    print("This script helps maintain your 'active' status on Slack.")
    print("Please ensure your cursor is in a private Slack chat before proceeding.")
    
    try:
        duration_hours = int(input("Enter the number of hours to maintain active status: "))
        if duration_hours <= 0:
            raise ValueError("Duration must be a positive number.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    print("\nPreparing to start. Make sure a private Chat was open last on Slack. The Script will switch the Tab automatically.")
    for i in range(5, 0, -1):
        print(f"Starting in {i} seconds...", end='\r')
        time.sleep(1)
    print("\nStarting now!")

    switch_to_slack()
    maintain_active_status(duration_hours)

if __name__ == "__main__":
    main()