INSERT INTO "Subscription"(subscription_id, name, price, borrowing_count) VALUES(0, 'None', 0, 2);
INSERT INTO "Subscription"(subscription_id, name, price, borrowing_count) VALUES(1, 'Basic', 10, 5);
INSERT INTO "Subscription"(subscription_id, name, price, borrowing_count) VALUES(2, 'Bookworm', 20, 15);
INSERT INTO "Subscription"(subscription_id, name, price, borrowing_count) VALUES(3, 'No-life', 30, 45);
INSERT INTO "Author"(author_id, first_name, last_name, nickname) VALUES (0,  'Russell', 'Jenkins', null);
INSERT INTO "Author"(author_id, first_name, last_name, nickname) VALUES (1,  'Ronald', 'Martinez', 'qwerty');
INSERT INTO "Author"(author_id, first_name, last_name, nickname) VALUES (2,  'Josef', 'Čermák', null);
INSERT INTO "Author"(author_id, first_name, last_name, nickname) VALUES (3,  'Jiřina', 'Zemanová', null);
INSERT INTO "Author"(author_id, first_name, last_name, nickname) VALUES (4,  'Krystyna', 'Babij', null);
INSERT INTO "Category"(category_id, name, description) VALUES (0,  'kryminał', 'Pięćdziesiąt.');
INSERT INTO "Category"(category_id, name, description) VALUES (1,  'komedia', 'Źródło rysunek.');
INSERT INTO "Category"(category_id, name, description) VALUES (2,  'biografia', 'Utwór trzeba.');
INSERT INTO "Category"(category_id, name, description) VALUES (3,  'fantastyka', 'Wywołać podział.');
INSERT INTO "Category"(category_id, name, description) VALUES (4,  'popularno-naukowe', 'Przedstawiciel.');
INSERT INTO "Publisher"(publisher_id, name) VALUES (0, 'Reynolds and Sons');
INSERT INTO "Publisher"(publisher_id, name) VALUES (1, 'Noel Roger S.A.S.');
INSERT INTO "Publisher"(publisher_id, name) VALUES (2, 'Grund-Bogaczyk Sp. z o.o. Sp.k.');
INSERT INTO "Publisher"(publisher_id, name) VALUES (3, 'Meyer SA');
INSERT INTO "Publisher"(publisher_id, name) VALUES (4, 'Dufour');
INSERT INTO "Publisher"(publisher_id, name) VALUES (5, 'Underwood-Young');
INSERT INTO "Publisher"(publisher_id, name) VALUES (6, 'Fras-Kozdrój Sp. z o.o.');
INSERT INTO "Publisher"(publisher_id, name) VALUES (7, 'Grupa Nalewajek');
INSERT INTO "Publisher"(publisher_id, name) VALUES (8, 'Spółdzielnia Tytko Sp. z o.o.');
INSERT INTO "Publisher"(publisher_id, name) VALUES (9, 'Dupre Boucher S.A.S.');
INSERT INTO "Publisher"(publisher_id, name) VALUES (10, 'Salas-Allen');
INSERT INTO "Publisher"(publisher_id, name) VALUES (11, 'Carter Inc');
INSERT INTO "Publisher"(publisher_id, name) VALUES (12, 'Davis-Kline');
INSERT INTO "Publisher"(publisher_id, name) VALUES (13, 'Kříž a.s.');
INSERT INTO "Publisher"(publisher_id, name) VALUES (14, 'Pacocha i syn s.c.');
INSERT INTO "Publisher"(publisher_id, name) VALUES (15, 'Kratochvíl');
INSERT INTO "Publisher"(publisher_id, name) VALUES (16, 'Payet');
INSERT INTO "Publisher"(publisher_id, name) VALUES (17, 'Meyer, Meadows and Thomas');
INSERT INTO "Publisher"(publisher_id, name) VALUES (18, 'Colin');
INSERT INTO "Publisher"(publisher_id, name) VALUES (19, 'Dušková o.s.');
INSERT INTO "Book"(book_id, title, category_id) VALUES (0, 'Body teacher play', 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (0, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (1, 'Evening manager deal fish decide', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (1, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (2, 'Mention experience guess name issue', 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (2, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (3, 'Arm available term upon', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (3, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (4, 'Future free painting war alone', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (4, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (5, 'What personal risk power', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (5, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (6, 'The focus computer thousand', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (6, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (7, 'Eye down necessary voice', 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (7, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (8, 'News phone certain', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (8, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (9, 'Apply travel second', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (9, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (10, 'College her region him', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (10, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (11, 'Low region from', 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (11, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (12, 'Four brother option poor east', 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (12, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (13, 'Health claim', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (13, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (14, 'Pay defense wall', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (14, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (15, 'Able nothing leg culture', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (15, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (16, 'Great which bad this third', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (16, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (17, 'Difficult environmental', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (17, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (18, 'Entire none worker', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (18, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (19, 'Option possible common', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (19, 1);
INSERT INTO "Book"(book_id, title, category_id) VALUES (20, 'Quia repudiandae doloribus vel natus', 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (20, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (21, 'Est laborum', 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (21, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (22, 'Fuga magnam eaque odio', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (22, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (23, 'Quia soluta aliquam', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (23, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (24, 'Similique ex voluptates', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (24, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (25, 'Labore aut similique nostrum', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (25, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (26, 'Consectetur accusamus quidem', 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (26, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (27, 'Nihil accusamus fuga', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (27, 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (27, 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (27, 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (27, 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (27, 0);
INSERT INTO "Book"(book_id, title, category_id) VALUES (28, 'Adipisci facilis incidunt minus', 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (28, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (29, 'Quisquam corrupti', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (29, 2);
INSERT INTO "Book"(book_id, title, category_id) VALUES (30, 'Dicta unde perspiciatis', 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (30, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (31, 'Harum architecto doloremque similique', 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (31, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (32, 'Voluptatem provident quis vero error', 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (32, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (33, 'Animi vero', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (33, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (34, 'Numquam recusandae hic', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (34, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (35, 'Dolorum ipsum eligendi accusamus', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (35, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (36, 'Reprehenderit ea deleniti unde aliquid', 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (36, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (37, 'Necessitatibus accusamus voluptatibus', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (37, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (38, 'Iure soluta modi quisquam', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (38, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (39, 'Molestias provident modi rerum', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (39, 3);
INSERT INTO "Book"(book_id, title, category_id) VALUES (40, 'Niedźwiedź prawdziwy oddać powstanie', 3);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (40, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (41, 'Parlament droga odpowiedni nikt zmęczony', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (41, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (42, 'Przejść według naukowy płynąć', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (42, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (43, 'Wiele przyjmować gospodarstwo minerał', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (43, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (44, 'Fragment wzbudzać zwierzę cień', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (44, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (45, 'Mieć Na Imię dziesięć planeta', 1);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (45, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (46, 'Dziś lis', 4);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (46, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (47, 'Kula mąka kapelusz pszczoła', 0);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (47, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (48, 'Rosja przez nazywać się ogromny', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (48, 4);
INSERT INTO "Book"(book_id, title, category_id) VALUES (49, 'Obecny Chrystus odnosić się Azja', 2);
INSERT INTO "BookAuthor"(book_id, author_id) VALUES (49, 4);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780417060910, 4, 352, '2010-02-05', 0, 6);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781174592218, 6, 871, '2018-06-30', 1, 18);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781241864545, 4, 922, '1972-06-18', 2, 12);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780580278402, 5, 374, '2010-10-22', 3, 19);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780455669137, 5, 429, '1973-09-25', 4, 11);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781823995476, 3, 135, '1974-03-06', 5, 3);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780066928166, 6, 551, '1974-02-08', 6, 18);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780072130263, 6, 225, '1999-02-11', 7, 18);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781168372543, 6, 912, '2000-06-22', 8, 6);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781860191848, 6, 559, '2018-08-19', 9, 19);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781943604951, 1, 858, '2006-02-09', 10, 9);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781565537484, 1, 856, '1977-12-21', 11, 2);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780096610482, 4, 356, '2010-09-19', 12, 18);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781120835253, 4, 311, '2017-05-14', 13, 8);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781864510621, 2, 797, '2004-03-23', 14, 9);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780044080374, 6, 315, '2005-11-17', 15, 9);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780664705015, 2, 160, '1991-11-06', 16, 10);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781128477790, 6, 674, '1989-09-13', 17, 6);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781799734543, 4, 727, '1989-02-27', 18, 11);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781418566104, 1, 772, '1992-06-09', 19, 7);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780498556005, 5, 702, '1996-07-11', 20, 18);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781435973695, 1, 773, '1984-10-12', 21, 3);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780831730451, 5, 812, '2018-07-06', 22, 1);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781693822124, 2, 899, '1991-02-17', 23, 7);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781089522515, 3, 334, '1986-05-05', 24, 1);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780792367253, 6, 720, '2014-03-26', 25, 17);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781260759785, 2, 520, '2002-02-02', 26, 14);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780986031779, 5, 574, '1985-11-15', 27, 12);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780599575158, 6, 440, '2001-05-17', 28, 6);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780622419718, 5, 522, '1975-09-16', 29, 7);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780584304688, 5, 449, '1970-01-07', 30, 3);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780798716864, 4, 490, '1992-04-19', 31, 2);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780015732844, 2, 835, '1971-06-21', 32, 19);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780061242755, 1, 379, '2010-01-06', 33, 17);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780019032827, 6, 604, '1993-02-07', 34, 5);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781098067533, 1, 747, '2005-11-03', 35, 0);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781115627559, 4, 351, '1985-02-26', 36, 4);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780634087608, 5, 437, '1973-08-22', 37, 1);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781342926036, 2, 690, '1982-06-23', 38, 16);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781225133865, 1, 604, '2016-04-16', 39, 0);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781977585608, 1, 825, '1992-07-31', 40, 1);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780087790506, 3, 907, '2006-06-07', 41, 5);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781377977485, 1, 502, '2001-02-27', 42, 1);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781074713379, 5, 409, '1974-02-07', 43, 18);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781289888596, 5, 169, '1995-02-21', 44, 17);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780644634786, 6, 527, '1988-02-22', 45, 15);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780772462121, 1, 728, '1977-07-06', 46, 14);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9781067599010, 3, 406, '1990-12-31', 47, 9);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780904550061, 3, 794, '2013-01-26', 48, 17);
INSERT INTO "Edition"(isbn, number, page_count, date, book_id, publisher_id) VALUES(9780999034224, 3, 255, '2005-05-05', 49, 2);
INSERT INTO "Card"(card_id, number, token) VALUES (0, '************0187', '63bd9d86d8467c2df4b856aa0b208043');
INSERT INTO "Card"(card_id, number, token) VALUES (1, '************9545', '4b14897738c56bc238f529266af3bcd6');
INSERT INTO "Card"(card_id, number, token) VALUES (2, '************9702', 'e93cf9212b6ba6258157357a8d081685');
INSERT INTO "Card"(card_id, number, token) VALUES (3, '************3593', '1afd17c8ac94037a270aad85672e0c9');
INSERT INTO "Card"(card_id, number, token) VALUES (4, '************0060', 'ba05f6a2f368aea167a80d47d6b9db08');
INSERT INTO "User"(user_id, name, email, hash, borrowings_remaining, subscription_id, card_id) VALUES(0, 'hic', 'pawelsommerfeld@mol.pl', 'c096685688cfe2a4d59b83b1c4c540c3f12758da704c5dbcbd7d7e51ce51c73a', 1, 0, 0);
INSERT INTO "User"(user_id, name, email, hash, borrowings_remaining, subscription_id, card_id) VALUES(1, 'rencontre', 'cezary60@o2.pl', '583763a274932280ff04041ca4a5d61d38948b368c57609c94dbc3a7d5c5c0c3', 0, 0, 1);
INSERT INTO "User"(user_id, name, email, hash, borrowings_remaining, subscription_id, card_id) VALUES(2, 'przeciwnik', 'jasinakonstanty@gmail.com', 'a8c7697a161fa56f9a30a4dec1eeaba6b3a3a3337a3804ead2943049df9d9466', 21, 3, 2);
INSERT INTO "User"(user_id, name, email, hash, borrowings_remaining, subscription_id, card_id) VALUES(3, 'nisi', 'vaillantaime@roussel.fr', '7146aaf16084e8b0d9830fa891395153e10531bd9e1c6ec9f87002c667fd9866', 1, 0, 3);
INSERT INTO "User"(user_id, name, email, hash, borrowings_remaining, subscription_id, card_id) VALUES(4, 'sed', 'bianka52@ppuh.com', 'b53c5c87d0222c476996a698a40ccd61cc765dd0436d827dd6dcf9d10eb87c6e', 0, 0, 4);
INSERT INTO "Payments"(payments_id, amount, date, user_id) VALUES(0, 0, '2020-12-01', 0);
INSERT INTO "Payments"(payments_id, amount, date, user_id) VALUES(1, 0, '2020-12-01', 1);
INSERT INTO "Payments"(payments_id, amount, date, user_id) VALUES(2, 30, '2020-12-01', 2);
INSERT INTO "Payments"(payments_id, amount, date, user_id) VALUES(3, 0, '2020-12-01', 3);
INSERT INTO "Payments"(payments_id, amount, date, user_id) VALUES(4, 0, '2020-12-01', 4);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (0, '2020-12-01', '2020-12-01', 9780772462121, 1);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (1, '2020-12-01', '2020-12-01', 9780072130263, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (2, '2020-12-01', '2020-12-01', 9781225133865, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (3, '2020-12-01', '2020-12-01', 9780019032827, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (4, '2020-12-01', '2020-12-01', 9780792367253, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (5, '2020-12-01', '2020-12-01', 9780798716864, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (6, '2020-12-01', '2020-12-01', 9781435973695, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (7, '2020-12-01', '2020-12-01', 9780498556005, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (8, '2020-12-01', '2020-12-01', 9781120835253, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (9, '2020-12-01', '2020-12-01', 9780498556005, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (10, '2020-12-01', '2020-12-01', 9780986031779, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (11, '2020-12-01', '2020-12-01', 9781241864545, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (12, '2020-12-01', '2020-12-01', 9781067599010, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (13, '2020-12-01', '2020-12-01', 9781168372543, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (14, '2020-12-01', '2020-12-01', 9780792367253, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (15, '2020-12-01', '2020-12-01', 9781799734543, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (16, '2020-12-01', '2020-12-01', 9780622419718, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (17, '2020-12-01', '2020-12-01', 9780019032827, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (18, '2020-12-01', '2020-12-01', 9781168372543, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (19, '2020-12-01', '2020-12-01', 9780664705015, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (20, '2020-12-01', '2020-12-01', 9780044080374, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (21, '2020-12-01', '2020-12-01', 9781115627559, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (22, '2020-12-01', '2020-12-01', 9781693822124, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (23, '2020-12-01', '2020-12-01', 9781799734543, 2);
INSERT INTO "Borrowing"(borrowing_id, start_date, end_date, isbn, user_id) VALUES (24, '2020-12-01', '2020-12-01', 9780087790506, 4);