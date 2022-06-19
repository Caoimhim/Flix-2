import os
from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP,
    Text,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base

dbname='localhost:5432/movies'

def get_postgres_uri():
    #host = os.environ.get("DATABASE_URL", "postgres")
    host = "ec2-54-157-16-196.compute-1.amazonaws.com"
    port = 5432
    #password = os.environ.get("DB_PASS", "abc123")
    password = "a220896f9f98e61b782d00faf5fc12be1dc660dda09dfbf38d3d107af0c89038"
    user, db_name = "jbffakrqdahvzx", "dcne8ihbq22hi7"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


Base = declarative_base(
    metadata=MetaData(),
)


engine = create_engine(
    get_postgres_uri(),
    isolation_level="REPEATABLE READ",
    connect_args={'ssl_context': True}
)


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    create_time = Column(TIMESTAMP(timezone=True), index=True)


def start_mappers():
    Base.metadata.create_all(engine)
