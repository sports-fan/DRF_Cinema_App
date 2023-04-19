## Cinema App
### Add new movies to a cinema program, via api. Each movie has:
- name
- protagonists
- poster (image)
- start_date
- status (coming-up, starting, running, finished)
- ranking (the field to help us sort “trending” rooms

### Sync postgres movie instances to mongodb, account all the cases (creation, deletion, etc). 

### The ranking of each movie can be faked at first, however from the movie creation(status=upcoming) to the movie launch (status=running), the rank of each instance increases by 10, once every 5 minutes.

### Add api to list sorted trending movies from mongodb. 

### Code was tested right using Pytest

## Stack: Postgres | MongoDB | Celery | Redis | RabbitMQ | Django ninja.
