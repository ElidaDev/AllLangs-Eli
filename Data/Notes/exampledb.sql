-- Select the database to use
USE exampledb;
-- Create the Contacts table only if it doesn't exist
-- id is INT but NOT auto-incrementing
CREATE TABLE IF NOT EXISTS Contacts (
    id INT,
    LastName VARCHAR(200),
    FirstName VARCHAR(200)
    -- Consider adding PRIMARY KEY(id) if ID should be strictly unique
);
-- 1. Add 2 famous CS people, providing manual IDs
INSERT INTO Contacts (id, LastName, FirstName) VALUES
(1, 'Lovelace', 'Ada'),     -- Ada Lovelace
(2, 'Turing', 'Alan');      -- Alan Turing
-- 2. Show the current people
-- Expected: (1, 'Lovelace', 'Ada'), (2, 'Turing', 'Alan')
SELECT '-- Initial Inserts --' AS Step; -- Adding separator for clarity
SELECT * FROM Contacts;
-- 3. Delete one person
-- Deleting Alan Turing (id=2)
DELETE FROM Contacts
WHERE id = 2;
-- Using ID is safer than WHERE LastName = 'Turing' AND FirstName = 'Alan';
-- 4. Add 2 more famous CS people, providing new manual IDs
INSERT INTO Contacts (id, LastName, FirstName) VALUES
(3, 'Hopper', 'Grace'),     -- Grace Hopper
(4, 'Knuth', 'Donald');     -- Donald Knuth
-- 5. Show all remaining people after delete and adds
-- Expected: (1, 'Lovelace', 'Ada'), (3, 'Hopper', 'Grace'), (4, 'Knuth', 'Donald')
SELECT '-- After Delete & Second Inserts --' AS Step;
SELECT * FROM Contacts;
-- 6. Update one of the names
-- Let's update Ada Lovelace (id=1) to use 'King' (She became Countess of Lovelace via marriage to William King)
UPDATE Contacts
SET LastName = 'King'
WHERE id = 1;
-- Using ID is safer than WHERE LastName = 'Lovelace' AND FirstName = 'Ada';
-- 7. Show the information again after the update
-- Expected: (1, 'King', 'Ada'), (3, 'Hopper', 'Grace'), (4, 'Knuth', 'Donald')
SELECT * FROM Contacts;

ALTER TABLE Contacts ADD GamerTag VARCHAR(255);
UPDATE Contacts SET GamerTag = "Grrrraeaat1952" WHERE LastName = "Tiger";