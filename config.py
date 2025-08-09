import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

class Config:
    DB_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'dev.db')}"
    DEBUG = True

class TestConfig(Config):
    DB_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'test.db')}"
    DEBUG = False

class ProdConfig(Config):
    DB_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'prod.db')}"
    DEBUG = False
