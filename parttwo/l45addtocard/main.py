from models.book import Book
from models.user import User

from models.utilities import gettitles, specialdiscount

# from models.utilities import *


def main():
    bookObj1 = Book("Python", "Daw Win Win", 20, 500)
    bookObj2 = Book("Javascript", "Daw Aye Aye", 30, 300)
    bookObj3 = Book("Php", "Su Su", 100, 1000)
    bookObj4 = Book("C", "Daw Zin Mar", 50, 20)

    # ? Original Price
    specialdiscount(bookObj1)
    specialdiscount(bookObj2)
    # ? discount
    # ? user
    user = User("Aung Kyaw")
    user.addtocart(bookObj1)
    user.addtocart(bookObj2)

    print("Book Titles: ", gettitles(user.carts))
    print(f"Total Pages in book 1= {len(bookObj1)}")
    print(f"Total Pages in book 2= {len(bookObj2)}")

    print(user)

    print(f"Total Price: {user.totalprice():.2f}")


if __name__ == "__main__":
    main()


# ? app logic
# ? Book
# ? User
# ? Original Price : 100 10%
# ? After Discount Price : 90
# ? Book Title : [, , ,]
# ? book 1 pages : 10
# ? book 2 pages : 15
# ? book 3 pages : 14
# ? User: SuSu, Card:["Story One by nu nu","Story Two by yu yu"]
# ? Total Price : 90
