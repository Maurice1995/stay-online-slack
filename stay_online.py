import pyautogui
import time

# Constants
INTERVAL = 1790  # 29 minutes and 50 seconds in seconds
HOURS_TO_SECONDS = 3600

def simulate_activity():
    """
    Simulate user activity by alternating between pressing 'm' and 'shift+m'.
    This function is called every INTERVAL seconds.
    """

    pyautogui.press('m')
    time.sleep(INTERVAL)
    pyautogui.hotkey('shift', 'm')

def switch_to_slack():
    """
    Attempt to switch to the Slack window using Alt+Tab.
    """
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)  # Wait for window switch to complete

def maintain_active_status(duration_hours):
    """
    Maintain active status on Slack for the specified duration.

    Args:
    duration_hours (int): Number of hours to maintain active status
    """
    total_intervals = int((duration_hours * HOURS_TO_SECONDS) / INTERVAL)
    
    for _ in range(total_intervals):
        simulate_activity()

    print("Active status maintenance completed!")

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