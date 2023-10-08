import uuid
from bson import ObjectId
import random
import string

class IDGenerator:
    def generate_ids(self, id_type, quantity):
        if id_type == 'uuid':
            return [str(uuid.uuid4()) for _ in range(quantity)]
        elif id_type == 'objectid':
            return [str(ObjectId()) for _ in range(quantity)]
        elif id_type == 'numeric':
            return [str(random.randint(0, 999999999)) for _ in range(quantity)]
        elif id_type == 'string':
            return [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(quantity)]
        elif id_type == 'wep':
            return [''.join(random.choices('0123456789ABCDEF', k=26)) for _ in range(quantity)]
        else:
            raise ValueError(f'Invalid ID type: {id_type}')
