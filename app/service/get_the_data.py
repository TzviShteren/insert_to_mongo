from app.repository.init_data import insert_event_to_mongo
from app.service.kafka_settings.consumer import consume
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)


def get_student():
    consume(
        topic=os.environ['GLOBAL_TERRORISM'],
        function=insert_event_to_mongo,
    )
