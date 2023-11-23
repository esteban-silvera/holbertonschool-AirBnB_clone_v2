#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
storage_type = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        if storage_type == 'db':  # for dbstorage
            cities = relationship('City', backref='state',
                                  cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter attribute for cities in FileStorage"""
            city_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
