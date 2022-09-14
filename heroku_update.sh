heroku login
heroku container:login
heroku container:push web -a pytracker-input
heroku container:release web -a pytracker-input
heroku open -a pytracker-input