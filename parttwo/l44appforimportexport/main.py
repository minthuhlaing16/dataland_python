from manage import BookManage


def main():
    manage = BookManage()

    # * Add book
    manage.addbook("Harry Potter", "John Doe", 2022)
    manage.addbook("Fast and Furious", "Alice", 1999)
    manage.addbook("Game of Throne", "Bob", 2013)
    manage.addbook("Lord of Ring", "John Doe", 2014)
    manage.addbook("King of Viper", "Hla Hla", 2015)
    manage.addbook("Dracular", "John Doe", 2016)

    # * List Books
    manage.listbooks()

    # * Search by author
    authorname = "John Doe"
    filterresults = manage.searchbyauthor(authorname)
    print(f"Book by {authorname}")

    for book in filterresults:
        print(f"{book.title} public in {book.year}")


if __name__ == "__main__":
    main()
