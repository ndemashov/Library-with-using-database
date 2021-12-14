def create_library_tabel():
    return """ 
    CREATE OR REPLACE PROCEDURE create_tables()
    LANGUAGE SQL
    AS $$
     CREATE TABLE author(
        id SERIAL,
        surname VARCHAR(20) NOT NULL,
        name VARCHAR(20) NOT NULL,
        patronymic VARCHAR(20),
        amount_book INT,
        PRIMARY KEY(id)
    );

    CREATE TABLE book(
        id SERIAL,
        title VARCHAR(50) NOT NULL,
        writing_year INT CHECK (writing_year<=2022),
        author INT NOT NULL,
        release_year INT NOT NULL,
        PRIMARY KEY(id),
        FOREIGN KEY (author) REFERENCES author(id)
    );
    CREATE INDEX ON book (title);

    CREATE TABLE reader(
        id SERIAL,
        surname VARCHAR(20) NOT NULL,
        name VARCHAR(20) NOT NULL,
        patronymic VARCHAR(20),
        PRIMARY KEY(id)
    );
    
    CREATE TABLE phone(
        reader_id INT NOT NULL,
        phone INT,
        FOREIGN KEY (reader_id) REFERENCES reader(id)
    );

    CREATE TABLE export(
        reader INT NOT NULL,
        book INT NOT NULL,
        loaning_date date NOT NULL,
        return_date date DEFAULT NULL,
        presence bool DEFAULT FALSE,
        FOREIGN KEY (book) REFERENCES book(id),
        FOREIGN KEY (reader) REFERENCES reader(id)
    );
$$;
    """
def delete_library_table():
    return """
    CREATE OR REPLACE PROCEDURE delete_tables()
    LANGUAGE SQL
    AS $$
     DROP TABLE author CASCADE;
     DROP TABLE book CASCADE;
     DROP TABLE reader CASCADE;
     DROP TABLE phone CASCADE;
     DROP TABLE export CASCADE;
$$;
    """
def filling_labrary_table():
    return """
        CREATE OR REPLACE PROCEDURE filling_tables()
        LANGUAGE SQL
        AS $$
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Горький', 'Максим', NULL, 3);
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Достоевский', 'Фёдор', 'Михайлович', 4); 
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Толстой', 'Лев', 'Николаевич', 3); 
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Бунин', 'Иван', 'Алексеевич', 2);  
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Гоголь', 'Николай', 'Васильевич', 4);  
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Некрасов', 'Николай', 'Алексеевич', 3); 
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Чехов', 'Антон', 'Павлович', 4); 
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Булгаков', 'Михаил', 'Афанасьефич', 2);  
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Пушкин', 'Александр', 'Сергеевич', 5);  
            INSERT INTO author (surname, name, patronymic, amount_book) VALUES ('Лермонтов', 'Михаил', 'Юрьевич', 4); 
            
            
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Вишневый сад', 1903, 7, 1968); 
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Темные аллеи', 1944, 4, 1977);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Война и мир', 1863, 3, 1984);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Дуэль', 1891, 7, 1967);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Мертвые души', 1841, 5, 1875);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('На Дне', 1901, 1, 1963);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Герои нашего времени', 1840, 10, 1965);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Мертвые души', 1841, 5, 1865);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Мать', 1898, 4, 1969);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Русские женщины', 1872, 6, 1995);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Евгений Онегин', 1833, 9, 1979);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Детство', 1913, 1, 1983);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Шинель', 1842, 5, 1874);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Демон', 1839, 10, 1955);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Преступление и наказание', 1866, 2, 1963);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Детство', 1852, 3, 1961);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Борис Годунов', 1831, 9, 1969);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Вишневый сад', 1903, 7, 1998); 
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Маленькие трагедии', 1830, 9, 1959);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Преступление и наказание', 1866, 2, 1983);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Крестьянские дети', 1861, 6, 1988);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Мастер и Маргарита', 1940, 8, 1999);

            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Моцарт и Сальери', 1832, 9, 1989);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Идиот', 1869, 2, 1973);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('На охоте', 1884, 7, 1965); 
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Шинель', 1842, 5, 1865);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Кому на Руси жить хорошо', 1874, 6, 1975);

            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Война и мир', 1863, 3, 1994);

            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Скупой рыцарь', 1830, 9, 1985);

            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Исповедь', 1831, 10, 1963);

            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Мать', 1906, 1, 1972);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Мастер и Маргарита', 1940, 8, 1989);
          
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Кавказец', 1841, 10, 1978);
            INSERT INTO book (title, writing_year, author, release_year) VALUES ('Идиот', 1869, 2, 1993);
            
            INSERT INTO reader (surname, name, patronymic) VALUES ('Команов', 'Михаил', 'Александрович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Аратан', 'Кузьма', 'Вячеславович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Тамашнев', 'Тимофей', 'Петрович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Туташнев', 'Дмитрий', 'Карапузович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Наднамышнев', 'Иван', 'Федорович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Найденов', 'Антон', 'Рюрикович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Катавец', 'Сергей', 'Романович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Горапик', 'Арарат', 'Тутанович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Зеленов', 'Михаил', 'Петрович');
            INSERT INTO reader (surname, name, patronymic) VALUES ('Найденов', 'Александр', 'Александрович');
            
            INSERT INTO phone (reader_id, phone) VALUES (1, 123413);
            INSERT INTO phone (reader_id, phone) VALUES (1, 3483434);
            INSERT INTO phone (reader_id, phone) VALUES (2, 456376);
            INSERT INTO phone (reader_id, phone) VALUES (3, 543434);
            INSERT INTO phone (reader_id, phone) VALUES (4, 5343453);
            INSERT INTO phone (reader_id, phone) VALUES (5, 3435434);
            INSERT INTO phone (reader_id, phone) VALUES (6, 5343446);
            INSERT INTO phone (reader_id, phone) VALUES (7, 5346545);
            INSERT INTO phone (reader_id, phone) VALUES (8, 5344544);
            INSERT INTO phone (reader_id, phone) VALUES (9, 4333453);
            INSERT INTO phone (reader_id, phone) VALUES (10, 6755454);
            
            INSERT INTO export (reader, book, loaning_date, return_date, presence) VALUES (1, 3, '14.12.2012', NULL, FALSE);
            INSERT INTO export (reader, book, loaning_date, return_date, presence) VALUES (1, 5, '14.12.2012', NULL, FALSE);
            INSERT INTO export (reader, book, loaning_date, return_date, presence) VALUES (1, 6, '14.12.2012', NULL, FALSE);
            INSERT INTO export (reader, book, loaning_date, return_date, presence) VALUES (3, 7, '14.12.2012', NULL, FALSE);
            INSERT INTO export (reader, book, loaning_date, return_date, presence) VALUES (2, 9, '14.12.2012', NULL, FALSE);
$$;
        """
