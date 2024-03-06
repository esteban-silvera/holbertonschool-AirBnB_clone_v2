#!/usr/bin/python3
""" coments """


from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
from models.city import City
from models import storage


storage_type = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ coment """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type != 'db':
        @property
        def cities(self):
            """
            Getter attribute that returns the list of City instances
            with state_id equals to the current State.id
            """
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
