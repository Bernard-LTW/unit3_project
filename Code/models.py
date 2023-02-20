from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

class Vocabulary(Base):
    __tablename__ = 'vocabulary'
    id = Column(Integer, primary_key=True)
    lesson = Column(Integer, nullable=False)
    part_of_lesson = Column(Integer, nullable=False)
    katakana = Column(String, nullable=False)
    hiragana = Column(String, nullable=False)
    definition = Column(String, nullable=False)
    stats = relationship("UserStats", back_populates="vocabulary", order_by="UserStats.lesson, UserStats.part_of_lesson")

class UserStats(Base):
    __tablename__ = 'user_stats'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    vocabulary_id = Column(Integer, ForeignKey('vocabulary.id'))
    lesson = Column(Integer, nullable=False)
    part_of_lesson = Column(Integer, nullable=False)
    correct = Column(Integer, nullable=False)
    incorrect = Column(Integer, nullable=False)
    user = relationship("Users", back_populates="user_stats")
    Users.user_stats = relationship("UserStats", order_by=id, back_populates="user")
    vocabulary = relationship("Vocabulary", back_populates="stats")






