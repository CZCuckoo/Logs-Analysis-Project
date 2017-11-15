import psycopg2
from datetime import datetime

def connect(query):
    database = psycopg2.connect(database="news")
    c = database.cursor()
    c.execute(query)
    query_results = c.fetchall()
    database.close()
    return query_results

def print_results(query_results):
    # Iterate over the rows and get our results
    for i in query_results:
        print(i[0] + ' - ' + str(i[1]))
    print '\n'

def print_popular_articles():
    print("-------------------------")
    print("The Most Popular Articles")
    print("-------------------------")
    query1 = """
            select title, page_views as views from popular_articles limit 3;
            """
    popular_articles = connect(query1)
    print_results(popular_articles)

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
        print(i[0].strftime('%B %d, %Y') + ' - ' + i[1])
        print '\n'

if __name__ == "__main__":
    print_popular_articles()
    print_popular_authors()
    print_error()
