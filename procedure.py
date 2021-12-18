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

            CALL add_book('Вишневый сад', 1903, 1968, 'Чехов', 'Антон', 'Павлович');
            CALL add_book('Темные аллеи', 1944,  1977, 'Бунин', 'Иван', 'Алексеевич');
            CALL add_book('Война и мир', 1863, 1984, 'Толстой', 'Лев', 'Николаевич');
            CALL add_book('Дуэль', 1891, 1967, 'Чехов', 'Антон', 'Павлович');
            CALL add_book('Мертвые души', 1841, 1875, 'Гоголь', 'Николай', 'Васильевич');
            CALL add_book('На Дне', 1901, 1963, 'Пешков', 'Алексей', 'Максимович');
            CALL add_book('Герои нашего времени', 1840, 1965, 'Лермонтов', 'Михаил', 'Юрьевич');
            CALL add_book('Мертвые души', 1841, 1865, 'Гоголь', 'Николай', 'Васильевич');
            CALL add_book('Мать', 1898, 1969, 'Бунин', 'Иван', 'Алексеевич');
            CALL add_book('Русские женщины', 1872, 1995, 'Некрасов', 'Николай', 'Алексеевич');
            CALL add_book('Евгений Онегин', 1833,1979, 'Пушкин', 'Александр', 'Сергеевич');
            CALL add_book('Детство', 1913, 1983, 'Пешков', 'Алексей', 'Максимович');
            CALL add_book('Шинель', 1842, 1874, 'Гоголь', 'Николай', 'Васильевич');
            CALL add_book('Демон', 1839, 1955, 'Лермонтов', 'Михаил', 'Юрьевич');
            CALL add_book('Преступление и наказание', 1866, 1963, 'Достоевский', 'Фёдор', 'Михайлович');
            CALL add_book('Детство', 1852, 1961, 'Толстой', 'Лев', 'Николаевич');
            CALL add_book('Борис Годунов', 1831, 1969, 'Пушкин', 'Александр', 'Сергеевич');
            CALL add_book('Вишневый сад', 1903, 1998, 'Чехов', 'Антон', 'Павлович');
            CALL add_book('Маленькие трагедии', 1830, 1959, 'Пушкин', 'Александр', 'Сергеевич');
            CALL add_book('Преступление и наказание', 1866, 1983, 'Достоевский', 'Фёдор', 'Михайлович');
            CALL add_book('Крестьянские дети', 1861, 1988, 'Некрасов', 'Николай', 'Алексеевич');
            CALL add_book('Мастер и Маргарита', 1940, 1998, 'Булгаков', 'Михаил', 'Афанасьефич');
            CALL add_book('Моцарт и Сальери', 1832, 1989, 'Пушкин', 'Александр', 'Сергеевич');
            CALL add_book('Идиот', 1869, 1973, 'Достоевский', 'Фёдор', 'Михайлович');
            CALL add_book('На охоте', 1884, 1965, 'Чехов', 'Антон', 'Павлович');
            CALL add_book('Шинель', 1842, 1865, 'Гоголь', 'Николай', 'Васильевич');
            CALL add_book('Кому на Руси жить хорошо', 1874, 1975, 'Некрасов', 'Николай', 'Алексеевич');
            CALL add_book('Война и мир', 1863, 1994, 'Толстой', 'Лев', 'Николаевич');
            CALL add_book('Скупой рыцарь', 1830, 1985, 'Пушкин', 'Александр', 'Сергеевич');
            CALL add_book('Исповедь', 1831, 1963, 'Лермонтов', 'Михаил', 'Юрьевич');
            CALL add_book('Мать', 1906, 1972, 'Пешков', 'Алексей', 'Максимович');
            CALL add_book('Мастер и Маргарита', 1940, 1989, 'Булгаков', 'Михаил', 'Афанасьефич');
            CALL add_book('Кавказец', 1841, 1978, 'Лермонтов', 'Михаил', 'Юрьевич');
            CALL add_book('Идиот', 1869, 1993, 'Достоевский', 'Фёдор', 'Михайлович');

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

	SELECT id FROM author INTO id_author
	WHERE surname = a_surname AND name = a_name AND patronymic = a_patronymic;

	INSERT INTO book (title, writing_year, author, release_year) VALUES (b_title, b_writing_year, id_author, b_release_year);

	ELSE
		SELECT id FROM author INTO id_author
		WHERE surname = a_surname AND name = a_name AND patronymic = a_patronymic;
	    INSERT INTO book (title, writing_year, author, release_year) VALUES (b_title, b_writing_year, id_author, b_release_year);
    END IF;
END
$$;
    """


def delete_by_key_word():
    return """
    CREATE OR REPLACE PROCEDURE delete_key_word(n_table VARCHAR (10), 
                                                field VARCHAR (10),
											    key_word VARCHAR (50))
    LANGUAGE plpgsql
    AS $$
    BEGIN
		EXECUTE format('DELETE FROM %I CASCADE WHERE %I = $1;', n_table, field) USING key_word;
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


def find_by_key_word():
    return """
    CREATE OR REPLACE FUNCTION find_key_word_from_author(key_word VARCHAR (50))
	RETURNS TABLE(id integer, surname varchar(20), name varchar(20), patronymic varchar(20), amount_book integer )
    LANGUAGE plpgsql
    AS $$
    BEGIN
		return query(SELECT * FROM author WHERE author.surname = $1);
    END
    $$;

    CREATE OR REPLACE FUNCTION find_key_word_from_book(key_word VARCHAR (50))
	RETURNS TABLE(id integer, title VARCHAR(20), writing_year INT, author INT, release_year INT, presence bool)
    LANGUAGE plpgsql
    AS $$
    BEGIN
		return query(SELECT * FROM book WHERE book.title = $1);
    END
    $$;

    CREATE OR REPLACE FUNCTION find_key_word_from_reader(key_word VARCHAR (50))
	RETURNS TABLE(id integer, sname VARCHAR(20), name VARCHAR(20), patronymic VARCHAR(20))
    LANGUAGE plpgsql
    AS $$
    BEGIN
		return query(SELECT * FROM reader WHERE reader.name = $1);
    END
    $$;

    CREATE OR REPLACE FUNCTION find_key_word_from_export(key_word VARCHAR (50))
	RETURNS TABLE(reader INT, book INT, loaning_date date, return_date date, presence bool )
    LANGUAGE plpgsql
    AS $$
    BEGIN
		return query(SELECT * FROM export WHERE export.loaning_date = $1);
    END
    $$;
    
    CREATE OR REPLACE FUNCTION show_book( b_title varchar(50) )
RETURNS TABLE(title varchar(15), surname varchar(15), name varchar(15))
LANGUAGE plpgsql
AS $$
BEGIN
return query(
    SELECT book.title, author.surname, author.name FROM book
	INNER JOIN author ON book.author = author.id
	WHERE book.title = b_title
    );
END
$$;
    """