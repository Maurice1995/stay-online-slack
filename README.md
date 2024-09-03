# Slack Active Status Script

This Python script helps maintain an "active" status on Slack when you're away from your keyboard but still want to remain reachable. It's designed for professionals who may be working on tasks that don't involve constant computer interaction, such as handling hardware, operating CNC machines, or managing 3D printers.

## Purpose

The script simulates minimal activity to prevent Slack from changing your status to "away" after 30 minutes of inactivity. This ensures that colleagues can see you as available and feel comfortable reaching out, even when you're not actively using your computer.

**Important Note:** This script is intended for legitimate use cases where you are actually available and responsive, just not at your keyboard. It should not be used to mislead colleagues about your availability.

## How It Works

1. The script uses `pyautogui` to simulate keystrokes at regular intervals.
2. It alternates between pressing 'm' and 'shift+m' every 29.83 minutes (1790 seconds).
3. These keystrokes are minimal and designed to be used in a private Slack chat to avoid disturbing ongoing conversations.

## Prerequisites

- Python 3.x
- pyautogui library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Maurice1995/stay-online-slack.git
   ```
2. Install the required library:
   ```
   pip install pyautogui
   ```

## Usage

1. Open a private chat in Slack where your keystrokes won't disturb others.
2. Run the script:
   ```
   python slack_active.py
   ```
3. Enter the number of hours you want to maintain active status when prompted.
4. Quickly switch back to your Slack window (the script will attempt to do this for you with Alt+Tab).

## Ethical Considerations

- Use this script responsibly and in accordance with your workplace policies.
- Ensure you're actually available and responsive to messages while the script is running.
- Be transparent with your team about your work habits and availability.

## Disclaimer

This script is provided as-is, without any guarantees. The user is responsible for using it in an ethical manner and in compliance with their workplace policies.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

[MIT License](https://choosealicense.com/licenses/mit/)