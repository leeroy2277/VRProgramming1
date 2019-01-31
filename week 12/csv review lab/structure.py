import datetime

class Document:

    def __init__(self, author: str[], date):

        self.author = author

        self.date = datetime.datetime.now()


    def get_Authors(self):

        return self.author


    def add_Author(self, name):

        self.author.append(name)


    def get_Date(self):

        return self.date



class Book(Document):

    def __init__(self, title: str, author, date):

        self.title = title

        super().__init__(author, date)



    def getTitle(self):

        return self.title


class Email(Document):
    def __init__(self, subject: str, to: str[]):

        self.subject = subject

        self.to = to

        super().__init__(subject, to)

    def get_Subject(self):

        return self.subject

    def get_To(self):

        return self.to
