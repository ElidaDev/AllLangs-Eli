sudo mysql -u root -proot
CREATE DATABASE IoT;

GRANT ALL PRIVILEGES ON IoT.* TO 'sictc'@'localhost';

FLUSH PRIVILEGES;

exit;

sudo mysql -u sictc -pPencil1

SHOW DATABASES;

USE IoT;

CREATE TABLE Accounts(
   Id int NOT NULL AUTO_INCREMENT,
   Name varchar(50),
   Address varchar(50),
   City varchar(50),
   State varchar(2),
   Zip varchar(10),
   LastUpdate timestamp DEFAULT CURRENT_TIMESTAMP,
   CreatedDate timestamp DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (Id)
);

INSERT INTO Accounts (Name, Address, City, State, Zip) VALUES ('SICTC', '1901 Lynch Rd', 'Evansville', 'IN', '47711');
INSERT INTO Accounts (Name, Address, City, State, Zip) VALUES ('Max Payne', '182 West 106th St.', 'New York', 'NY', '00544');


CREATE TABLE Users(
   Id int NOT NULL AUTO_INCREMENT,
   AccountId int, 
   Email varchar(200),
   LastName varchar(50), 
   FirstName varchar(50), 
   Password varchar(255),
   LastLogin timestamp NULL,
   LastUpdate timestamp NULL,
   CreatedDate timestamp DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (Id),
   UNIQUE KEY (Email)
);

INSERT INTO Users (AccountId, Email, LastName, FirstName, Password) VALUES(1, 'johnc@sictc.edu', 'Cobb', 'John', SHA1('Pencil1'));

CREATE TABLE IoT(
   Id int NOT NULL AUTO_INCREMENT,
   AccountId int NOT NULL,
   TypeId int NOT NULL,
   IMEI char(16) NOT NULL,
   Serial varchar(20) NOT NULL, 
   Name varchar(50) NOT NULL, 
   Lat int, 
   Lng int, 
   Alt int, 
   Speed int,
   Direction int,
   Bearing int, 
   LastUpdate timestamp NULL,
   CreatedDate timestamp DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (Id)
);

CREATE TABLE Groups(
   Id int NOT NULL AUTO_INCREMENT,  
   AccountId int NOT NULL,
   Name varchar(50),
   LastUpdate timestamp NULL,
   CreatedDate timestamp DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (Id)
);


CREATE TABLE IoTGroups(
   Id int NOT NULL AUTO_INCREMENT,  
   IoTId int NOT NULL,
   GroupId int NOT NULL,
   CreatedDate timestamp DEFAULT CURRENT_TIMESTAMP, 
   PRIMARY KEY (Id)
);
 
CREATE TABLE States(
   Id int NOT NULL AUTO_INCREMENT, 
   States varchar(2),
   PRIMARY KEY (Id)
);
 
INSERT INTO States (State) VALUES ('AL');
INSERT INTO States (State) VALUES ('AK');
INSERT INTO States (State) VALUES ('AZ');
INSERT INTO States (State) VALUES ('AR');
INSERT INTO States (State) VALUES ('CA');
INSERT INTO States (State) VALUES ('CO');
INSERT INTO States (State) VALUES ('CT');
INSERT INTO States (State) VALUES ('DE');
INSERT INTO States (State) VALUES ('FL');
INSERT INTO States (State) VALUES ('GA');
INSERT INTO States (State) VALUES ('HI');
INSERT INTO States (State) VALUES ('ID');
INSERT INTO States (State) VALUES ('IL');
INSERT INTO States (State) VALUES ('IN');
INSERT INTO States (State) VALUES ('IA');
INSERT INTO States (State) VALUES ('KS');
INSERT INTO States (State) VALUES ('KY');
INSERT INTO States (State) VALUES ('LA');
INSERT INTO States (State) VALUES ('ME');
INSERT INTO States (State) VALUES ('MD');
INSERT INTO States (State) VALUES ('MA');
INSERT INTO States (State) VALUES ('MI');
INSERT INTO States (State) VALUES ('MN');
INSERT INTO States (State) VALUES ('MS');
INSERT INTO States (State) VALUES ('MO');
INSERT INTO States (State) VALUES ('MT');
INSERT INTO States (State) VALUES ('NE');
INSERT INTO States (State) VALUES ('NV');
INSERT INTO States (State) VALUES ('NH');
INSERT INTO States (State) VALUES ('NJ');
INSERT INTO States (State) VALUES ('NM');
INSERT INTO States (State) VALUES ('NY');
INSERT INTO States (State) VALUES ('NC');
INSERT INTO States (State) VALUES ('ND');
INSERT INTO States (State) VALUES ('OH');
INSERT INTO States (State) VALUES ('OK');
INSERT INTO States (State) VALUES ('OR');
INSERT INTO States (State) VALUES ('PA');
INSERT INTO States (State) VALUES ('RI');
INSERT INTO States (State) VALUES ('SC');
INSERT INTO States (State) VALUES ('SD');
INSERT INTO States (State) VALUES ('TN');
INSERT INTO States (State) VALUES ('TX');
INSERT INTO States (State) VALUES ('UT');
INSERT INTO States (State) VALUES ('VT');
INSERT INTO States (State) VALUES ('VA');
INSERT INTO States (State) VALUES ('WA');
INSERT INTO States (State) VALUES ('WV');
INSERT INTO States (State) VALUES ('WI');
INSERT INTO States (State) VALUES ('WY');
