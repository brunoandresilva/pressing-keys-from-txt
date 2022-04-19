from pynput.keyboard import Key, Controller


def main():
    keyboard = Controller()
    with open('test.txt') as f:
        lines = f.readlines()
    for i in lines:
        if i.find("press ") != -1:
            index = i.find("press")
            key = i[index + 6]
            keyboard.press(key)
            keyboard.release(key)

if __name__ == "__main__":
    main()