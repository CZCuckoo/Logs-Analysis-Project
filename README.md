# Logs-Analysis-Project

## Description
This is a project created for the Udacity Full Stack Web Developer Course. The intent is to simulate a real-life scenario in which you've been asked to build an internal reporting tool that will use information from this database to discover what kinds of articles the site's readers like. It poses three questions.

* <strong>What are the most popular three articles of all time?</strong>
* <strong>Who are the most popular article authors of all time?</strong>
* <strong>On which days did more than 1% of requests lead to errors?</strong>

Note that this project used Python3, and a Vagrant remote environment. The database we are working with can be found <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">here</a>.

This database includes three tables:
* Articles, which includes information about the authors, including a title, slug, and author ID.
* Authors, which includes the name, bio, and employee ID number for each reporter.
* Logs, which includes an entry for each attempted access of an article on the site, including the time, and whether the attempt was successful.

## Instructions

In order to successfully answer these questions, five views were created.

### popular_articles
This view uses the article and logs tables, matching the path within the log table to the slug within the articles table. In order to do so, we need to concatenate /article/ to each slug in order to match the path.
```sql
Create view popular_articles as
select title, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
group by articles.title
order by page_views desc;
```

### popular_authors
This view uses the authors and logs tables in the same way as the popular articles, matching the path within the log table to the slug within the articles table. In order to do so, we need to concatenate /article/ to each slug in order to match the path.
```sql
Create view popular_authors as
select author, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
group by articles.author
order by page_views desc;
```

### total_requests
This view uses the log table to determine the total number of requests on the site.
```sql
create view total_requests as
select date(time), count(*) as requests
from log
group by date
order by date desc;
```

### failed_requests
This view uses the log table to find all failed requests on the site by looking for the 404 status.
```sql
create view failed_requests
as select date(time), count(*) as requests
from log where status = '404 NOT FOUND'
group by date
order by date desc;
```

### daily_errors
This view uses the two previous views to divide failed requests by total requests, giving us a percentage of errors. It uses casting to convert both numbers to decimals, and multiplies them by 100, rounding them to 2 decimal places. It then checks to see if any of those totals are greater than 1%, in order to answer question 3.
```sql
create view daily_errors
as select failed_requests.date, round((failed_requests.requests::decimal/total_requests.requests::decimal * 100), 2) as error_percentage
from failed_requests, total_requests
where total_requests.date = failed_requests.date
and ((failed_requests.requests::decimal/total_requests.requests::decimal * 100) > 1.0)
order by failed_requests.date;
```

After these views are created, run logs.py. The output should look the same as is found in the output.txt file.
