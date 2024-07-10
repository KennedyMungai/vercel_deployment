"""The main file for running the application"""
from fastapi import FastAPI

app = FastAPI(title='Vercel FastAPI', version='0.1.0')

@app.get('/')
async def root():
    """The root endpoint for the API

    Returns:
        dict: A dict containing the message
    """
    return {'message': 'Hello World'}
