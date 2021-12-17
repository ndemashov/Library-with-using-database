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
        amount_book INT NOT NULL DEFAULT 0,
        PRIMARY KEY(id)
    );

    CREATE TABLE book(
        id SERIAL,
        title VARCHAR(50) NOT NULL,
        writing_year INT CHECK (writing_year<=2022),
        author INT NOT NULL,
        release_year INT NOT NULL,
        presence bool DEFAULT TRUE,
        PRIMARY KEY(id),
        FOREIGN KEY (author) REFERENCES author(id) ON DELETE CASCADE
    );
    CREATE INDEX ON book (title);

    CREATE TABLE reader(
        id SERIAL,
        surname VARCHAR(20) NOT NULL,
        name VARCHAR(20) NOT NULL,
        patronymic VARCHAR(20),
        PRIMARY KEY(id)
    );

    CREATE TABLE export(
        reader INT NOT NULL,
        book INT NOT NULL,
        loaning_date date NOT NULL,
        return_date date DEFAULT NULL,
        presence bool DEFAULT FALSE,
        FOREIGN KEY (book) REFERENCES book(id) ON DELETE CASCADE,
        FOREIGN KEY (reader) REFERENCES reader(id) ON DELETE CASCADE
    );
$$;

 CREATE OR REPLACE FUNCTION print_book()
    RETURNS TABLE(id integer, title VARCHAR(20), writing_year INT, author INT, release_year INT, presence bool)
    LANGUAGE plpgsql
    AS $$
    DECLARE
    BEGIN
    return query(
	    SELECT * FROM book
	);
    END
    $$;
    
    CREATE OR REPLACE FUNCTION print_author()
    RETURNS TABLE(id integer, surname varchar(20), name varchar(20), patronymic varchar(20), amount_book integer )
    LANGUAGE plpgsql
    AS $$
    DECLARE
    BEGIN
    return query(
	    SELECT * FROM author
	);
    END
    $$;
    
    CREATE OR REPLACE FUNCTION print_reader()
    RETURNS TABLE(id integer, sname VARCHAR(20), name VARCHAR(20), patronymic VARCHAR(20))
    LANGUAGE plpgsql
    AS $$
    DECLARE
    BEGIN
    return query(
	    SELECT * FROM reader
	);
    END
    $$;
    
    CREATE OR REPLACE FUNCTION print_export()
    RETURNS TABLE(reader INT, book INT, loaning_date date, return_date date, presence bool)
    LANGUAGE plpgsql
    AS $$
    DECLARE
    BEGIN
    return query(
	    SELECT * FROM export
	);
    END
    $$;
    """
def delete_library_table():
    return """
    CREATE OR REPLACE PROCEDURE delete_tables()
    LANGUAGE SQL
    AS $$
     DROP TABLE IF EXISTS author CASCADE;
     DROP TABLE IF EXISTS book CASCADE;
     DROP TABLE IF EXISTS reader CASCADE;
     DROP TABLE IF EXISTS export CASCADE;
$$;
    """
def filling_labrary_table():
    return """
        CREATE OR REPLACE PROCEDURE filling_tables()
        LANGUAGE SQL
        AS $$
            INSERT INTO author (surname, name, patronymic) VALUES ('Горький', 'Максим', NULL);
            INSERT INTO author (surname, name, patronymic) VALUES ('Достоевский', 'Фёдор', 'Михайлович'); 
            INSERT INTO author (surname, name, patronymic) VALUES ('Толстой', 'Лев', 'Николаевич'); 
            INSERT INTO author (surname, name, patronymic) VALUES ('Бунин', 'Иван', 'Алексеевич');  
            INSERT INTO author (surname, name, patronymic) VALUES ('Гоголь', 'Николай', 'Васильевич');  
            INSERT INTO author (surname, name, patronymic) VALUES ('Некрасов', 'Николай', 'Алексеевич'); 
            INSERT INTO author (surname, name, patronymic) VALUES ('Чехов', 'Антон', 'Павлович'); 
            INSERT INTO author (surname, name, patronymic) VALUES ('Булгаков', 'Михаил', 'Афанасьефич');  
            INSERT INTO author (surname, name, patronymic) VALUES ('Пушкин', 'Александр', 'Сергеевич');  
            INSERT INTO author (surname, name, patronymic) VALUES ('Лермонтов', 'Михаил', 'Юрьевич'); 
            
            
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
$$;
        """
def add_library_book():
    return """
    CREATE OR REPLACE PROCEDURE add_book(b_title varchar(50),
                                    b_writing_year INT,
                                    b_release_year INT,
                                    a_surname varchar(20),
                                    a_name varchar(20),
                                    a_patronymic varchar(20) DEFAULT NULL)
