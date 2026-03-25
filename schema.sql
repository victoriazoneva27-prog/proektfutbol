PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS clubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    city TEXT
);

CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    nationality TEXT,
    position TEXT NOT NULL CHECK(position IN ('GK', 'DF', 'MF', 'FW')),
    number INTEGER NOT NULL CHECK(number BETWEEN 1 AND 99),
    status TEXT DEFAULT 'active',
    club_id INTEGER NULL,
    FOREIGN KEY (club_id) REFERENCES clubs(id)
);

CREATE TABLE IF NOT EXISTS transfers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    from_club_id INTEGER NULL,
    to_club_id INTEGER NOT NULL,
    transfer_date TEXT NOT NULL,
    fee REAL,
    note TEXT,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (from_club_id) REFERENCES clubs(id),
    FOREIGN KEY (to_club_id) REFERENCES clubs(id),
    CHECK (from_club_id IS NULL OR to_club_id != from_club_id)
);

INSERT OR IGNORE INTO clubs (id, name, city) VALUES (1, 'Левски', 'София');
INSERT OR IGNORE INTO clubs (id, name, city) VALUES (2, 'Лудогорец', 'Разград');
INSERT OR IGNORE INTO clubs (id, name, city) VALUES (3, 'Ботев', 'Пловдив');
INSERT OR IGNORE INTO clubs (id, name, city) VALUES (4, 'ЦСКА', 'София');

INSERT OR IGNORE INTO players (id, full_name, birth_date, nationality, position, number, status, club_id)
VALUES
(1, 'Иван Петров', '1999-05-10', 'Bulgarian', 'FW', 9, 'active', 1),
(2, 'Георги Иванов', '1998-03-22', 'Bulgarian', 'MF', 8, 'active', 1),
(3, 'Петър Стоянов', '2000-07-14', 'Bulgarian', 'DF', 5, 'active', 2),
(4, 'Николай Димов', '1997-11-01', 'Bulgarian', 'GK', 1, 'active', 2),
(5, 'Мартин Колев', '2001-02-19', 'Bulgarian', 'FW', 11, 'active', 3),
(6, 'Даниел Тодоров', '1999-09-30', 'Bulgarian', 'MF', 7, 'active', 4);

INSERT OR IGNORE INTO transfers (id, player_id, from_club_id, to_club_id, transfer_date, fee, note)
VALUES
(1, 1, 3, 1, '2025-01-10', 25000, 'Зимен трансфер'),
(2, 2, 4, 1, '2025-07-01', 30000, 'Летен трансфер'),
(3, 3, 1, 2, '2025-08-15', 15000, 'Редовен трансфер'),
(4, 5, NULL, 3, '2025-02-01', 0, 'Първи клуб'),
(5, 6, 2, 4, '2025-06-20', 18000, 'Летен трансфер');