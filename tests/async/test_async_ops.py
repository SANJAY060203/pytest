import pytest
from src.async_ops import fetch_data

@pytest.mark.asyncio
async def test_fetch_data():
    assert await fetch_data() == "done"
