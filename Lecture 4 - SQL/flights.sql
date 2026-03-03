-- Create the flights table
CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    duration INTEGER NOT NULL
);

-- Insert sample flight data
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Shanghai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 455);

-- Query all flights
SELECT * FROM flights;

-- Query flights from New York
SELECT * FROM flights WHERE origin = 'New York';

-- Query flights with duration less than 500
SELECT * FROM flights WHERE duration < 500;

-- Query flights from New York with duration less than 500
SELECT * FROM flights WHERE origin = 'New York' AND duration < 500;

-- Count flights from each origin
SELECT origin, COUNT(*) FROM flights GROUP BY origin;

-- Get average duration per origin
SELECT origin, AVG(duration) FROM flights GROUP BY origin;

-- Update a flight duration
-- UPDATE flights SET duration = 430 WHERE origin = "New York" AND destination = "London";

-- Delete a flight
-- DELETE FROM flights WHERE destination = "Tokyo";

-- ─────────────────────────────────────────────
-- Airports table
-- ─────────────────────────────────────────────
CREATE TABLE airports (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    city    TEXT NOT NULL,
    country TEXT NOT NULL,
    code    TEXT NOT NULL UNIQUE   -- IATA code
);

INSERT INTO airports (city, country, code) VALUES ('New York',  'United States', 'JFK');
INSERT INTO airports (city, country, code) VALUES ('London',    'United Kingdom','LHR');
INSERT INTO airports (city, country, code) VALUES ('Paris',     'France',        'CDG');
INSERT INTO airports (city, country, code) VALUES ('Tokyo',     'Japan',         'NRT');
INSERT INTO airports (city, country, code) VALUES ('Istanbul',  'Turkey',        'IST');
INSERT INTO airports (city, country, code) VALUES ('Shanghai',  'China',         'PVG');

-- ─────────────────────────────────────────────
-- Passengers table
-- ─────────────────────────────────────────────
CREATE TABLE passengers (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL
);

INSERT INTO passengers (first_name, last_name) VALUES ('Alice',   'Nguyen');
INSERT INTO passengers (first_name, last_name) VALUES ('Bob',     'Okafor');
INSERT INTO passengers (first_name, last_name) VALUES ('Carlos',  'Reyes');
INSERT INTO passengers (first_name, last_name) VALUES ('Diana',   'Petrov');
INSERT INTO passengers (first_name, last_name) VALUES ('Ethan',   'Kim');
INSERT INTO passengers (first_name, last_name) VALUES ('Fatima',  'Al-Hassan');

-- ─────────────────────────────────────────────
-- Junction table: one passenger ↔ many flights,
--                 one flight    ↔ many passengers
-- ─────────────────────────────────────────────
CREATE TABLE passenger_flights (
    passenger_id INTEGER NOT NULL REFERENCES passengers(id),
    flight_id    INTEGER NOT NULL REFERENCES flights(id),
    PRIMARY KEY (passenger_id, flight_id)
);

-- Assign passengers to flights (multiple flights per passenger, multiple passengers per flight)
-- Note: flight IDs reference the actual IDs auto-assigned in the flights table
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (1, 1);  -- Alice   → New York→London
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (1, 4);  -- Alice   → New York→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (2, 1);  -- Bob     → New York→London
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (2, 2);  -- Bob     → Shanghai→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (3, 2);  -- Carlos  → Shanghai→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (3, 5);  -- Carlos  → Moscow→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (4, 4);  -- Diana   → New York→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (4, 7);  -- Diana   → Tokyo→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (5, 4);  -- Ethan   → New York→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (5, 5);  -- Ethan   → Moscow→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (6, 7);  -- Fatima  → Tokyo→Paris
INSERT INTO passenger_flights (passenger_id, flight_id) VALUES (6, 8);  -- Fatima  → Cape Town→Cairo

-- ─────────────────────────────────────────────
-- Sample queries
-- ─────────────────────────────────────────────

-- List all passengers with their flights
SELECT p.first_name || ' ' || p.last_name AS passenger,
       f.origin, f.destination, f.duration
FROM passengers p
JOIN passenger_flights pf ON p.id = pf.passenger_id
JOIN flights           f  ON f.id = pf.flight_id
ORDER BY p.last_name;

-- Count how many passengers are on each flight
SELECT f.origin, f.destination, COUNT(pf.passenger_id) AS num_passengers
FROM flights f
JOIN passenger_flights pf ON f.id = pf.flight_id
GROUP BY f.id
ORDER BY num_passengers DESC;
