import pandas
from turtle import Turtle, Screen
import random
from parts import Parts
from counter import Counter
from timer import Timer
from score import Score

"""
C8 Carbine Anatomy Trivia is an educational application designed to test the user's knowledge of its parts. The 
application will randomly display a part, and the user will be required to guess it correctly. Users can evaluate 
their progress by tracking how quickly they complete each round. The quickest time will be recorded and displayed.
The game is completed once all 22 parts are named correctly. The game can be restarted during or after each round.

Author: Alwin Lee
Date: Feb 03, 2025
Version: 1.0

"""


def configure_screen():
    """
    Configure the screen dimensions and upload an image of the C8 Anatomy Trivia layout.

    :return: None
    """
    screen.title("C8 Carbine")
    screen.setup(width=1169, height=789, startx=None, starty=0)
    screen.addshape("C8_Diagram.gif")
    image = Turtle()
    image.shape("C8_Diagram.gif")


def retrieve_csv_data():
    """
    Reads the CSV file 'C8_Carbine_Parts.csv' and returns the data.

    Each row contains a unique part and its corresponding x and y coordinates,
    along with a primary key identified by an alphabet.

    :return: contents of the CSV file as a Pandas DataFrame.
    """
    data = pandas.read_csv("C8_Carbine_Parts.csv")
    return data


def select_random_part(temp_parts_list):
    """
    Randomly selects a part from temp_parts_list, removes it from the list, and presents it as the next question.

    :param temp_parts_list: a list containing parts of the C8 Carbine.
    :return: a random part that is removed from the temp_parts_list.
    """
    random_alphabet = random.choice(temp_parts_list)
    temp_parts_list.remove(random_alphabet)
    return random_alphabet


def restart_game():
    """
    Resets the game characteristics, such as time, counter, and parts, to their original state.
    The temp_parts_list, containing all the parts, is repopulated, and a new game begins.

    :return: None
    """
    timer.reset_timer()
    timer.start_timer()
    counter.reset_counter()
    Parts.reset_parts()
    start_game(retrieve_csv_data())


def start_game(data):
    """
    Container to organize the entire game and recall functions when the game requires a restart.

    The user is required to name a variety of parts of the C8 Carbine until all 22 parts are named.
    A timer is used to track how long each round takes and records the fastest time. During and after each round,
    the user can also restart from the beginning or quit the program.

    :param data: contents of the CSV file C8_Carbine_Parts as a Pandas DataFrame.
    :return: None
    """
    # Populate the screen with objects before starting the game.
    screen.update()
    # temp_parts_list acts as temporary storage for the parts' primary keys.
    temp_parts_list = master_parts_list[:]
    while len(temp_parts_list) != 0:
        random_part = select_random_part(temp_parts_list)
        # Retrieve the CSV row corresponding to the currently assessed part.
        filtered_part = data[data.Alphabet == random_part]
        while True:
            screen.update()
            user_input_text = screen.textinput(title="C8 Carbine", prompt=f"Name gun part: {random_part}\nType "
                                                                          f"'Restart' to begin again, or 'Quit' to "
                                                                          f"exit.")
            # Ignore empty inputs or dialog closure by the user.
            if user_input_text is None:
                continue
            if filtered_part.Part.item() == user_input_text.title().strip():
                Parts(filtered_part.Part.item(), filtered_part.Xcoordinate.item(), filtered_part.Ycoordinate.item())
                counter.update_counter()
                break
            elif user_input_text.lower().strip() == "restart":
                restart_game()
            elif user_input_text.lower().strip() == "quit":
                exit()
    score.clear()
    timer.stop_timer()
    while True:
        screen.update()
        user_input_text = screen.textinput(title="C8 Carbine", prompt=f"* * Trivia Completed * * \nType 'Restart' to "
                                                                      f"begin again, or 'Quit' to exit.")
        # Ignore empty inputs or dialog closure by the user.
        if user_input_text is None:
            continue
        elif user_input_text.lower() == "restart":
            restart_game()
        elif user_input_text.lower() == "quit":
            exit()


screen = Screen()
# Turn off animation to avoid visual delays.
screen.tracer(0)
configure_screen()
temp_parts_list = []
score = Score()
timer = Timer(screen)
counter = Counter()
# Save a copy of parts' primary keys to master_parts_lists.
master_parts_list = retrieve_csv_data().Alphabet.to_list()
start_game(retrieve_csv_data())

screen.mainloop()
