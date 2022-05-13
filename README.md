# CeneoScraper

## struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa opinii|Selektor|Nazwa zmiennej|Typ danych|
|---------------|--------|--------------|----------|
|opinia|div.js_product-review|opinion|bs4.element.Tag|
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|opinion_id|str|
|autor opinii| span.user-post__author-name|author|str|
|rekomendacja autora|span.user-post__author-recomendation > em|recommendation|str|
|liczba gwiazdek|span.user-post__score-count|stars|str|
|treść opinii|div.user-post__text|content|str|
|lista zalet|div[class$=positives\] ~ div.review-feature__item|pros||
|lista wad|div[class$=negatives\] ~ div.review-feature__item|cons||
|dla ilu osób przydatna|button.vote-yes > span|useful||
|dla ilu osób nieprzydatna|button.vote-no > span|useless||
|data wystawienia opinii|span.user-post__published > time:nth-child(1)\["datetime"\]|published||
|data zakupu produktu|span.user-post__published > time:nth-child(2)\["datetime"\]|purchased||

## etapy pracy nad projektem strukturalnym
1.Pobranie elementów pojedynczej opinii do niezależnych zmiennych 
2. Zapisanie wszystkich elementów pojedynczej opinii do jednej zmiennej \słownik\
3. Pobranie wszystkich opinii z pojedynczej strony do słowników i dodanie ich do listy
4. Pobranie wszystkich opinii o produkcie z wszystkich stron i zapisanie ich do pliku json
5. Dodanie możliwości podania id produktu przez użytkownika za pomocą klawiatury
6. Refakturyzacja (optymalizacja) kodu:
    a. Stworzenie funkcji do pobierania składowych strony HTML
    b. Utworzenie słownika opisującego strukturę opinii wraz z selektorami poszczególnych elementów
    c. Zamiana instrukcji pobierających składowe opinii do pojedynczych zmiennych i tworzenie z nich słownik na wyrażenie słownikowe tworzące słownik reprezentujący pojedynczą opinię na podstawie słownika selektorów
7. Analiza opinii o wybranym produkcie
    a. wczytaniewszystkich opinii o wskazanym produkcie do obiektu DataFrame
    b. wylicznie podstawowych statystyk na podstawie opinii
        b1. liczba wszystkich opinii o produkcie
        b2. liczba opinii w których autor poda listę zalet produktu
        b3. liczba opinii w których autor poda listę wad produktu
        b4. średnia ocena produktu
    c. przygotowanie wykresów na podstawie zawartości opinii
        c1. udział poszczególnych rekomendacji w ogólnej liczbie opinii
        c2. histogram częstości występowanie poszczególnych ocen (liczby gwiazdek)
