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
VALUES (NULL, "M", "B", "T", "D", "f", "j", "g", "p", 0),
(NULL, "Y", "W", "Z", "H", "t", "w", "j", "h", 2),
(NULL, "n", "m", "f", "y", "N", "M", "B", "Y", 3),
(NULL, "k", "p", "r", "w", "K", "P", "R", "W", 4),
(NULL, "N", "M", "J", "B", "m", "n", "g", "b", 3),
(NULL, "t", "p", "f", "y", "T", "Z", "M", "K", 1),
(NULL, "N", "B", "G", "W", "j", "b", "g", "y", 2),
(NULL, "f", "n", "m", "k", "H", "W", "J", "B", 0),
(NULL, "g", "d", "r", "t", "M", "D", "Z", "N", 1),
(NULL, "Y", "B", "G", "R", "w", "j", "f", "z", 0),
(NULL, "K", "H", "M", "N", "k", "d", "m", "n", 3),
(NULL, "Y", "J", "H", "B", "f", "w", "d", "p", 0),
(NULL, "z", "g", "r", "m", "Z", "G", "R", "M", 4),
(NULL, "D", "J", "H", "N", "b", "j", "h", "n", 3);

