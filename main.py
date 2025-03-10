from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import os

# Get the Slack bot token from environment variables
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Define the specific channel ID to respond to
TARGET_CHANNEL_ID = "C08GBSCSEG3"

# Define a Pydantic model for the Slack event
class SlackEvent(BaseModel):
    type: str
    user: str
    reaction: str
    item: dict
    item_user: str
    event_ts: str

# Initialize FastAPI app
app = FastAPI()

# Create POST endpoint to handle reaction events
@app.post("/slack/reaction")
async def handle_reaction(request: Request):
    try:
        # Parse the incoming request
        body = await request.json()

        # Check if it's a challenge request
        if "challenge" in body:
            return {"challenge": body["challenge"]}
        

        print(body["event"]["type"])
        # return(body["event"]["type"])

        # Extract the event data
        # event_data = body.get("event", {})

        # Create an instance of the SlackEvent model
        # slack_event = SlackEvent(**event_data)
        # print(slack_event)

        # # Check if the event is from the target channel
        # if slack_event.channel != TARGET_CHANNEL_ID:
        #     return {
        #         "status": "ignored",
        #         "message": "Event from non-target channel",
        #         "data": slack_event.dict()
        #     }

        # # Process reactions if from the target channel
        # reactions = slack_event.reactions
        # for reaction in reactions:
        #     print(f"Reaction: {reaction['name']}, Count: {reaction['count']}, Users: {reaction['users']}")

        # return {
        #     "status": "success",
        #     "message": "Processed reactions",
        #     "data": slack_event.dict()
        # }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 