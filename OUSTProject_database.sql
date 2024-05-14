-- Student Number: 10541054
-- Student Name:	Andrea Marcosano


IF DB_ID('OUSTProject') IS NOT NULL             
	BEGIN
		PRINT 'If DB firm exist, drop it';
		
		USE master;		
		ALTER DATABASE OUSTProject SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
		
		DROP DATABASE OUSTProject;
	END
GO

PRINT 'Create DB OUSTProject';

CREATE DATABASE OUSTProject;

GO

-- Use OUSTProject

USE OUSTProject;

GO
-------------------------------------------------------------------------------------------
-- Create database tables
-------------------------------------------------------------------------------------------

-- Create Student Table, stores details about the students

PRINT 'Creating Student table...';

CREATE TABLE Student
(
	Student_ID VARCHAR(8) NOT NULL PRIMARY KEY ,
	First_Name VARCHAR(50) NOT NULL,
	Last_Name VARCHAR(50) NOT NULL,
	Email VARCHAR(50) NOT NULL,
	Mobile_phone VARCHAR(20) NOT NULL 

);
-- Create coordinator, stores all the data of the coordinator of the course

PRINT 'Creating Coordinator Table...'

CREATE TABLE Coordinator
(
	Coordinator_ID VARCHAR(8) NOT NULL PRIMARY KEY ,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	Email VARCHAR(50) NOT NULL,
	Mobile_phone VARCHAR(20) NOT NULL 

);

-- Create paylevel Table, stores details of the different courses

PRINT 'Creating Course Table...'

CREATE TABLE Course
(
	Course_Code VARCHAR(3) NOT NULL PRIMARY KEY,
	Course_Title VARCHAR(100) NOT NULL,
	year_start_offer VARCHAR(4) NOT NULL,
	year_end_offer VARCHAR(4) NULL,
	Coordinator_ID VARCHAR(8) NULL

	CONSTRAINT Coordinator_ID FOREIGN KEY (Coordinator_ID) REFERENCES Coordinator(Coordinator_ID),
);

-- Create Unit Table, stores details about the Units

PRINT 'Creating Unit Table...'
CREATE TABLE Unit
(
	Record_N int NOT NULL PRIMARY KEY IDENTITY,
	Unit_Code VARCHAR(7) NOT NULL,
	Unit_Title VARCHAR(50) NOT NULL,
	Score FLOAT NOT NULL,
	Grade VARCHAR(2) NULL,

	Student_ID VARCHAR(8) NOT NULL FOREIGN KEY REFERENCES  Student(Student_ID),
	Course_Code VARCHAR(3) NOT NULL FOREIGN KEY REFERENCES Course(Course_code),


	CONSTRAINT Score CHECK (Score > 0.0 AND Score <= 100.0)
	
);

--insert valuent into table student
INSERT INTO Student
VALUES ('20241201', 'jim', 'MAX', 'j.max@our.oust.edu.au', '2024120201'),
		('20241202', 'jit', 'MAX', 'jt.max@our.oust.edu.au', '2024120202'),
		('20241203', 'late', 'MAX', 'l.max@our.oust.edu.au', '2024120203'),
		('20241204', 'rep', 'SMITH', 'r.smith@our.oust.edu.au', '2024120204'),
		('20241205', 'paul', 'LANDAN', 'p.landan@our.oust.edu.au', '2024120205'),
		('20241206', 'peter', 'LONDON', 'p.london@our.oust.edu.au', '2024120206'),
		('20241207', 'john', 'TURNER', 'j.turner@our.oust.edu.au', '2024120207'),
		('20241208', 'jim', 'XIAO', 'j.XIAO@our.oust.edu.au', '2024120208');


--insert valuent into table Coordinator
INSERT INTO Coordinator
VALUES ('11111111', 'John','Paul', 'john.paul@gmail.com','201256325'),
	   ('22222222', 'Josh','Max','josh.max@gmail.com','201256326'),
	   ('33333333', 'Max','Gello', 'max.gello@gmail.com','20125632'),
	   ('44444444', 'Jitian', 'Xiao','jitian.xiao@gmail.com','201256328'),
	   ('55555555', 'Mathew', 'landan', 'mathew.landan@gmail.com', '201256329'),
	   ('66666666', 'Greg', 'Smith', 'greg.smith@gmail.com','201256320');



--insert valuent into table Course
INSERT INTO Course
VALUES ('Y64', 'Bachelor of computer Science', 2001, NULL,'44444444' ),
		('Y63', 'Bachelor of computer System', 2002, NULL,'33333333' ),
		('Y62', 'Bachelor of Electric engineering', 2002, NULL,'66666666' ),
		('Y61', 'Bachelor of cybersecurity', 2002, NULL,'22222222' ),
		('Y59', 'Civil Engineering', 2004, NULL,'11111111' ),
		('Y58', 'Mechanical engineering', 2002, NULL,'55555555' ),
		('Y57', 'Bachelor of Mechatronics', 2002, NULL,'22222222' );

