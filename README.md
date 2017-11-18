# Logs-Analysis-Project

## Description
This is a project created for the Udacity Full Stack Web Developer Course. The intent is to simulate a real-life scenario in which you've been asked to build an internal reporting tool that will use information from this database to discover what kinds of articles the site's readers like. It poses three questions.

* <strong>What are the most popular three articles of all time?</strong>
* <strong>Who are the most popular article authors of all time?</strong>
* <strong>On which days did more than 1% of requests lead to errors?</strong>

Note that this project uses Python3, and a Vagrant remote environment. The database we are working with can be found <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">here</a>.

## Instructions
This database includes three tables:
* Articles, which includes information about the authors, including a title, slug, and author ID.
* Authors, which includes the name, bio, and employee ID number for each reporter.
* Logs, which includes an entry for each attempted access of an article on the site, including the time, and whether the attempt was successful. 
