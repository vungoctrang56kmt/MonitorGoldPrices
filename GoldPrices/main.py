from fastapi import FastAPI, HTTPException
import httpx
import asyncio

app = FastAPI()

GOLD_API_URL = "https://www.goldapi.io/api/XAU/USD"
API_KEY = "goldapi-h8ho519lwhhvk0y-io"
UPDATE_INTERVAL = 60  # Thời gian cập nhật (giây)

gold_price = None

async def fetch_gold_price():
    global gold_price
    headers = {"x-access-token": API_KEY}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(GOLD_API_URL, headers=headers)
            if response.status_code == 200:
                gold_price = response.json()
            else:
                print(f"Failed to fetch data from Gold API: {response.status_code}")
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from Gold API")
    except httpx.RequestError as e:
        print(f"Request error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")

async def update_gold_price_periodically():
    while True:
        try:
            await fetch_gold_price()
        except Exception as e:
            print(f"Error while updating gold price: {e}")
        await asyncio.sleep(UPDATE_INTERVAL)

@app.get("/gold_price")
async def get_gold_price():
    if gold_price is None:
        await fetch_gold_price()
    return gold_price


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(update_gold_price_periodically())
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8242)
