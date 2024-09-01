import pyautogui
import time
import webbrowser

def send_message_via_whatsapp(message, phone_number):
    # open whatsapp web
    webbrowser.open('https://web.whatsapp.com/')
    time.sleep(5)  # wait for whatsapp web to load 

    # search for the contact and send the message
    pyautogui.click(269, 227)  # click on the search box (adjust coordinates if needed)
    pyautogui.write(phone_number)
    time.sleep(1)  # wait for contact to appear
    pyautogui.press('enter')
    time.sleep(1)  # wait for chat to open
    pyautogui.write(message)
    pyautogui.press('enter')

def read_messages_from_file(file_path):
    # read lines from the specified file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def main():
    # phone number of the recipient (include country code, like '+1234567890')
    phone_number = ''

    # path to the text file
    file_path = 'lang.txt'

    # read messages from the file
    messages = read_messages_from_file(file_path)

    # send each message via WhatsApp
    for message in messages:
        # send message with a 1-second delay
        send_message_via_whatsapp(message.strip(), phone_number)
        time.sleep(1)  # wait 1 second before sending the next message

if __name__ == "__main__":
    main()
