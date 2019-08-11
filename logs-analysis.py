#!/usr/bin/env python

import psycopg2

print "\n\nConnecting to database..."
conn = psycopg2.connect(database="news")

cursor = conn.cursor()

print "Generating report...\n\n"

query = """ SELECT a.title, COUNT(*) as views
            FROM articles a
            JOIN log l on l.path LIKE '%' || a.slug || '%'
            WHERE l.status = '200 OK'
            GROUP BY a.title
            ORDER BY COUNT(*) DESC
            LIMIT 3;"""

cursor.execute(query)
results = cursor.fetchall()

print " ***************************** "
print " ********** RESULTS ********** "
print " ***************************** \n\n"

print " ***** Top 3 Articles of All Time ***** \n\n"

for r in results:
    print r[0] + " - " + str(r[1]) + " views"

query = """ SELECT ar.name, COUNT(*) as views
            FROM articles a
            JOIN log l on l.path LIKE '%' || a.slug || '%'
            JOIN authors ar on ar.id = a.author
            WHERE l.status = '200 OK'
            GROUP BY ar.name
            ORDER BY COUNT(*) DESC
            LIMIT 3;"""

cursor.execute(query)
results = cursor.fetchall()

print "\n\n ***** Author Leaderboard ***** \n\n"

for r in results:
    print r[0] + " - " + str(r[1]) + " article views"


query = """ SELECT view_date, COUNT(*) as errors,
            (SELECT COUNT(*) FROM log ls
             WHERE DATE(ls.time) = l.view_date) as views,
             CAST(COUNT(*) as decimal)/(SELECT COUNT(*)
             FROM log ls WHERE DATE(ls.time) = l.view_date) as error_rate
            FROM (SELECT status, DATE(time) as view_date from log) l
            WHERE status <> '200 OK'
            GROUP BY view_date
            HAVING CAST(COUNT(*) as decimal)/(SELECT COUNT(*)
             FROM log ls WHERE DATE(ls.time) = l.view_date) > 0.01"""

cursor.execute(query)
results = cursor.fetchall()

print "\n\n ***** High Error Days (1% or More) ***** \n\n"

for r in results:
    print str(r[0]) + " - " + str(r[1]) + " errors, "
    + str(r[2]) + " views, " + str(round(r[3]*100, 2)) + " %"


print "\n\n Report generation complete! Have a great day!"

conn.close()
