class classproperty:
    def __init__(self, func):  # Stores the function
        self.func = func

    def __get__(self, obj, cls=None):  # ? make it work like a property(no () needed)
        return self.func(cls)


class Greet:
    # _greeting = "Hello Mandalay"
    greeting = "Hello Mandalay"

    @classproperty
    def sayhi(cls):
        # return cls._greeting
        return cls.greeting


print(Greet.sayhi)


# Method override in Subclass


class SocialMedia:
    @classproperty
    def category(cls):
        return "Generic Social Platform"


class Facebook(SocialMedia):
    @classproperty
    def category(cls):
        return "Social Network"


class YouTube(SocialMedia):
    @classproperty
    def category(cls):
        return "Video Sharing"


print(SocialMedia.category)
print(Facebook.category)
print(YouTube.category)
