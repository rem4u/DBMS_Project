STEPS FOR RUNNING THIS APPLICATION:-
I have worked in Windows so will guide you through the steps to run the application in **Windows** 

- Download Git in windows (https://www.youtube.com/watch?v=J_Clau1bYco ,refer to this video and follow thw steps )

Create a Folder Name of your choice , and navigate to that folder

Clone this git repository using command : git clone https://github.com/rem4u/DBMS_Project.git

Now Install the **modules** that is required to run this application :- 
  -  Download and install Python, for this tutorial I'll be using Python 3.7.2, make sure to check the box Add Python to PATH on the installation setup screen.
  -  Download and install MySQL Community Server and MySQL Workbench. You can skip this step if you already have a MySQL server installed.
  -  Install Python Flask with the command: **pip install flask**
  -  Install Flask-MySQLdb with the command: **pip install flask-mysqldb**

**Create the following MYSQL tables**:-
 - register table:- CREATE table register(sno int not null auto_increment, name varchar(80) not null , email varchar(200) not null,password varchar(30) not null,college varchar(80) not null,PRIMARY KEY(`sno`));
 - user_experience:- CREATE table user_experience(sno int not null auto_increment, name varchar(80) not null, experience varchar(220) not null);
 - help_others:- CREATE table help_others(sno int not null auto_increment, name varchar(80), not null,role varchar(50) not null, requirement varchar(60), link varchar(40) , userid varchar(60));
 
**To run the application :-** 

execute the following command:- 

- python app.py / python3 app.py

