CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    Title VARCHAR(255),
    ReleaseYear INT,
	DirectorID INT,
    Rating DECIMAL(3, 2),
    Description TEXT,
	FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID)
); 

CREATE TABLE Genres (
    GenreID INT PRIMARY KEY,
    GenreName VARCHAR(255)
);

CREATE TABLE Directors (
    DirectorID INT PRIMARY KEY,
    DirectorName VARCHAR(255),
    BirthDate DATE
);

CREATE TABLE Actors (
    ActorID INT PRIMARY KEY,
    ActorName VARCHAR(255),
    BirthDate DATE
);

CREATE TABLE MovieGenres (
    MovieID INT,
    GenreID INT,
    PRIMARY KEY (MovieID, GenreID),
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);

CREATE TABLE MovieActors (
    MovieID INT,
    ActorID INT,
    PRIMARY KEY (MovieID, ActorID),
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (ActorID) REFERENCES Actors(ActorID)
);

CREATE TABLE MovieDirectors (
    MovieID INT,
    DirectorID INT,
    PRIMARY KEY (MovieID, DirectorID),
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID)
);

-- Populate Genres
INSERT INTO Genres (GenreID, GenreName) VALUES
(1, 'Action'),
(2, 'Drama'),
(3, 'Comedy'),
(4, 'Sci-Fi'),
(5, 'Adventure');

-- Populate Directors
INSERT INTO Directors (DirectorID, DirectorName, BirthDate) VALUES
(1, 'Christopher Nolan', '1970-07-30'),
(2, 'Quentin Tarantino', '1963-03-27'),
(3, 'Denis Villeneuve', '1967-10-03'),
(4, 'David Fincher', '1962-08-28'),
(5, 'Greta Gerwig', '1983-08-04'),
(6, 'James Cameron', '1954-08-16'),
(7, 'Patty Jenkins', '1971-07-24');

-- Populate Actors
INSERT INTO Actors (ActorID, ActorName, BirthDate) VALUES
(1, 'Leonardo DiCaprio', '1974-11-11'),
(2, 'Brad Pitt', '1963-12-18'),
(3, 'Margot Robbie', '1990-07-02'),
(4, 'Robert Downey Jr.', '1965-04-04'),
(5, 'Chris Evans', '1981-06-13'),
(6, 'Scarlett Johansson', '1984-11-22'),
(7, 'Tom Hardy', '1977-09-15'),
(8, 'Anne Hathaway', '1982-11-12'),
(9, 'Matthew McConaughey', '1969-11-04'),
(10, 'Ryan Gosling', '1980-11-12'),
(11, 'Emma Stone', '1988-11-06'),
(12, 'Gal Gadot', '1985-04-30'),
(13, 'Hugh Jackman', '1968-10-12'),
(14, 'Christian Bale', '1974-01-30'),
(15, 'Amy Adams', '1974-08-20');

-- Populate Movies
INSERT INTO Movies (MovieID, Title, ReleaseYear, DirectorID, Rating, Description) VALUES
(1, 'Inception', 2010, 1, 8.8, 'A mind-bending thriller about dream manipulation.'),
(2, 'Django Unchained', 2012, 2, 8.4, 'A freed slave sets out to rescue his wife.'),
(3, 'Interstellar', 2014, 1, 8.6, 'Explorers travel through a wormhole in space.'),
(4, 'La La Land', 2016, 5, 8.0, 'A musician and actress chase their dreams.'),
(5, 'Arrival', 2016, 3, 7.9, 'A linguist communicates with aliens.'),
(6, 'Wonder Woman', 2017, 7, 7.4, 'An Amazonian warrior fights in World War I.'),
(7, 'Blade Runner 2049', 2017, 3, 8.0, 'A new Blade Runner unearths a long-buried secret.'),
(8, 'Once Upon a Time in Hollywood', 2019, 2, 7.6, 'An actor and his stunt double in 1960s LA.'),
(9, 'Tenet', 2020, 1, 7.4, 'An agent manipulates time to prevent WWIII.'),
(10, 'Dune', 2021, 3, 8.1, 'A noble family is embroiled in a galactic conflict.');

-- Insert a test movie with no actors or genres
INSERT INTO Movies (MovieID, Title, ReleaseYear, DirectorID, Rating, Description) 
VALUES (11, 'Test Movie', 2023, 1, 7.0, 'A movie with no actors or genres.');

-- Populate MovieGenres
INSERT INTO MovieGenres (MovieID, GenreID) VALUES
(1, 1), (1, 4),
(2, 1), (2, 2),
(3, 5), (3, 4),
(4, 3), (4, 2),
(5, 4),
(6, 1), (6, 5),
(7, 4), (7, 5),
(8, 2),
(9, 1), (9, 4),
(10, 5);

-- Populate MovieActors
INSERT INTO MovieActors (MovieID, ActorID) VALUES
(1, 1), (1, 7), (1, 8),
(2, 1), (2, 2), (2, 3),
(3, 1), (3, 9), (3, 8),
(4, 10), (4, 11),
(5, 15), (5, 12),
(6, 12), (6, 6),
(7, 7), (7, 13),
(8, 2), (8, 3), (8, 10),
(9, 14), (9, 6),
(10, 14), (10, 15), (10, 7);

-- Populate MovieDirectors
INSERT INTO MovieDirectors (MovieID, DirectorID) VALUES
(1, 1),
(2, 2),
(3, 1),
(4, 5),
(5, 3),
(6, 7),
(7, 3),
(8, 2),
(9, 1),
(10, 3);


Select * from Movies;
Select * from Genres;
Select *  from Directors;
Select * from Actors; 
Select * from MovieGenres;
Select * from MovieActors;



-- PROJECT2 

-- Search Movies by Year
SELECT COUNT(*) AS MovieCount FROM Movies WHERE ReleaseYear = 2020;

-- Search Movies by Year Range
SELECT COUNT(*) AS MovieCount FROM Movies WHERE ReleaseYear BETWEEN 2000 AND 2010;

-- Add Index to Optimize Performance
CREATE INDEX idx_movies_year ON Movies (ReleaseYear);
CREATE INDEX idx_movies_year_range ON Movies (ReleaseYear);


---checking
SELECT name 
FROM sqlite_master 
WHERE type = 'index' 
AND tbl_name = 'Movies';
