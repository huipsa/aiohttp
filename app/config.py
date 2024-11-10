import os


class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/ads')
    PORT = int(os.getenv('PORT', 5000))
