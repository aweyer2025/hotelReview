SELECT name, open_mode FROM v$pdbs;

'ORCLPDB1'


ALTER PLUGGABLE DATABASE ORCLPDB1 OPEN;

ALTER SESSION SET CONTAINER = ORCLPDB1;

SHOW CON_NAME;


ALTER USER aweyer IDENTIFIED BY new_password;



create user aweyer identified by Passw0rd
default tablespace USERS
TEMPORARY TABLESPACE TEMP
quota UNLIMITED on users;


GRANT CREATE SESSION TO aweyer;  -- Allows user to connect to the database
GRANT CREATE TABLE TO aweyer;    -- Allows user to create tables
GRANT CREATE VIEW TO aweyer;     -- Allows user to create views
GRANT CREATE PROCEDURE TO aweyer;-- Allows user to create stored procedures
GRANT CREATE SEQUENCE TO aweyer; -- Allows user to create sequences
GRANT UNLIMITED TABLESPACE TO aweyer;  -- Allows unlimited use of tablespaces
grant dba to aweyer;

SELECT username FROM dba_users WHERE username = 'aweyer';

SELECT username, account_status, default_tablespace, temporary_tablespace, created 
FROM dba_users;





CREATE TABLE Hotel (
    hotelID NUMBER PRIMARY KEY,
    Name VARCHAR2(30) NOT NULL,
    City VARCHAR2(30) NOT NULL
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