--insert valuent into table unit
--first student student id 20241201 course Y64
INSERT INTO Unit
VALUES('Unit_0', 'Unit_title_000', 86.6, NULL, '20241201', 'Y64'),
('Unit_1', 'Unit_title_001', 86.6, NULL, '20241201', 'Y64'),
('Unit_2', 'Unit_title_002', 76.6, NULL, '20241201', 'Y64'),
('Unit_3', 'Unit_title_003', 66.6, NULL, '20241201', 'Y64'),
('Unit_4', 'Unit_title_004', 56.6, NULL, '20241201', 'Y64'),
('Unit_5', 'Unit_title_005', 46.6, NULL, '20241201', 'Y64'), --class failed twice
('Unit_5', 'Unit_title_005', 36.6, NULL, '20241201', 'Y64'),
('Unit_5', 'Unit_title_005', 78.6, NULL, '20241201', 'Y64'),
('Unit_6', 'Unit_title_006', 94.6, NULL, '20241201', 'Y64'),
('Unit_7', 'Unit_title_007', 55.6, NULL, '20241201', 'Y64'),
('Unit_8', 'Unit_title_008', 66.6, NULL, '20241201', 'Y64'),
('Unit_9', 'Unit_title_009', 77.6, NULL, '20241201', 'Y64'),
('Unit_10', 'Unit_title_010', 88.6, NULL, '20241201', 'Y64'),
('Unit_11', 'Unit_title_011', 86.9, NULL, '20241201', 'Y64'),
('Unit_12', 'Unit_title_012', 83.6, NULL, '20241201', 'Y64'),
('Unit_13', 'Unit_title_013', 82.6, NULL, '20241201', 'Y64'),
('Unit_14', 'Unit_title_014', 55.6, NULL, '20241201', 'Y64'),
('Unit_15', 'Unit_title_015', 23.6, NULL, '20241201', 'Y64'), --class failed once
('Unit_15', 'Unit_title_015', 53.6, NULL, '20241201', 'Y64'),
('Unit_16', 'Unit_title_016', 86.6, NULL, '20241201', 'Y64'),
('Unit_17', 'Unit_title_017', 99.6, NULL, '20241201', 'Y64'),
('Unit_18', 'Unit_title_018', 78.6, NULL, '20241201', 'Y64'),
('Unit_19', 'Unit_title_019', 79.6, NULL, '20241201', 'Y64'),
('Unit_20', 'Unit_title_020', 56.6, NULL, '20241201', 'Y64'),
('Unit_21', 'Unit_title_021', 76.6, NULL, '20241201', 'Y64'),
('Unit_22', 'Unit_title_022', 96.6, NULL, '20241201', 'Y64'),
('Unit_23', 'Unit_title_023', 76.6, NULL, '20241201', 'Y64'),
('Unit_24', 'Unit_title_024', 66.6, NULL, '20241201', 'Y64');

--insert valuent into table unit
--first student student id 20241202 course Y63
INSERT INTO Unit
VALUES('Unit_0', 'Unit_title_000', 86.6, NULL, '20241202', 'Y63'),
('Unit_1', 'Unit_title_001', 66.6, NULL, '20241202', 'Y63'),
('Unit_2', 'Unit_title_002', 76.6, NULL, '20241202', 'Y63'),
('Unit_3', 'Unit_title_003', 66.6, NULL, '20241202', 'Y63'),
('Unit_4', 'Unit_title_004', 56.6, NULL, '20241202', 'Y63'),
('Unit_5', 'Unit_title_005', 46.6, NULL, '20241202', 'Y63'), --class failed twice
('Unit_5', 'Unit_title_005', 36.6, NULL, '20241202', 'Y63'),
('Unit_5', 'Unit_title_005', 78.6, NULL, '20241202', 'Y63'),
('Unit_6', 'Unit_title_006', 94.6, NULL, '20241202', 'Y63'),
('Unit_7', 'Unit_title_007', 55.6, NULL, '20241202', 'Y63'),
('Unit_8', 'Unit_title_008', 66.6, NULL, '20241202', 'Y63'),
('Unit_9', 'Unit_title_009', 77.6, NULL, '20241202', 'Y63'),
('Unit_10', 'Unit_title_010', 88.6, NULL, '20241202', 'Y63'),
('Unit_11', 'Unit_title_011', 86.9, NULL, '20241202', 'Y63'),
('Unit_12', 'Unit_title_012', 83.6, NULL, '20241202', 'Y63'),
('Unit_13', 'Unit_title_013', 52.6, NULL, '20241202', 'Y63'),
('Unit_14', 'Unit_title_014', 55.6, NULL, '20241202', 'Y63'),
('Unit_15', 'Unit_title_015', 23.6, NULL, '20241202', 'Y63'), --class failed once
('Unit_15', 'Unit_title_015', 53.6, NULL, '20241202', 'Y63'),
('Unit_16', 'Unit_title_016', 86.6, NULL, '20241202', 'Y63'),
('Unit_17', 'Unit_title_017', 19.6, NULL, '20241202', 'Y63'), --failed class twice
('Unit_17', 'Unit_title_017', 49.6, NULL, '20241202', 'Y63'),
('Unit_17', 'Unit_title_017', 59.6, NULL, '20241202', 'Y63'),
('Unit_18', 'Unit_title_018', 78.6, NULL, '20241202', 'Y63'),
('Unit_19', 'Unit_title_019', 79.6, NULL, '20241202', 'Y63'),
('Unit_20', 'Unit_title_020', 56.6, NULL, '20241202', 'Y63'),
('Unit_21', 'Unit_title_021', 76.6, NULL, '20241202', 'Y63'),
('Unit_22', 'Unit_title_022', 56.6, NULL, '20241202', 'Y63'),
('Unit_23', 'Unit_title_023', 56.6, NULL, '20241202', 'Y63'),
('Unit_24', 'Unit_title_024', 56.6, NULL, '20241202', 'Y63');

