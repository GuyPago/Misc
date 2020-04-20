from Project_2_Guys_dictionary import call_dictionary
import time


def launch_hub():
    while True:
        user_input = str(input("Welcome to guy's Hub!\n\nFor Guy's Math-Center --> enter 'm'\n"+
                               "For Guy's Dictionary --> enter 'd'\n\n" +
                               "To quit --> enter 'q'\n")) or '0'
        if (user_input == '0'):
            print("\nNot entered any value\n\n")
        elif (user_input == 'q'):
            print("\nClosing, Bye !")
            time.sleep(1)
            break
        elif (user_input == 'd'):
            print("\nLaunching 'Guy's dictionary', please hold...")
            time.sleep(0.7)
            dot = "." * 5
            t = 0.3
            for i in dot[:]:
                print(dot)
                dot = dot[0:-1]
                time.sleep(t)
                t -= 0.05
            print("\n")
            call_dictionary()
        else:
            print("\nUndefined request\n\n")


if __name__ == "__main__":
    launch_hub()
