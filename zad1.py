class Article:
    def __init__(self, title, author, description, category, views = 0, comments = []):
        self.__title = title
        self.__author = author
        self.__description = description
        self.__category = category
        self.__views = views
        self.__comments = comments
        #self.__number_of_comments = len(comments)
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_description(self):
        return self.__description
    def get_category(self):
        return self.__category
    def get_views(self):
        return self.__views
    def get_comments(self):
        return self.__comments
    def get_number_of_comments(self):
        return len(self.__comments)
    def set_title(self, new_title):
        l = new_title.split(' ')
        counter = 0
        for rijec in l:
            if rijec.isalpha() == True:
                counter = counter + 1
        if counter == len(l) and len(new_title) <= 50:
            self.__title = new_title
        else:
            print('Nepravilan unos!')
    def set_author(self, new_author):
        l = new_author.split(' ')
        counter = 0
        for rijec in l:
            if rijec.isalpha() == True:
                counter = counter +1
        if counter == len(l) and len(new_author) <= 100:
            self.__author = new_author
        else:
            print('Nepravilan unos!')
    def set_description(self, new_description):
        if len(new_description) <= 300:
            self.__description = new_description
        else:
            print('Prekoracen broj karaktera! Maksimalno 300.')
    def set_category(self, new_category):
        if len(new_category) <= 20:
            self.__category = new_category
        else:
            print('Prekoracen broj karaktera! Maksimalno 20.')
    def set_views(self, new_views):
        if new_views.isdigit() == True:
            self.__views = new_views
        else:
            print('Molimo unesite ispravno broj pregleda.')
    def insert_new_comment(self,title, author, comment):
        self.__comments.append((title, author, comment))
    def delete_comment_by_title(self, title):
        for comment in self.__comments:
            if comment[0] == title:
                self.__comments.remove(comment)
    def delete_comment_by_author(self, author):
        for comment in self.__comments:
            if comment[1] == author:
                self.__comments.remove(comment)
    def get_comment_by_title(self, title):
        for comment in self.__comments:
            if comment[0] == title:
                return comment
    def get_comment_by_author(self, author):
        for comment in self.__comments:
            if comment[1] == author:
                return comment
    def inc_views(self, num=1):
        self.__views = self.__views + num
    def __str__(self):
        return f'title: {self.__title}, author: {self.__author}, description: {self.__description}, category: {self.__category}, views: {self.__views}, number_of_comments: {len(self.__comments)}'