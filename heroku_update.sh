heroku login
heroku container:login
heroku container:push web -a pytracker-dev
heroku container:release web -a pytracker-dev
heroku open -a pytracker-dev