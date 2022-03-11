{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # 
\fs20 Who is the owner with the most boats per country?\
SELECT id_owner\
FROM boat NATURAL JOIN owner NATURAL JOIN country\
GROUP BY iso_code\
HAVING COUNT(*)>= ALL(\
	SELECT COUNT(*)\
	FROM boat B\
	WHERE B.id_owner = id_owner\
	GROUP BY iso_code)\
;\
\
# List all the owners that have at least two boats in distinct countries.\
\
SELECT id_owner, iso_code\
FROM boat NATURAL JOIN country \
GROUP BY id_owner \
HAVING COUNT(DISTINCT(iso_code))>2;\
\
# Who are the sailors that have sailed to every location in 'Portugal'?\
SELECT id_sailor, end_latitude, end_longitude\
FROM trip NATURAL JOIN location NATURAL JOIN country\
HAVING COUNT(DISTINCT(name)) >= ALL(\
	SELECT COUNT(*)\
	FROM location NATURAL JOIN country\
	WHERE country.name = \'91Portugal\'92)\
;\
\
# List the sailors with the most trips along with their reservations\
SELECT id_sailor, COUNT(DISTINCT(start_date)), COUNT(DISTINCT(end_date))\
FROM reservation NATURAL JOIN trip\
HAVING COUNT(DISTINCT(start_date)) >= ALL(\
	SELECT COUNT(DISTINCT(start_date))\
	FROM reservation\
	GROUP BY id_sailor)\
AND HAVING COUNT(DISTINCT(end_date)) >= ALL(\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 	SELECT COUNT(DISTINCT(end_date))\
	FROM reservation\
	GROUP BY id_sailor)\
;\
\
#List the sailors with the longest duration of trips (sum of trip durations) for the same\
\pard\pardeftab720\partightenfactor0
\cf0 single reservation; display also the sum of the trip durations.\
\
SELECT id_sailor, SUM(duration))\
FROM reservation NATURAL JOIN trip\
HAVING SUM(DURATION) >= ALL(\
	SELECT SUM(duration)\
	FROM trip\
	GROUP BY (start_date,end_date))\
}