from typing import Any


from constants import Environment
from dotenv import load_dotenv

load_dotenv()
import os

class Config(object):
    
    
    ENVIRONMENT = os.getenv("ENVIRONMENT", Environment.PRODUCTION)

    SENDER_EMAILL = os.getenv("SENDER_EMAILL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = os.getenv("SMTP_PORT")
    
    TO_EMAIL = os.getenv("TO_EMAIL")
    


