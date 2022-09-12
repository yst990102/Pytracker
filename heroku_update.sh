heroku login
heroku container:login
heroku container:push web -a pytracker
heroku container:release web -a pytracker
heroku open -a pytracker