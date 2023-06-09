import pymongo, os
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Extract env vars
db_name = os.environ['DB_NAME']
port = os.environ['DB_PORT']
server = os.environ['DB_SERVER']

# Create mongo client
client = pymongo.MongoClient(host=server, port=int(port), connect=True)

db = client[db_name]

# Create user & book collections
USERS = db['users']
BOOKS = db['books']

# USERS.__dict__