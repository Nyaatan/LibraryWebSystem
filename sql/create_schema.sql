create table "Author"
(
    author_id integer not null
        constraint author_pk
            primary key,
    first_name varchar(32),
    last_name  varchar(32),
    nickname   varchar(64)
);

create table "Category"
(
    category_id integer     not null
        constraint category_pk
            primary key,
    name        varchar(32) not null,
    description varchar(128)
);

create table "Book"
(
    book_id     integer      not null
        constraint book_pk
            primary key,
    title       varchar(128) not null,
    category_id integer      not null
        constraint book_category_id_fk
            references "Category"
);


create table "BookAuthor"
(
    book_id   integer not null
        constraint bookauthor_book_id_fk
            references "Book",
    author_id integer not null
        constraint bookauthor_author_id_fk
            references "Author"
);

create table "Publisher"
(
    publisher_id   integer     not null
        constraint publisher_pk
            primary key,
    name varchar(64) not null
);

create table "Edition"
(
    isbn         bigint not null
        constraint edition_pk
            primary key,
    number       integer,
    page_count   integer not null,
    date         date    not null,
    book_id      integer not null
        constraint edition_book_id_fk
            references "Book",
    publisher_id integer not null
        constraint edition_publisher_id_fk
            references "Publisher"
);

create table "Subscription"
(
    subscription_id              integer not null
        constraint subscription_pk
            primary key,
    name            varchar(16) not null,
    price           integer not null,
    borrowing_count integer not null
);

create table "Card"
(
    card_id     integer     not null
        constraint card_pk
            primary key,
    number varchar(16) not null,
    token  varchar(32) not null
);

create table "User"
(
    user_id                   integer     not null
        constraint user_pk
            primary key,
    name                 varchar(16) not null,
    email                varchar(32) not null,
    hash                 varchar(256) not null,
    borrowings_remaining integer     not null,
    subscription_id      integer     not null
        constraint user_subscription_id_fk
            references "Subscription",
    card_id              integer
        constraint user_card_id_fk
            references "Card"
);

create table "Borrowing"
(
    borrowing_id           integer not null
        constraint borrowing_pk
            primary key,
    start_date   date    not null,
    end_date     date    not null,
    isbn bigint not null
        constraint borrowing_edition_isbn_fk
            references "Edition",
    user_id      integer not null
        constraint borrowing_user_id_fk
            references "User"
);

create table "Payments"
(
    payments_id      integer        not null
        constraint payments_pk
            primary key,
    amount  numeric(10, 2) not null,
    date    date           not null,
    user_id integer        not null
        constraint payments_user_id_fk
            references "User"
);

create view "Current_borrows"(user_id, isbn, title, first_name, last_name, nickname, start_date) as
SELECT u.user_id,
       e.isbn,
       b.title,
       a.first_name,
       a.last_name,
       a.nickname,
       bo.start_date
FROM "User" u
         JOIN "Borrowing" bo USING (user_id)
         JOIN "Edition" e USING (isbn)
         JOIN "Book" b USING (book_id)
         JOIN "BookAuthor" USING (book_id)
         JOIN "Author" a USING (author_id);

create view "Available_books"(title, first_name, last_name, nickname, name, number) as
SELECT b.title,
       a.first_name,
       a.last_name,
       a.nickname,
       p.name,
       e.number
FROM "Book" b
         JOIN "BookAuthor" USING (book_id)
         JOIN "Author" a USING (author_id)
         JOIN "Edition" e USING (book_id)
         JOIN "Publisher" p USING (publisher_id);

create view "User_data"(user_id, name, email, hash, borrowings_remaining) as
SELECT "User".user_id,
       "User".name,
       "User".email,
       "User".hash,
       "User".borrowings_remaining
FROM "User"
with local check option;

create index author_last_name_first_name_index
    on "Author" (last_name, first_name);

create index author_nickname_index
    on "Author" (nickname);
	
create index book_title_index
    on "Book" (title);

create index category_name_index
    on "Category" (name);

create index publisher_name_index
    on "Publisher" (name);
	
create unique index subscription_name_index
    on "Subscription" (name);

create unique index user_email_index
    on "User" (email);

create unique index user_name_index
    on "User" (name);
	
create index end_date_index 
	on "Borrowing" (end_date desc);

create procedure delete_old_borrows() 
    LANGUAGE plpgsql
AS $$
    BEGIN
        delete from "Borrowing"
        where end_date > (NOW() - INTERVAL '6 months');
    end
$$;

CREATE FUNCTION subtract_borrow_amount_funtion()
    RETURNS TRIGGER
    LANGUAGE plpgsql
AS $$
    DECLARE borrows_left INT;
    BEGIN
        SELECT borrowings_remaining INTO borrows_left FROM "User" where user_id = NEW.user_id;
        IF borrows_left > 0 THEN
            UPDATE "User" SET borrowings_remaining = borrows_left - 1 where user_id = NEW.user_id;
        END IF;
        RETURN NEW;
    END
$$;

CREATE TRIGGER subtract_borrow_amount AFTER INSERT
    ON "Borrowing"
    FOR EACH ROW
    EXECUTE PROCEDURE subtract_borrow_amount_funtion();

CREATE USER "Admin"
    login
    password 'admin'
    superuser
	createrole
	noinherit
	CONNECTION LIMIT 1;

create user "Client"
    password 'client'
	noinherit;

GRANT SELECT, UPDATE (number)
ON "Card"
TO "Client";

GRANT UPDATE (name, email, hash)
ON "User_data"
TO "Client";

GRANT SELECT (borrowings_remaining)
ON "User_data"
TO "Client";

GRANT SELECT
ON "Subscription"
TO "Client";

GRANT SELECT
ON "User_data", "Available_books", "Current_borrows"
TO "Client";

