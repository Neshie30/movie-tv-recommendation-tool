# Netflix Recommendation Program
#### Video Demo:  <(https://youtu.be/suOodf6xNfQ)>
### Description:
This project is a program that recommends Netflix movies or shows tailored to the user's preferences. The program uses a csv dataset containing information about titles, including genres, release years and a content type. By letting the user filter content with this information,
the program returns a list of recommendations that match the user's interests.

The goal of this project was to apply concepts learned in the CS50 course like loops, conditionals, exceptions and functions.
The project also uses libraries such as randoms, ast, and pandas to manipulate data and generate recommendations.

When the program runs, the user is prompted their name. Then the program asks for a genre, release year, and content type (movie or show). If the user inputs an invalid option, the program will reprompt the user until they input a valid option. After inputs are validated, the content will be filtered and will return at least 5 recommended titles.

### project.py
The file contains 4 functions to operate the recommendation system and the main function to run the program.

- The `load_dataset` function loads the dataset from the "titles.csv" file and returns it as a pandas DataFrame, which will let the program access and manipulate the dataset.
- The `filter_content` function cleans and narrows down the dataset based on the user's chosen genre, release year, and content type. It will remove rows that don't match the user's preference and return rows that are relevant.
- The `recommend_content` function randomly selects values or rows from the filtered data by using the random library and returns them as recommendations to match the user's preferences. If less than five rows exists, the function will print a warning that there are less than 5 values and will return the avaiable matches instead of outputting a ValueError.
- The `get_unique_genres` function extracts all the unique genres from the dataset and returns them as a sorted list. In the dataset, the genres are stored as strings that represent lists (ex. "["action", "comedy"]"). To treat these values as a list, the function uses the ast library to convert the string into an actual list using the `ast.literal_eval` function (ex. ["action", "comedy"]). After converting the strings into lists, the function will extract the genres, remove duplicate values, and sort them alphabetically. This function allows the user to see which genres are available.
- The `main` function will control the flow of the entire program, prompt the user for input, validate the user's response, store the values in variables, pass them through the functions, and display the recommended content.

### test_project.py
The file contains unit tests that check if the program's functions operates as intended. It tests whether the `load_dataset` loads a dataset as a pandas DataFrame and that the dataset it empty. Additional tests check if the `filter_content` function contains any rows and that the function is case insensitive, whether the `recommend_content` function produces at least 5 values, and checks if certain genres appear in the `get_unique_genres` function.

### titles.csv
This is a csv file that contains a dataset including information about movies and shows such as their titles, genres, release_year, and content type. This dataset is read by the program and is used to generate recommendations based of the user's preferences.

### Design Choices
One design choice in this project was the use of while loops to validate user input. Since the program asks the user to select a genre, a release year, and a content type, the program has to ensure the input matches the values existing in the dataset. By using the while loop, the program will reprompt the user repeatedly until a valid input is entered. This prevents any errors from invalid inputs and ensures that the data is filtered properly.

For inputting the release years, an additonal validation step was required because release years are integers. If a user entered a string instead of a number, it would raise a ValueError. To prevent the error, exceptions were implimented. The try block attempts to convert the text to an integer and checks if it matches one of the available years. If a ValueError occurs, the except block will prompt the user to enter the year again. Exceptions were also implimented in the `recommend_content` function so that if fewer than five rows of content are available, the function will warn the user that there are less than 5 rows and returns the available results instead of raising a ValueError.

The project also uses the pandas library because it provides powerful tools for manipulating datasets. Filtering rows, selecting columns, and extracting unique values are much more efficient when using a pandas DataFrame.


