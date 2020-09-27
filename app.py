MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    shelf = input("Enter shelf the movie is on: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year,
        'shelf': shelf
    })


def list_movies():
    for movie in movies:
        print(f'{movie["title"]} was directed by {movie["director"]} in the year {movie["year"]}')


def find_movie():
    search_string = input("What movie are you looking for? ")
    for movie in movies:
        if search_string == movie["title"]:
            print(
                f'{movie["title"]} was directed by {movie["director"]} in the year {movie["year"]} and is located at shelf {movie["shelf"]}')
        else:
            print("Could not find movie in database")


def show_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            list_movies()
        elif selection == 'f':
            find_movie()
        else:
            print("Unknown command. Please try again")

        selection = input(MENU_PROMPT)


show_menu()
