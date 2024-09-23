import asyncio


async def test_nothing():
    await asyncio.sleep(0.01)
    assert True, "Please add a real test"
