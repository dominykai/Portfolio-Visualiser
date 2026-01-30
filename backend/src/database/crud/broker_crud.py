import csv
import os
from typing import Optional

from sqlalchemy.orm import Session

from backend.src.database.models.broker_model import Broker
from backend.src.utils.sys_utils import get_file_from_assets

def get_db_brokers(db: Session, broker_name: str) -> Optional[Broker]:
    """Return a row from the database that matches the broker name primary key."""
    return db.query(Broker).filter(Broker.name == broker_name).first()

def is_db_broker_exist(db: Session, broker_name: str) -> bool:
    """Return a boolean on whether a broker exists in the database."""
    return get_db_brokers(db, broker_name) is not None

def create_db_brokers(db: Session, broker_name: str):
    """Create a new broker in the database."""
    db_broker = Broker(name=broker_name)
    db.add(db_broker)
    db.commit()
    db.refresh(db_broker)
    return db_broker

def preload_db_brokers_table_from_csv(db: Session, filename: str = None):
    """Preload a pre-generated brokers csv file into the database."""
    if filename is None:
        filename = get_file_from_assets("supported_brokers.csv")

    if not os.path.isfile(filename):
        raise FileNotFoundError("Cannot find file for brokers table feeding:", filename)

    with open(filename, "r") as f:
        reader = csv.reader(f)

        next(reader) # Ignore Headers
        for row in reader:
            if not is_db_broker_exist(db, row[0]):
                create_db_brokers(db, row[0])
