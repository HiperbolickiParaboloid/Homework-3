from zad1 import Article
from zad2 import TechArticle
articles = []
categories = ["sports", "politics", "software_development", "economy", "law"]
titles = []

#unos objekata kroz input() i validacija

for i in range(1,5):
    while 1:
        print("Molimo unesite naslov clanka.")
        title = input()
        l = title.split(' ')
        counter = 0
        for rijec in l:
            if rijec.isalpha() == True:
                counter = counter + 1
        if counter == len(l) and len(title) <= 50 and title not in titles:
            titles.append(title)
            true_title = title
            break
        else:
            print('Nepravilan unos naslova! Provjerite broj karaktera i koristite samo alfabetske znakove. Ako je to u redu, onda je naslov duplikat, pa odaberite novi.')
    while 1:
        print("Molimo unesite autora clanka.")
        author = input()
        l = author.split(' ')
        counter = 0
        for rijec in l:
            if rijec.isalpha() == True:
                counter = counter +1
        if counter == len(l) and len(author) <= 100:
            true_author = author
            break
        else:
            print('Nepravilan unos! Provjerite broj karaktera i koristite samo alfabetske znakove.')
    while 1:
        print("Molimo unesite opis clanka.")
        description = input()
        if len(description) <= 300:
            true_description = description
            break
        else:
            print('Prekoracen broj karaktera! Maksimalno 300.')
    while 1:
        print("Molimo odaberite kategoriju clanka.")
        print(categories)
        new_category = input()
        category = new_category.lower()
        if category in categories:
            true_category = category
            break
        else:
            print("Morate odabrati jednu od ponudjenih kategorija.")
    while 1:
        print("Molimo unesite broj pregleda clanka.")
        views = input()
        if views.isdigit() == True:
            true_views = views
            break
        else:
            print('Molimo unesite ispravno broj pregleda.')
    article = Article(true_title, true_author, true_description, true_category, true_views, [])
    articles.append(article)

for i in range(1,3):
    while 1:
        print("Molimo unesite naslov clanka.")
        title = input()
        l = title.split(' ')
        counter = 0
        for rijec in l:
            if rijec.isalpha() == True:
                counter = counter + 1
        if counter == len(l) and len(title) <= 50 and title not in titles:
            titles.append(title)
            true_title = title
            break
        else:
            print('Nepravilan unos naslova! Provjerite broj karaktera i koristite samo alfabetske znakove. Ako je to u redu, onda je naslov duplikat, pa odaberite novi.')
    while 1:
        print("Molimo unesite autora clanka.")
        author = input()
        l = author.split(' ')
        counter = 0
        for rijec in l:
            if rijec.isalpha() == True:
                counter = counter +1
        if counter == len(l) and len(author) <= 100:
            true_author = author
            break
        else:
            print('Nepravilan unos! Provjerite broj karaktera i koristite samo alfabetske znakove.')
    while 1:
        print("Molimo unesite opis clanka.")
        description = input()
        if len(description) <= 300:
            true_description = description
            break
        else:
            print('Prekoracen broj karaktera! Maksimalno 300.')
    while 1:
        print("Molimo unesite broj pregleda clanka.")
        views = input()
        if views.isdigit() == True:
            true_views = views
            break
        else:
            print('Molimo unesite ispravno broj pregleda.')
    while 1:
        print("Molimo odaberite jezik na kome je napisan clanak. (en ili rs)")
        lang = input()
        if lang == 'en' or lang == 'rs':
            true_lang = lang
            break
        else:
            print ('Pogresan unos! Molimo pokusajte ponovo.')
    while 1:
        print("Molimo unesite datum kreiranja clanka.")
        creation_date = input()
        l = creation_date.split('/')  #pretpostavka je da je unos ispravan, tako kaze postavka zadatka
        if len(l[0]) < 2:
            l[0] = '0'+l[0]
        if len(l[1]) < 2:
            l[1] = '0'+l[1]
        new_creation_date = l[0]+'/'+l[1]+'/'+l[2]
        true_creation_date = new_creation_date
        break
    article = TechArticle(true_title, true_author, true_description, "TechArticle", true_views, [], true_creation_date, true_lang)
    articles.append(article)

#unos komentara kroz input()

article_names = []      #lista clanaka
comment_names = []      #lista komentara
for article in articles:
    article_names.append(article.get_title())
