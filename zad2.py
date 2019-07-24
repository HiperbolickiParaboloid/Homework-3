from zad1 import Article
class TechArticle(Article):
    def __init__(self, title, author, description, category, views, comments = [], creation_date = "01/01/2000", lang = "en"):
        super().__init__(title, author, description, category, views, comments)
        self.__creation_date = creation_date
        self.__lang = lang 
    def get_lang(self):
        return self.__lang
    def get_creation_date(self):
        return self.__creation_date
    def set_lang(self, new_lang):
        if new_lang == 'en' or new_lang == 'rs':
            self.__lang = new_lang
        else:
            print ('Pogresan unos!')
    def set_creation_date(self, new_creation_date):
        l = new_creation_date.split('/')  #pretpostavka je da je unos ispravan, tako kaze postavka zadatka
        if len(l[0]) < 2:
            l[0] = '0'+l[0]
        if len(l[1]) < 2:
            l[1] = '0'+l[1]
        newest_creation_date = l[0]+'/'+l[1]+'/'+l[2]
        self.__creation_date = newest_creation_date
    def get_comments_by_term(self, term):
        lista = []
        comments = self.get_comments()
        for comment in comments:
            if comment[0].startswith(term) == True:
                lista.append(comment)
        return lista
    def __str__(self):
        return f'title: {self.get_title()}, author: {self.get_author()}, description: {self.get_description()}, category: {self.get_category()}, views: {self.get_views()}, number_of_comments: {len(self.get_comments())}, creation_date: {self.__creation_date}, language: {self.__lang}'