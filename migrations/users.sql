DROP TABLE IF EXISTS "users";
CREATE TABLE "users"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "username" TEXT    NOT NULL,
    "email_address" TEXT    NOT NULL UNIQUE,
    "password" TEXT    NOT NULL
);

INSERT INTO "users"
VALUES (NULL, 'olarobocza', 'olarobocza@wp.pl', 'pbkdf2:sha256:260000$5RX3gz8x0zYYdV0b$40b4e799bbb610afec79c931075c72aa9876861e5648599c61fdcdde641ba822');
INSERT INTO "users"
VALUES (NULL, 'marcin', 'marcin@wp.pl', 'pbkdf2:sha256:260000$oYfOrddkoPhZiGHe$dbb8174fb6fc506fa7f20787090650444a00f225c9c94ad911cb15ae60936f84');
