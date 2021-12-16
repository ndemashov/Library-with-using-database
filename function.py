# Здесь будут реальзованы хранимые функции типа print_author
def trigger_function():
    return """
    CREATE OR REPLACE FUNCTION increase()
    RETURNS trigger AS
    $$
    DECLARE
    author_id book.author%TYPE;
    delta INT;
    BEGIN
        IF TG_OP = 'INSERT' THEN
            delta = 1;
            author_id = NEW.author;
        ELSIF TG_OP = 'DELETE' THEN
            delta = -1;
            author_id = OLD.author;
        END IF;
        UPDATE author SET amount_book = amount_book + delta
        WHERE author.id = author_id;
        RETURN NULL;
    END
    $$ LANGUAGE plpgsql;
    """
def trigger():
    return """
    CREATE TRIGGER increase_amount_book AFTER INSERT OR DELETE ON book
    FOR EACH ROW EXECUTE PROCEDURE increase();
    """