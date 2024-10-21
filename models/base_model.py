#!/usr/bin/python3
"""State Module for AirBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    
	
	""" Representation of state """
	__tablename__ = 'state'
	
	name = Column(String(128), nullable=False)
	
if getenv('HBNB_TYPE_StORAGE'):
== 'db':
cities = relationship('City', cascade='all, delete', backref='state')
	
else:
@property
def cities(self):
			""" returns the list of City instances with state_id equals to the current State.id """
			from models import storage
				
			from models.city import City
				
			city_list = []
			city_dict = storage.all(City)
				
			for city in city_dict. values():
				
				for city in city_dict.values():
					if city.state_id == self.id:
						city_list.append(city)
				return city_list
				
				
			def __init__(self, *args, **kwargs):
				"""initializes state"""
				super().__init__(args, **kwargs)