LANGUAGE plpgsql
AS $$
DECLARE
	id_author author.id%type;
BEGIN

    IF NOT EXISTS (SELECT surname, name, patronymic FROM author
    WHERE surname = a_surname AND name = a_name AND patronymic = a_patronymic)
    THEN
	INSERT INTO author (surname, name, patronymic) VALUES (a_surname, a_name, a_patronymic);

	IF a_patronymic <> NULL THEN
		SELECT id FROM author INTO id_author
		WHERE surname = a_surname AND name = a_name AND patronymic = a_patronymic;
	ELSE
		SELECT id FROM author INTO id_author
		WHERE surname = a_surname AND name = a_name;
	END IF;

	INSERT INTO book (title, writing_year, author, release_year) VALUES (b_title, b_writing_year, id_author, b_release_year);

	ELSE
		IF a_patronymic <> NULL THEN
			SELECT id FROM author INTO id_author
			WHERE surname = a_surname AND name = a_name AND patronymic = a_patronymic;
		ELSE
			SELECT id FROM author INTO id_author
			WHERE surname = a_surname AND name = a_name;
		END IF;
		INSERT INTO book (title, writing_year, author, release_year) VALUES (b_title, b_writing_year, id_author, b_release_year);
    END IF;
END
$$;
    """
def delete_by_key_word():
    return """
    CREATE OR REPLACE PROCEDURE delete_key_word(n_table VARCHAR (10), 
											key_word VARCHAR (50))
    LANGUAGE plpgsql
    AS $$
    BEGIN
        DELETE FROM book WHERE title = key_word;
    END
    $$;    
    """

def add_export():
    return """
    CREATE OR REPLACE PROCEDURE add_export(d date, r int, b int)
    LANGUAGE SQL
    AS $$
	    INSERT INTO export (reader, book, loaning_date, presence) VALUES (r, b, d, false);
	    update book set presence = false where id = b;
    $$;
    """

def presence_export():
    return """
    CREATE OR REPLACE PROCEDURE presence_export(d date, r int, b int)
    LANGUAGE SQL
    AS $$
	    update export set return_date = d, presence = true where reader = r and book = b;
	    update book set presence = true where id = b;
    $$;
    """

def clear_table():
    return """
    CREATE OR REPLACE PROCEDURE clear_table( t_name varchar(20) )
    LANGUAGE plpgsql
    AS $$
        DECLARE
	tbl text;
    BEGIN
	IF t_name = 'ALL' THEN
		FOR tbl IN 
			SELECT table_name FROM information_schema.tables WHERE table_schema='public'
		LOOP
  			EXECUTE format('TRUNCATE TABLE %I CASCADE', tbl);
		END LOOP;
	ELSE	
    	EXECUTE format('TRUNCATE TABLE %I CASCADE', t_name);
	END IF;
    END
    $$;
    """

def add_reader():
    return """
    CREATE OR REPLACE PROCEDURE add_reader(s varchar, n varchar, p varchar)
    LANGUAGE SQL
    AS $$
	    INSERT INTO reader (surname, name, patronymic) VALUES(s, n, p)
    $$;
    """
def delete_entry():
    return """
    CREATE OR REPLACE PROCEDURE delete_entry( t_name varchar(20), entry_id integer )
    LANGUAGE plpgsql
    AS $$
	BEGIN
		EXECUTE format('DELETE FROM %I CASCADE WHERE id = $1;', t_name) USING entry_id;
	END
	$$;
    """