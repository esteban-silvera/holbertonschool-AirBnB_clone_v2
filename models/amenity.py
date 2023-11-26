#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
   """Amenities of a place"""
   __tablename__ = "amenities"
   name = Column(String(128), nullable=False)
   place_amenities = relationship('place', secondary='place_amenity',
                                  nullable=False)
 