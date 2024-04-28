import string


class Pagination:
    def __init__(self, items=None, page_size=1):
        self.items = items
        self.page_size = page_size
        self.page = 0

    def getContentBySimbols(self):
        result = []
        for i in range(0, len(self.items), self.page_size):
            result.append(list(self.items[i:i + self.page_size]))
        return result

    def getVisibleItems(self):
        content = self.getContentBySimbols()
        return content[self.page]

    def nexPage(self):
        if self.page + 1 <= len(self.getContentBySimbols()):
            self.page += 1
        else:
            raise ValueError("no next page")

    def prevPage(self):
        if self.page - 1 >= 0:
            self.page -= 1
        else:
            raise ValueError("you are on the first page")

    def lastPage(self):
        self.page = len(self.getContentBySimbols()) - 1

    def firstPage(self):
        self.page = 0

    def goToPage(self, number):
        if number > len(self.getContentBySimbols()) - 1:
            self.page = len(self.getContentBySimbols()) - 1
        elif number < 1:
            self.page = 0
        else:
            self.page = number

    def __str__(self):
        result = f"Page: {self.page + 1}\nContent: {self.getVisibleItems()}"
        return result


def main():
    my_content = "Hi! My name is Maria and this is my test. I'll make my sentence a little bit longer"
    content = Pagination(my_content, 10)
    print(content)
    content.nexPage()
    print(content)
    content.nexPage()
    content.nexPage()
    print(content)
    content.goToPage(6)
    print(content)
    content.firstPage()
    print(content)
    content.lastPage()
    print(content)


if __name__ == "__main__":
    main()
