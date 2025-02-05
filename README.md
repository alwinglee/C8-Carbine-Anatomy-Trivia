Title: C8 Carbine Anatomy Trivia

Table of Contents:
    - Introduction
    - Installation
    - Dependencies
    - Required Files
    - How to Play
    - Features
    - Project Status
    - Used Technologies
    - Sources
    - Author's Information

Introduction:
- C8 Carbine Anatomy Trivia is an educational application designed to test the user's knowledge of the carbine's parts. The application will randomly display a part, and the user will be required to guess it correctly.

Installation:
- Clone the repository or download as a Zip
- Install the pandas library
- Run the game and enjoy

Dependencies:
- Requires the installation of pandas to read the CSV file.

Required Files:
- For the application to function properly, the following two files must be present: C8_Carbine_Parts.csv and C8_Diagram.gif.
- The CSV file contains all the C8 Carbine parts, while the GIF file serves as the background and interface for the trivia application. Do not modify or rename the files.
- Both files are already included in the repository.

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

Used Technologies:
- The application was built using PyCharm Community Edition 2023.3.3 and written in the Python programming language (3.12.1).
- Libraries:
    - Pandas (installation required) - Reads and extracts data from the CSV file C8_Carbine_Parts.csv, which contains all the different C8 Carbine parts.
    - Turtle Graphics (built-in library) - Renders the graphical interface, handles user input, displays the timer, tracks the part counter, records the fastest time, and shows correctly identified parts.
    - Random (built-in library) - Assists in selecting a random gun part to test the user's knowledge.
- Custom Modules:
    - parts - An instance is created after each successful guess and is displayed next to its corresponding alphabet.
    - counter - Counts the correct and remaining parts until the round is complete.
    - timer - Tracks, stops, and resets time.
    - score - Determines if a personal record is achieved and displays the best record during the session and even after the application is closed and reopened.

Sources:
- As a reservist in the military, I wanted to create an application to continuously assess my knowledge of the C8 Carbine's parts. By incorporating my technical skills in Python, I designed it to be a convenient way to challenge myself.
Please note that the C7A2 is the standard-issue rifle of the Canadian Armed Forces. Unfortunately, I was unable to find a high-quality image of the C7A2; however, the C8 Carbine has identical parts to the C7A2.

Author's Information:
- Created by Alwin Lee.
- Contact: alwin.g.lee@gmail.com
