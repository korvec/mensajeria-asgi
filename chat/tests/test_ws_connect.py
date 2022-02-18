import pytest
import asyncio

from ws_connect import connection

def test_connection():
    response = asyncio.run(connection())
    assert response['message'] == 'ACK'
