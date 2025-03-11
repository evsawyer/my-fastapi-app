from fastapi import FastAPI, HTTPException, Request
from starlette.responses import JSONResponse 
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

# Get the Slack bot token from environment variables
# SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Define the specific channel ID to respond to
TARGET_CHANNEL_ID = "C08GBSCSEG3"

# Initialize FastAPI app
app = FastAPI()

# Create POST endpoint to handle reaction events
@app.post("/slack/reaction")
async def handle_reaction(request: Request):
    try:
        payload = await request.json()
        event_type = payload.get("type")

        if event_type == "url_verification":
            return JSONResponse(content={"challenge": payload.get("challenge")})

        if "event" in payload:
            event = payload["event"]
            if event.get("type") == "message":
                return JSONResponse(content={"status": "message received"}, status_code=200)
                print("message received")
            if event.get("type") == "reaction_added":
                return JSONResponse(content={"status": "reaction added"}, status_code=200)
                print("reaction added")

        return JSONResponse(content={"status": "event ignored"}, status_code=200)

        # Parse the incoming request
        # body = await request.json()

        # # Check if it's a challenge request
        # if "challenge" in body:
        #     return {"challenge": body["challenge"]}
        

        # print(body["event"]["type"])
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