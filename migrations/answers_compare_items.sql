DROP TABLE IF EXISTS "answers_compare_items";
CREATE TABLE "answers_compare_items"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "id_user"     INTEGER NOT NULL,
    "id_compare_items"    INTEGER NOT NULL,
    "your_answer" INTEGER NOT NULL
);
