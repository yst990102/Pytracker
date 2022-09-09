heroku login
sh docker_run.sh
heroku container:login
heroku container:push web -a pytracker
heroku container:release web -a pytracker
heroku open -a pytracker