while 1:
    print("Molimo unesite naslov clanka koji zelite da komentarisete.")
    print(article_names)
    article_title = input()
    if article_title in article_names:
        while 1:
            print ("Molimo unesite naslov komentara.")
            comment_name = input()
            if comment_name not in comment_names:
                comment_names.append(comment_name)
                print ("Molimo unesite vase ime/nadimak.")
                comment_author = input()
                print ("Molimo unesite komentar.")
                comment_comment = input()
                for article in articles:
                    if article_title == article.get_title():
                        article.insert_new_comment(comment_name, comment_author, comment_comment)
                break
            else:
                print ("Nepravilan unos naslova. Pokusajte ponovo.")
    else:
        print ("Odaberite neki od ponudjenih clanaka.")
    print ("Ako zelite da komentarisete jos, molimo unesite DA.")
    stop = input()
    if stop == "DA":
        continue
    else:
        break

#filtriranje uz pomoc filter funkcije (pod b)

print("Unesite kategoriju za filtriranje.")     #pretpostaviti da je pravilan unos, ako ne samo treba provjriti da li je unos jednak nekom clanu liste categories
required_category = input()
def filter_by_category(article):
    category = article.get_category()
    if category == required_category:
        return True
    else:
        return False
filtered_by_category = list(filter(filter_by_category, articles))
for article in filtered_by_category:
    print (article)

#sortiranje i upisivanje u fajlove (pod c)

print ("Unesite kategoriju clanaka koje zelite sortirati po broju pregleda.")
required_category = input()
views_by_category = list(filter(filter_by_category, articles))
list_of_views = []          #lista sa izvucenim brojevima pregleda
for article in views_by_category:
    int_views = int(article.get_views())        #pretvaranje u int da bi se uspjesno izvrsilo sortiranje
    list_of_views.append(int_views)
list_of_views.sort(reverse = True)
new_list_of_views = []
for view in list_of_views:
    srt_views = str(view)        #vracanje u str kako bi moglo da se poredi sa onim sto vrati metod get_views()
    new_list_of_views.append(srt_views)
sorted_by_views = []            #lista clanaka sortiranih po broju pregleda, koju treba upisati u fajl
for view in new_list_of_views:
    for article in views_by_category:
        if view == article.get_views():
            sorted_by_views.append(article)
f = open(required_category + "_" + "sorted_by_views.txt", "w+")
for article in sorted_by_views:
    list_of_comments = article.get_comments()
    str_comments = ""
    for comment in list_of_comments:
        str_comments = str_comments + "|" + comment[2]
        str_commentss = str_comments[1:]
    if len(list_of_comments) == 0:
        file_comments = ""
    else:
        file_comments = str_commentss
    line = str(article.get_title()) + ";" + str(article.get_author()) + ";" + str(article.get_description())+ ";" + file_comments + ";" + str(article.get_views()) + "\n"
    f.write(line)
f.close()

#za sortiranje po broju komentara koristio sam isti kod, samo sto sam promijenio metode
#i nije bilo potrebe da sortiranu listu vracam u string kao iznad, jer metoda get_number_of_comments vraca int

print ("Unesite kategoriju clanaka koje zelite sortirati po broju komentara.")
required_category = input()
print(articles)
views_by_category = list(filter(filter_by_category, articles))
list_of_views = []          #lista sa izvucenim brojem komentara
for article in views_by_category:
    list_of_views.append(article.get_number_of_comments())
list_of_views.sort(reverse = True)
sorted_by_views = []            #lista clanaka sortiranih po broju komentara, koju treba upisati u fajl
for view in list_of_views:
    for article in views_by_category:
        if view == article.get_number_of_comments():
            sorted_by_views.append(article)
f = open(required_category + "_" + "sorted_by_comments.txt", "w+")
for article in sorted_by_views:
    list_of_comments = article.get_comments()
    str_comments = ""
    for comment in list_of_comments:
        str_comments = str_comments + "|" + comment[2]
        str_commentss = str_comments[1:]
    if len(list_of_comments) == 0:
        file_comments = ""
    else:
        file_comments = str_commentss
    line = str(article.get_title()) + ";" + str(article.get_author()) + ";" + str(article.get_description())+ ";" + file_comments + ";" + str(article.get_views()) + "\n"
    f.write(line)
f.close()