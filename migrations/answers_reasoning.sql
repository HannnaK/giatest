DROP TABLE IF EXISTS "answers_reasoning";
CREATE TABLE "answers_reasoning"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "id_user"     INTEGER NOT NULL,
    "id_reasoning"    INTEGER NOT NULL,
    "is_answer_correct" BOOLEAN CHECK ("is_answer_correct" IN (0, 1))
);

