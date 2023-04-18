from cinemaApp.celery import app

@app.task
def increase_ranking():
    print("OK")