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
(NULL, "N", "M", "J", "B", "m", "n", "g", "b", 1),
(NULL, "t", "p", "f", "y", "T", "Z", "M", "K", 1),
(NULL, "N", "B", "G", "W", "j", "b", "g", "y", 2),
(NULL, "f", "n", "m", "k", "H", "W", "J", "B", 0),
(NULL, "g", "d", "r", "t", "M", "D", "Z", "N", 1),
(NULL, "Y", "B", "G", "R", "w", "j", "f", "z", 0),
(NULL, "K", "H", "M", "N", "k", "d", "m", "n", 3),
(NULL, "Y", "J", "H", "B", "f", "w", "d", "p", 0),
(NULL, "z", "g", "r", "m", "Z", "G", "R", "M", 4),
(NULL, "D", "J", "H", "N", "b", "j", "h", "n", 3),
(NULL, "p", "k", "t", "y", "G", "W", "J", "M", 0),
(NULL, "f", "d", "h", "n", "F", "B", "H", "N", 3),
(NULL, "M", "G", "T", "R", "m", "g", "t", "b", 3),
(NULL, "k", "y", "w", "p", "K", "Y", "W", "P", 4),
(NULL, "Z", "K", "R", "M", "z", "j", "n", "h", 1),
(NULL, "d", "b", "k", "t", "D", "B", "K", "T", 4),
(NULL, "Z", "R", "F", "N", "j", "r", "b", "k", 1),
(NULL, "m", "h", "p", "f", "M", "G", "W", "F", 2),
(NULL, "N", "Z", "B", "J", "n", "y", "b", "d", 2),
(NULL, "f", "h", "p", "k", "F", "W", "Z", "K", 2),
(NULL, "Y", "B", "N", "P", "h", "d", "f", "t", 0),
(NULL, "g", "r", "m", "b", "P", "Y", "M", "K", 1),
(NULL, "W", "T", "F", "G", "w", "t", "f", "g", 4),
(NULL, "h", "d", "p", "m", "R", "B", "T", "M", 1),
(NULL, "W", "Z", "Y", "K", "w", "z", "y", "k", 4),
(NULL, "b", "p", "h", "t", "B", "P", "D", "G", 2),
(NULL, "y", "w", "k", "r", "H", "J", "Z", "M", 0),
(NULL, "G", "T", "N", "P", "g", "t", "n", "p", 4),
(NULL, "r", "f", "k", "d", "Y", "B", "K", "M", 1),
(NULL, "W", "Z", "F", "H", "g", "z", "d", "h", 2),
(NULL, "m", "k", "r", "j", "B", "P", "R", "J", 2),
(NULL, "W", "N", "Y", "D", "w", "y", "n", "d", 4),
(NULL, "t", "m", "z", "j", "B", "F", "H", "J", 1),
(NULL, "r", "b", "j", "m", "R", "B", "J", "Y", 3),
(NULL, "N", "Z", "H", "D", "w", "k", "p", "j", 0),
(NULL, "m", "y", "d", "t", "B", "N", "F", "P", 0),
(NULL, "K", "W", "Z", "J", "h", "w", "g", "j", 2),
(NULL, "m", "b", "f", "y", "M", "B", "F", "Y", 3),
(NULL, "G", "H", "R", "W", "g", "h", "r", "w", 4),
(NULL, "b", "z", "j", "d", "B", "Z", "J", "D", 3),
(NULL, "W", "N", "P", "K", "w", "t", "f", "r", 1),
(NULL, "d", "y", "h", "j", "P", "Y", "H", "M", 2),
(NULL, "d", "y", "h", "j", "P", "Y", "H", "M", 2),
(NULL, "G", "D", "N", "K", "b", "z", "w", "p", 0),
(NULL, "P", "M", "H", "F", "z", "b", "d", "w", 0),
(NULL, "h", "g", "f", "d", "R", "G", "T", "Y", 1),
(NULL, "n", "r", "g", "h", "N", "R", "G", "H", 3),
(NULL, "B", "M", "W", "T", "y", "z", "j", "p", 0),
(NULL, "d", "g", "h", "m", "D", "G", "H", "M", 4),
(NULL, "z", "n", "r", "p", "F", "N", "R", "P", 3);





































