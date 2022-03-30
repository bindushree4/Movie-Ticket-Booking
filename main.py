from theater import Theater
import sys
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("The program should accept only path to the input file as an argument.")
        sys.exit()

    input_path = sys.argv[1]
    try:
        input_file = open(input_path)
    except IOError:
        print("Input file does not exist.")
        sys.exit()
    theater = Theater(input_path)
    print(theater.seatReservation())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
