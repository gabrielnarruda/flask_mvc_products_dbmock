import peewee
from swagger_server.models.base_model import BaseModel


class Produtos(BaseModel):
    id = peewee.IntegerField()
    json_data = peewee.CharField()
