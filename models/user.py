#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the review instance"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Return a dictionary representation of the Review instance"""
        review_dict = super().to_dict()  # Call to_dict of BaseModel
        review_dict.update({
            'text': self.text,
            'place_id': self.place_id,
            'user_id': self.user_id,
        })
        return review_dict




