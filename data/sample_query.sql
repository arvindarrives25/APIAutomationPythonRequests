
CREATE DATABASE API;

use API;
CREATE TABLE TrainingInfo

(CourseName varchar(50),

PurchasedDate date,

Amount int(50),

Location varchar(50));



INSERT INTO TrainingInfo values("selenium",CURRENT_DATE(),120,'India');

INSERT INTO TrainingInfo values("Cypress",CURRENT_DATE(),45,'London');

INSERT INTO TrainingInfo values("MobileAutomation",CURRENT_DATE(),99,'Australia');

INSERT INTO TrainingInfo values("WebServices",CURRENT_DATE(),21,'Goa');

INSERT INTO TrainingInfo values("Webstress",CURRENT_DATE(),76,'Kolkata');

CREATE TABLE program

(programName varchar(50),

isbn varchar(50),

aisle varchar(50),

author varchar(50));

INSERT INTO program values("Devops","bid123","75","Arvind_devops");
INSERT INTO program values("Selenium","bid345","23","Arvind_selenium");
INSERT INTO program values("AWS","bid678","234","Arvind_aws");
select * from program;
select * from TrainingInfo;