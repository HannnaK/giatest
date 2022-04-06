DROP TABLE IF EXISTS "answers_reasoning";
CREATE TABLE "answers_reasoning"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "id_user"     INTEGER NOT NULL,
    "tests_number"  INTEGER NOT NULL,
    "id_reasoning"    INTEGER NOT NULL,
    "my_answer" INTEGER NOT NULL
);

