import pytest
import asyncio

from websocket import connection

def test_connection():
    response = asyncio.run(connection())
    assert response['message'] == 'ACK'