--insert valuent into table unit
--first student student id 20241203 course Y62
INSERT INTO Unit
VALUES ('Unit_0', 'Unit_title_000', 66.6, NULL, '20241203', 'Y62'),
('Unit_1', 'Unit_title_001', 66.6, NULL, '20241203', 'Y62'),
('Unit_2', 'Unit_title_002', 76.6, NULL, '20241203', 'Y62'),
('Unit_3', 'Unit_title_003', 66.6, NULL, '20241203', 'Y62'),
('Unit_4', 'Unit_title_004', 55.6, NULL, '20241203', 'Y62'),
('Unit_5', 'Unit_title_005', 45.6, NULL, '20241203', 'Y62'), --class failed twice
('Unit_5', 'Unit_title_005', 35.6, NULL, '20241203', 'Y62'),
('Unit_5', 'Unit_title_005', 75.6, NULL, '20241203', 'Y62'),
('Unit_6', 'Unit_title_006', 95.6, NULL, '20241203', 'Y62'),
('Unit_7', 'Unit_title_007', 50.6, NULL, '20241203', 'Y62'),
('Unit_8', 'Unit_title_008', 66.6, NULL, '20241203', 'Y62'),
('Unit_9', 'Unit_title_009', 77.6, NULL, '20241203', 'Y62'),
('Unit_10', 'Unit_title_010', 68.6, NULL, '20241203', 'Y62'),
('Unit_11', 'Unit_title_011', 66.9, NULL, '20241203', 'Y62'),
('Unit_12', 'Unit_title_012', 63.6, NULL, '20241203', 'Y62'),
('Unit_13', 'Unit_title_013', 52.6, NULL, '20241203', 'Y62'),
('Unit_14', 'Unit_title_014', 55.6, NULL, '20241203', 'Y62'),
('Unit_15', 'Unit_title_015', 23.6, NULL, '20241203', 'Y62'), --class failed once
('Unit_15', 'Unit_title_015', 53.6, NULL, '20241203', 'Y62'),
('Unit_16', 'Unit_title_016', 86.6, NULL, '20241203', 'Y62'),
('Unit_17', 'Unit_title_017', 19.6, NULL, '20241203', 'Y62'), --failed class twice
('Unit_17', 'Unit_title_017', 49.6, NULL, '20241203', 'Y62'),
('Unit_17', 'Unit_title_017', 59.6, NULL, '20241203', 'Y62'),
('Unit_18', 'Unit_title_018', 68.6, NULL, '20241203', 'Y62'),
('Unit_19', 'Unit_title_019', 69.6, NULL, '20241203', 'Y62'),
('Unit_20', 'Unit_title_020', 56.6, NULL, '20241203', 'Y62'),
('Unit_21', 'Unit_title_021', 76.6, NULL, '20241203', 'Y62'),
('Unit_22', 'Unit_title_022', 56.6, NULL, '20241203', 'Y62'),
('Unit_23', 'Unit_title_023', 56.6, NULL, '20241203', 'Y62'),
('Unit_24', 'Unit_title_024', 56.6, NULL, '20241203', 'Y62');


--function to populate grade 
UPDATE Unit
SET Grade = 
        CASE 
            WHEN Score < 50 THEN 'F'
            WHEN Score >= 50 AND Score < 60 THEN 'P'
            WHEN Score >= 60 AND Score < 70 THEN 'CR'
            WHEN Score >= 70 AND Score < 80 THEN 'D'
            WHEN Score >= 80 THEN 'HD'
        END
    FROM Unit
