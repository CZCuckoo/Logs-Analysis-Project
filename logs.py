#!/usr/bin/env python

import psycopg2
from datetime import datetime


# establish connection to database
def connect(query):
    database = psycopg2.connect(database="news")
    c = database.cursor()
    c.execute(query)
    query_results = c.fetchall()
    database.close()
    return query_results


def print_results(query_results):
    # loop through rows to get results
    for i in query_results:
        # convert second half to string for concatination
        print(i[0] + ' - ' + str(i[1]))
    print '\n'


# Question 1: What are the most popular three articles of all time?
def print_popular_articles():
    print("-------------------------")
    print("The Most Popular Articles")
    print("-------------------------")
    query1 = """
            select title, page_views as views from popular_articles limit 3;
            """
    popular_articles = connect(query1)
    print_results(popular_articles)


# Question 2: Who are the most popular article authors of all time?
def print_popular_authors():
    print("-------------------------")
    print("The Most Popular Authors")
    print("-------------------------")
    query2 = """
            select name, page_views as views
            from popular_authors join authors
            on popular_authors.author = authors.id;
            """
    popular_authors = connect(query2)
    print_results(popular_authors)


# Question 3: On which days did more than 1% of requests lead to errors?
def print_error():
    print("-------------------------")
    print("Request Errors Above 1%")
    print("-------------------------")
    query3 = """
            select date, concat(concat(daily_errors.error_percentage, '%'),
            ' errors')
            as error_percentage
            from daily_errors
            """
    error_request = connect(query3)
    for i in error_request:
        # Take date in current format and make it easier to read via .strftime
        print(i[0].strftime('%B %d, %Y') + ' - ' + i[1])
        print '\n'

# Run all three functions when python file is executed
if __name__ == "__main__":
    print_popular_articles()
    print_popular_authors()
    print_error()
