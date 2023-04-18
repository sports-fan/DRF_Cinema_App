from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from pymongo import MongoClient
from .models import Movie

mongo_client = MongoClient(host='localhost',
                        port=int(27017),
                        username="admin",
                        password="password"
                        )
mongo_db = mongo_client['cinemaApp']
mongo_movies = mongo_db["movies"]

@receiver(post_save, sender=Movie)
def sync_created_or_updated_movie(sender, instance, created, **kwargs):
    if created:
        print("Created")
        print(instance.started_at)
        # Create a new movie in MongoDB
        mongo_movies.insert_one({
            '_id': instance.id,
            'name': instance.name,
            'protagonists': instance.protagonists,
            'poster': instance.poster,
            'started_at': instance.started_at,
            'status': instance.status,
            'ranking': instance.ranking
        })
    else:
        # Update the movie in MongoDB
        mongo_movies.update_one(
            {'_id': instance.id},
            {'$set': {
                'name': instance.name,
                'protagonists': instance.protagonists,
                'poster': instance.poster,
                'started_at': instance.started_at,
                'status': instance.status,
                'ranking': instance.ranking
            }}
        )

@receiver(post_delete, sender=Movie)
def sync_deleted_movie(sender, instance, **kwargs):
    # Delete the movie in MongoDB
    mongo_movies.delete_one({'_id': instance.id})
