#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import csv
import pymysql as mydb
import sys

#Creating connection to the database
connection = mydb.connect(host='localhost', user='root', passwd='', database='refactoringprojectdb')

#Selecting 1500 commit messages containing different keywords from the list but not all of them
query = '(select c.commitid, replace(replace(replace(c.commitmessage, ",", ""), "=", ""), "-", "") from commit c where lower(c.commitmessage) like "%Refactor%" limit 200) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%Renam%" limit 150) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%Correct%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%Improv%" limit 100) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%Cleanup%" limit 100) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%push%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%Extract%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%Enhanc%" limit 100) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%polish%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%tidy%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%structur%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%organiz%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%simplif%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%clarif%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%Duplicate code%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%naming improvements%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%normaliz%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%redesign%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%typo%" limit 70) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%separat%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%encapsulat%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%avoid future confusion%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%use less code%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%pull out%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%remove redundant code%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%formatted%" limit 50) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%sorting%" limit 13) union (select c.commitid, replace(c.commitmessage, ",", "") from commit c where lower(c.commitmessage) like "%cleaning%" limit 50)';

#Creating cursor to execute the query and get the data from the DB
mycursor = connection.cursor()
mycursor.execute(query)

#Saving all the result from my cursor
result = mycursor.fetchall()

#Creating a csv file to then open it and save the results
fname = 'MessageswithKeywordsOFFICIAL.csv'
c = csv.writer(open('MessageswithKeywordsOFFICIAL.csv', 'wb'))
for row in result:
	c.writerow(row)
