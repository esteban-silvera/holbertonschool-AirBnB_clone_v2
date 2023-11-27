#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey,Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import os
storage_type = os.getenv('HBNB_TYPE_STORAGE')

# metadata = Base.metadata
# place_amenity = Table('place_amenity', metadata,
                       #Column('place_id',String(60),ForeignKey
                        # ('places.id'), primary_key=True, nullable=
                        # False),
                        # Column('amenity_id', String(60), ForeignKey
                         #('amenities.id'), primary_key=True, nullable=
                         # False))
        
class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    if storage_type == 'db':
     reviews = relationship("Review", backref="place", 
                            cascade="all, delete-orphan") # For DBStorage
     #amenities = relationship("Amenity", secondary="place_amenity", backref="place_amenities", 
                              #viewonly=False)
     

   # else:
      # @property  # For FileStorage
      # def reviews(self):
       #  """Getter attribute for reviews in FileStorage"""
       # from models import storage
       #  list = []
      # for v in storage.all(Review).values():
       #   if v.place.id == self.id:
        #    list.append(v)
        #  return list
      # @property
      # def amenities(self):
       # """getter attr for amenity in Filestorage"""
       # from models import storage
       # list = []
        # for v in storage.all(Amenity).values():
        #  if v.amenity_ids == self.id:
         #   list.append(v)
         #  return list
        
     # @amenities.setter
      # def amenities(self, v):
       # """setter for amenities"""
       # if type(value) is Amenity:
        #  self.amenity_ids.append(value.id)
