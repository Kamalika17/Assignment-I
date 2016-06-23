#!/usr/bin/python
import MySQLdb
import re
f1= open('mutect_immediate.vcf','r') #opening file mutect_immediate.vcf to read
f2= open('quality_mutation.txt','w') #new file to be written into
db = MySQLdb.connect(host="localhost",user="root",passwd="kamalika",db="mysql") #connecting mysql to python
cursor = db.cursor() 
comm_1= "CREATE TABLE IF NOT EXISTS my_vcf ( CHROM VARCHAR (30) NOT NULL ,POS VARCHAR(30) NULL,ID VARCHAR(20) NULL,REF VARCHAR(30) NULL,ALT VARCHAR(20) NULL,QUAL VARCHAR(30) NULL,FILTER VARCHAR(30) NULL,INFO VARCHAR(70) NULL,SAMPLE VARCHAR(50) NULL);" #Answer to Question 3a
comm_2= "INSERT INTO my_vcf (CHROM,POS,ID,REF,ALT,QUAL,FILTER,INFO,SAMPLE) VALUES (%s, %s , %s , %s , %s ,%s , %s , %s , %s);" #Answer to Question 3b
comm_3="SELECT * from my_vcf WHERE QUAL REGEXP '^[0-9]+$' AND QUAL < 500 AND QUAL > 50 ;" #Answer to Question 3c
cursor.execute(comm_1) #creating table
for i in f1:
	if not re.search('^#.*',i): #searching for lines without '#'
		temp = i.split()
		cursor.execute(comm_2,(temp[0],int(temp[1]),temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[10])) #Inserting values to table
cursor.execute(comm_3) #extracting mutation with quality < 500 and > 50
for j in cursor:
	f2.write(str(j)) #writing mutations to text file
db.commit()
db.close()
f1.close()
f2.close()
