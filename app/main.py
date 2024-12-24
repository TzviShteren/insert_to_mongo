from dotenv import load_dotenv
from app.repository.index import insert_indexes
from app.service.get_the_data import get_student

load_dotenv(verbose=True)

if __name__ == '__main__':
    insert_indexes()
    get_student()
