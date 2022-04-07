DROP TABLE IF EXISTS "reasoning";

CREATE TABLE "reasoning"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "statement"     TEXT CHARACTER utf8 NOT NULL,
    "query"    TEXT CHARACTER utf8 NOT NULL,
    "answer1" TEXT CHARACTER utf8 NOT NULL,
    "answer2"      TEXT CHARACTER utf8 NOT NULL,
    "correct_answer" TEXT CHARACTER utf8 NOT NULL
);
INSERT INTO "reasoning"
VALUES (NULL, 'Darek jest nie taki ci�ki jak Bogdan.', 'Kto jest ci�szy?', 'Bogdan', 'Darek', 'Bogdan'),
(NULL, 'Bartek jest wy�szy ni� Antek.', 'Kto jest ni�szy?', 'Antek', 'Bartek', 'Antek'),
(NULL, 'Filip jest nie tak smutny jak Bogdan.', 'Kto jest weselszy?', 'Filip', 'Bogdan', 'Filip'),
(NULL, 'Tomek jest l�ejszy ni� Jan.', 'Kto jest ci�szy?', 'Jan', 'Tomek', 'Jan'),
(NULL, 'Witek jest g�upszy ni� Bolek.', 'Kto jest g�upszy?', 'Witek', 'Bolek', 'Witek'),
(NULL, 'Rafa� jest nie tak ci�ki jak Roman.', 'Kto jest l�ejszy?', 'Roman', 'Rafa�', 'Rafa�'),
(NULL, 'Bogdan jest nie tak szybki jak Krzy�.', 'Kto jest wolniejszy?', 'Krzy�', 'Bogdan', 'Bogdan'),
(NULL, 'Jacek jest l�ejszy ni� Marcin.', 'Kto jest ci�szy?', 'Jacek', 'Marcin', 'Marcin'),
(NULL, 'Janusz jest m�drzejszy ni� Eryk.', 'Kto jest m�drzejszy.', 'Eryk', 'Janusz', 'Janusz'),
(NULL, 'Tomek jest weselszy ni� Marek.',  'Kto jest weselszy?', 'Marek', 'Tomek', 'Tomek'),
(NULL, 'Marcin jest wy�szy ni� Jan.', 'Kto jest ni�szy?', 'Marcin', 'Jan', 'Jan'),
(NULL, 'Julian jest l�ejszy ni� Bartek.', 'Kto jest ci�szy?', 'Bartek', 'Bartek', 'Julian'),
(NULL, 'Bogdan jest nie tak weso�y jak Janusz.', 'Kto jest weselszy?', 'Janusz', 'Janusz', 'Bogdan'),
(NULL, 'Marcin jest m�drzejszy ni� Pawe�.', 'Kto jest g�upszy?', 'Pawe�', 'Marcin', 'Pawe�');

