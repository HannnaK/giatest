DROP TABLE IF EXISTS "reasoning";

CREATE TABLE "reasoning"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "statement"     TEXT CHARACTER utf8 NOT NULL,
    "query"    TEXT CHARACTER utf8 NOT NULL,
    "answer1" TEXT CHARACTER utf8 NOT NULL,
    "answer2"      TEXT CHARACTER utf8 NOT NULL,
    "correct_answer" INTEGER NOT NULL
);
INSERT INTO "reasoning"
VALUES (NULL, 'Darek jest nie taki ci�ki jak Bogdan', 'Kro jest ci�szy?', 'Bogdan', 'Darek', 'Bogdan');
INSERT INTO "reasoning"
VALUES (NULL, 'Bartek jest wy�szy ni� Antek.', 'Kto jest ni�szy?', 'Antek', 'Bartek', 'Antek');
INSERT INTO "reasoning"
VALUES (NULL, 'Filip jest nie tak smutny jak Bogdan.', 'Kto jest weselszy?', 'Filip', 'Bogdan', 'Filip');
INSERT INTO "reasoning"
VALUES (NULL, 'Tomek jest l�ejszy ni� Jan.', 'Kto jest ci�szy?', 'Jan', 'Tomek', 'Jan');
INSERT INTO "reasoning"
VALUES (NULL, 'Witek jest g�upszy ni� Bolek.', 'Kto jest g�upszy?', 'Witek', 'Bolek', 'Witek');
