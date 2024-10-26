#!/usr/bin/python3
# models/city.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """Representation of city"""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    # Relationship with State
    state = relationship("State", backref="cities")

    def __init__(self, *args, **kwargs):
        """Initializes the city instance"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Return a dictionary representation of the City instance"""
        city_dict = super().to_dict()  # Call to_dict of BaseModel
        city_dict.update({
            'state_id': self.state_id,
            'name': self.name,
        })
        return city_dict

