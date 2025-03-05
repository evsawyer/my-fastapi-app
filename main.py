from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create Pydantic model for the incoming data
class ReactionEvent(BaseModel):
    type: str
    channel: str
    user: str
    text: str
    ts: str
    reactions: list

# Initialize FastAPI app
app = FastAPI()

# Create POST endpoint to handle reaction events
@app.post("/slack/reaction")
async def handle_reaction(event: ReactionEvent):
    try:
        # Extract reactions from the event
        reactions = event.reactions
        for reaction in reactions:
            print(f"Reaction: {reaction['name']}, Count: {reaction['count']}, Users: {reaction['users']}")
        
        return {
            "status": "success",
            "message": "Processed reactions",
            "data": event.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 