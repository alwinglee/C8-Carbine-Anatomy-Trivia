Title: C8 Carbine Anatomy Trivia

Table of Contents:
    - Introduction
    - How to Play
    - Features
    - Project Status:
    - Technologies
    - Libraries
    - Source
    - Author

Introduction:
C8 Carbine Anatomy Trivia is an educational application designed to test the user's knowledge of the carbine's parts.
The application will randomly display a part, and the user will be required to guess it correctly.

How to Play:
- Review and study the C8 parts diagram at:https://www.canada.ca/content/dam/themes/defence/caf/militaryhistory/dhh/drill/figure-4-1-2.jpg
- Run the application.
- Identify the parts as they appear until all 22 parts are named.
- You can restart or quit at any time, including after the round is complete.

Features:
- Timer: The timer is implemented and displayed to track the user's progress each round. The timer resets to zero every time a new game begins.
- Personal Record: The fastest time to complete a round is recorded and displayed, adding an extra level of self-competition.
- Part Counter: Keeps track of how many remaining parts need to be guessed until the trivia game is completed.
- Reset: During or after the game, users can type 'restart' to start the game over again.
- Quit: During or after the game, users can decide whether to continue testing themselves or quit the application by typing 'quit.'

Project Status:
- The application runs without any issues.
- Outstanding task remaining:
    - Complete documentation for the various modules.
- In the future, I plan to add the following features:
    - Limit the user to three attempts to guess all the parts. An attempt is lost for each incorrect or misspelled answer.
    - Redesign the graphical interface using Tkinter.

Technologies:
- Application was built using Pycharm Community Edition 2023.3.3
- Requires the installation of Pandas library

Libraries:
- pandas: Reads and extracts data from the CSV file C8_Carbine_Parts.csv, which contains all the different C8 Carbine parts.
- turtle: Renders the graphical interface, handling user input, displaying the timer, tracking the part counter, recording the fastest time, and showing correctly identified parts.
- random: Assists in selecting a random gun part to assess the user.


Sources:
- As a reservist in the military, I wanted to create an application to continuously assess my knowledge of the C8 Carbine's parts. By incorporating my technical skills in Python, I designed it to be a convenient way to challenge myself.
Please note that the C7A2 is the standard-issue rifle of the Canadian Armed Forces. Unfortunately, I was unable to find a high-quality image of the C7A2; however, the C8 Carbine has identical parts to the C7A2.


Author:
- Created by Alwin Lee.
- Can be contacted at alwin.g.lee@gmail.com
