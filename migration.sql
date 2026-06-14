PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS fato_resultado;
DROP TABLE IF EXISTS fato_standings;
DROP TABLE IF EXISTS dim_temporada;
DROP TABLE IF EXISTS dim_circuito;
DROP TABLE IF EXISTS dim_piloto;
DROP TABLE IF EXISTS dim_equipe;
DROP TABLE IF EXISTS dim_era;

CREATE TABLE IF NOT EXISTS dim_era (
    eraId INTEGER PRIMARY KEY,
    eraName TEXT NOT NULL,
    motorType TEXT,
    startYear INTEGER NOT NULL,
    endYear INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_circuito (
    circuitId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT,
    country TEXT,
    lat REAL,
    lng REAL
);

CREATE TABLE IF NOT EXISTS dim_piloto (
    driverId INTEGER PRIMARY KEY,
    number INTEGER,
    code TEXT,
    forename TEXT NOT NULL,
    surname TEXT NOT NULL,
    dob TEXT,
    nationality TEXT
);

CREATE TABLE IF NOT EXISTS dim_equipe (
    constructorId INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    nationality TEXT
);

CREATE TABLE IF NOT EXISTS dim_temporada (
    raceId INTEGER PRIMARY KEY,
    year INTEGER NOT NULL,
    round INTEGER,
    circuitId INTEGER REFERENCES dim_circuito(circuitId),
    name TEXT,
    date TEXT,
    time TEXT,
    eraId INTEGER REFERENCES dim_era(eraId)
);

CREATE TABLE IF NOT EXISTS fato_resultado (
    resultId INTEGER PRIMARY KEY,
    raceId INTEGER REFERENCES dim_temporada(raceId),
    driverId INTEGER REFERENCES dim_piloto(driverId),
    constructorId INTEGER REFERENCES dim_equipe(constructorId),
    number INTEGER,
    grid INTEGER,
    position INTEGER,
    positionText TEXT,
    points REAL,
    laps INTEGER,
    time TEXT,
    milliseconds INTEGER,
    fastestLap INTEGER,
    rank INTEGER,
    fastestLapTime TEXT,
    fastestLapSpeed REAL,
    statusId INTEGER
);

CREATE TABLE IF NOT EXISTS fato_standings (
    driverStandingsId INTEGER PRIMARY KEY,
    raceId INTEGER REFERENCES dim_temporada(raceId),
    driverId INTEGER REFERENCES dim_piloto(driverId),
    points REAL,
    position INTEGER,
    wins INTEGER
);