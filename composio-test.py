from mira_sdk import MiraClient, Flow, ComposioConfig
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")
composio_api_key = os.getenv("COMPOSIO_API_KEY")
entity_id = os.getenv("ENTITY_ID")
enum="TWITTER_CREATION_OF_A_POST"


# Initialize Mira client with your API key
client = MiraClient(config={"API_KEY": api_key})

version = "1.0.0"
input_data = {
    "topic": "",
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@venkatesh-mira/perfect-tweet-generator/{version}"
else:
    flow_name = "@venkatesh-mira/perfect-tweet-generator"



# Execute flow with Composio integration
# The flow's output will automatically replace {content} in the TASK
response = client.flow.execute(
    flow_name,
    input_data,
    ComposioConfig(
        COMPOSIO_API_KEY=composio_api_key,
        ACTION=enum,  # This is the Enum e.g., "TWITTER_POST", "DISCORD_SEND"
        TASK="Post this tweet - {content}",  # {content} is required and gets replaced with flow output
        ENTITY_ID=entity_id  # Platform-specific identifier
    )
)

print("The tweet has been made successfully!")

