DROP TABLE IF EXISTS "compare_items";

CREATE TABLE "compare_items"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "letter1"     TEXT CHARACTER utf8 NOT NULL,
    "letter2"    TEXT CHARACTER utf8 NOT NULL,
    "letter3" TEXT CHARACTER utf8 NOT NULL,
    "letter4"      TEXT CHARACTER utf8 NOT NULL,
    "letter5"     TEXT CHARACTER utf8 NOT NULL,
    "letter6"    TEXT CHARACTER utf8 NOT NULL,
    "letter7" TEXT CHARACTER utf8 NOT NULL,
    "letter8"      TEXT CHARACTER utf8 NOT NULL,
    "correct_answer" INTEGER NOT NULL
);
INSERT INTO "compare_items"
VALUES (NULL, "M", "B", "T", "D", "f", "j", "g", "p", 0);
INSERT INTO "compare_items"
VALUES (NULL, "Y", "W", "Z", "H", "t", "w", "j", "h", 2);
INSERT INTO "compare_items"
VALUES (NULL, "n", "m", "f", "y", "N", "M", "B", "Y", 3);
INSERT INTO "compare_items"
VALUES (NULL, "k", "p", "r", "w", "K", "P", "R", "W", 4);
INSERT INTO "compare_items"
VALUES (NULL, "N", "M", "J", "B", "m", "n", "g", "b", 3);
INSERT INTO "compare_items"
VALUES (NULL, "t", "p", "f", "y", "T", "Z", "M", "K", 1);
INSERT INTO "compare_items"
VALUES (NULL, "N", "B", "G", "W", "j", "b", "g", "y", 2);
INSERT INTO "compare_items"
VALUES (NULL, "f", "n", "m", "k", "H", "W", "J", "B", 0);
INSERT INTO "compare_items"
VALUES (NULL, "g", "d", "r", "t", "M", "D", "Z", "N", 1);
INSERT INTO "compare_items"
VALUES (NULL, "Y", "B", "G", "R", "w", "j", "f", "z", 0);
