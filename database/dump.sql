BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim','Kim@naver.com','010-0000-0000','Kim.com','2021-06-17 12:43:40');
INSERT INTO "users" VALUES(2,'Park','Park@naver.com','010-1111-1111','Park.com','2021-06-17 12:43:40');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-2222-2222','Lee.com','2021-06-17 12:43:40');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-3333-3333','Cho.com','2021-06-17 12:43:40');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-4444-4444','Yoo.com','2021-06-17 12:43:40');
COMMIT;
