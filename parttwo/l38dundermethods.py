#
# ? Dunder Methods ==>  __init__ , PHP ==> Magic Methods

# ? __len__ , __add__
from typing import Self


class Article:
    def __init__(self, title: str, rating: int) -> None:
        self.title = title
        self.rating = rating

    def __len__(self) -> int:
        return self.rating

    def __add__(self, other: Self) -> Self:
        combinetitle: str = f"{self.title} && {other.title}"
        combinerating: int = self.rating + other.rating
        return Article(combinetitle, combinerating)


def main() -> None:  # ? function, outside of the class
    sport: Article = Article("This is sport article", 3)
    news: Article = Article("This is news article", 5)

    print(sport.title)
    print(sport.rating)
    print(len(sport))

    print(news.title)
    print(news.rating)
    print(len(news))
    print(news.__len__())  # ! Not recommended

    mixarticles: Article = sport + news
    print(mixarticles)
    print(mixarticles.title)
    print(mixarticles.rating)


if __name__ == "__main__":
    main()

    #  ==> __eq__

    class Mobile:
        def __init__(self, brand: str, price: int, color: str) -> None:
            self.brand = brand
            self.price = price
            self.color = color

        # ? Check only price is equal or not
        # def __eq__(self, other: Self) -> bool:
        #     return self.price == other.price

        # ? Check all parameters equal or not
        def __eq__(self, other: Self) -> bool:
            print("Current = ", self.__dict__)
            print("Other = ", other.__dict__)
            return self.__dict__ == other.__dict__

    def main() -> None:
        mob1: Mobile = Mobile("Oppo", 300, "blue")
        mob2: Mobile = Mobile("Oppo", 300, "blue")

        print(mob1)
        print(mob1.brand)
        print(mob1.price)
        print(mob1.color)

        print(mob2)
        print(mob2.brand)
        print(mob2.price)
        print(mob2.color)
        print(mob1 == mob2)  # ? False before eq


if __name__ == "__main__":
    main()
