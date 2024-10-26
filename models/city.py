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

    # Relationship with Place
    places = relationship("Place", cascade="all, delete-orphan", backref="city")

    def __init__(self, *args, **kwargs):
        """Initializes city instance"""
        super().__init__(*args, **kwargs)

    @property
    def places(self):
        """Returns the list of Place instances associated with the current City."""
        from models import storage
        place_list = []
        place_dict = storage.all(Place)
        for place in place_dict.values():
            if place.city_id == self.id:
                place_list.append(place)
        return place_list

    def to_dict(self):
        """Return a dictionary representation of the City instance."""
        city_dict = super().to_dict()  # Call to_dict of BaseModel
        city_dict.update({
            'name': self.name,
            'state_id': self.state_id,
        })
        return city_dict


