# Logs-Analysis-Project

## Description
This is a project created for the Udacity Full Stack Web Developer Course. The intent is to simulate a real-life scenario in which you've been asked to build an internal reporting tool that will use information from this database to discover what kinds of articles the site's readers like. It poses three questions.

* <strong>What are the most popular three articles of all time?</strong>
* <strong>Who are the most popular article authors of all time?</strong>
* <strong>On which days did more than 1% of requests lead to errors?</strong>

Note that this project uses Python3, and a Vagrant remote environment. The database we are working with can be found <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">here</a>.

This database includes three tables:
* Articles, which includes information about the authors, including a title, slug, and author ID.
* Authors, which includes the name, bio, and employee ID number for each reporter.
* Logs, which includes an entry for each attempted access of an article on the site, including the time, and whether the attempt was successful.

## Instructions

In order to successfully answer these questions, five views were created.

```sql
Create view popular_articles as
select title, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
group by articles.title
order by page_views desc;
```

```sql
Create view top_authors as
select author, count(*) as page_views
from articles join log
on log.path = concat('/article/', articles.slug)
group by articles.author
order by page_views desc;
```

```sql
create view total_requests as
select date(time), count(*) as requests
from log
group by date
order by date desc;
```

```sql
create view failed_requests
as select date(time), count(*) as requests
from log where status = '404 NOT FOUND'
group by date
order by date desc;
```

```sql
create view daily_errors
as select failed_requests.date, round((failed_requests.requests::decimal/total_requests.requests::decimal * 100), 2) as error_percentage
from failed_requests, total_requests
where total_requests.date = failed_requests.date
and ((failed_requests.requests::decimal/total_requests.requests::decimal * 100) > 1.0)
order by failed_requests.date;
```

After these views are created, run logs.py.
