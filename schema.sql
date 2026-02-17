PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS clubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    city TEXT
);

CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER NOT NULL,
    full_name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    nationality TEXT,
    position TEXT NOT NULL,
    number INTEGER NOT NULL,
    status TEXT DEFAULT 'active',
    FOREIGN KEY (club_id) REFERENCES clubs(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS transfers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_id INTEGER NOT NULL,
    from_club_id INTEGER,
    to_club_id INTEGER NOT NULL,
    transfer_date TEXT,
    fee REAL,
    FOREIGN KEY (player_id) REFERENCES players(id),
    FOREIGN KEY (from_club_id) REFERENCES clubs(id),
    FOREIGN KEY (to_club_id) REFERENCES clubs(id)
);

CREATE TABLE IF NOT EXISTS leagues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    season TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS league_teams (
    league_id INTEGER,
    club_id INTEGER,
    PRIMARY KEY (league_id, club_id),
    FOREIGN KEY (league_id) REFERENCES leagues(id),
    FOREIGN KEY (club_id) REFERENCES clubs(id)
);

CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    league_id INTEGER,
    home_club_id INTEGER,
    away_club_id INTEGER,
    home_goals INTEGER DEFAULT 0,
    away_goals INTEGER DEFAULT 0,
    match_date TEXT,
    played INTEGER DEFAULT 0,
    FOREIGN KEY (league_id) REFERENCES leagues(id),
    FOREIGN KEY (home_club_id) REFERENCES clubs(id),
    FOREIGN KEY (away_club_id) REFERENCES clubs(id)
);

CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    player_id INTEGER,
    minute INTEGER CHECK(minute BETWEEN 1 AND 120),
    FOREIGN KEY (match_id) REFERENCES matches(id),
    FOREIGN KEY (player_id) REFERENCES players(id)
);

CREATE TABLE IF NOT EXISTS cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    player_id INTEGER,
    card_type TEXT CHECK(card_type IN ('yellow','red')),
    minute INTEGER CHECK(minute BETWEEN 1 AND 120),
    FOREIGN KEY (match_id) REFERENCES matches(id),
    FOREIGN KEY (player_id) REFERENCES players(id)
);

INSERT OR IGNORE INTO clubs (name, city) VALUES ('Левски', 'София');
INSERT OR IGNORE INTO clubs (name, city) VALUES ('Ботев', 'Пловдив');
INSERT OR IGNORE INTO clubs (name, city) VALUES ('Лудогорец', 'Разград');

INSERT INTO players (club_id, full_name, birth_date, nationality, position, number, status)
VALUES (1, 'Иван Петров', '1998-05-12', 'Българин', 'MF', 8, 'active');