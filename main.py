from fastapi import FastAPI, HTTPException
import redis

# Initialize FastAPI app
app = FastAPI()

# Connect to Redis
r = redis.Redis(
    host='redis-10436.c245.us-east-1-3.ec2.redns.redis-cloud.com',
    port=10436,
    password='hho6RFGFBC9vJn4qxM0MEPBjwO9DG6jd'
)

@app.get("/get-address/")
def get_address(latitude: float, longitude: float):
    key = f'location:{latitude}:{longitude}'
    stored_record = r.hgetall(key)
    if stored_record:
        decoded_record = {k.decode('utf-8'): v.decode('utf-8') for k, v in stored_record.items()}
        address = decoded_record.get('address', 'Address not found')
        return {"address": address}
    else:
        raise HTTPException(status_code=404, detail="Record not found")

