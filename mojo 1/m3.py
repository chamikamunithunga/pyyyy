# Example of asynchronous function
async def fetch_data() -> str:
    # Simulate an async task
    await asyncio.sleep(1)
    return "Data fetched"

# Call the async function
data = await fetch_data()
print(data)
