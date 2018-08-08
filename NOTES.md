## Heroku Deployment

```
heroku apps:create interactive-elastic
heroku git:remote --app interactive-elastic
heroku addons:create searchbox:starter
heroku config:set SECRET_KEY=12345678
heroku config:set FLASK_ENV=Production
```
