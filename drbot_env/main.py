# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess
import time
import webbrowser


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # Start Rasa API server
    api_command = "rasa run --enable-api --cors \"*\""
    api_process = subprocess.Popen(api_command.split(), stdout=subprocess.PIPE)

    # Start Rasa action server
    actions_command = "rasa run actions"
    actions_process = subprocess.Popen(actions_command.split(), stdout=subprocess.PIPE)

    time.sleep(10)

    # Open index.html in a web browser
    index_file_path = "index.html"
    webbrowser.open_new_tab(index_file_path)

    # Wait for the processes to complete
    api_process.wait()
    actions_process.wait()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
