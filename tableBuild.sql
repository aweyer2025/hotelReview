CREATE TABLE Hotel (
    hotelID INT PRIMARY KEY,  
    Name VARCHAR(30) NOT NULL,
    City VARCHAR(30) NOT NULL,
);

CREATE TABLE Feature (
    FeatureID INT PRIMARY KEY,
    Title VARCHAR(20)
);

CREATE TABLE Seed(
    SeedID INT PRIMARY KEY,
    wordOrPhrase VARCHAR(40)
    Polarity INT
    FeatureID FOREIGN KEY
);

CREATE TABLE Rating (
    RatingID INT PRIMARY KEY,
    Rating VARCHAR(20),
    FeatureID FOREIGN KEY,
    hotelID FOREIGN KEY
)

CREATE Review(
    ReviewID INT PRIMARY KEY,
    Title VARCHAR(300),
    Review CLOB,
    Date VARCHAR(15)
    hotelID FOREIGN KEY
)

commit;
