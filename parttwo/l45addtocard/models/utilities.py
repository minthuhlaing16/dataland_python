def pricestatusdecorator(func):
    def wrapper(book):
        print(
            f"Original Price = {book.getprice():.3f}"
        )  # ? format specification, full column ka format spec tway sa tone top mal so lol tar, .3 -> 3 decimal places,f -> fixed point notation
        func(book)
        print(f"After Discount Price = {book.getprice():.3f}")

    return wrapper


@pricestatusdecorator
def specialdiscount(book):
    book.applydiscount(10)
    # book.applydiscount(0.1)


def gettitles(books):
    return list(map(lambda book: book.title, books))
