import streamlit as st
import google.generativeai as genai
import os

# --- Configuration ---
# To run this app, set your GOOGLE_API_KEY environment variable.
# Example: export GOOGLE_API_KEY="your_api_key"
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except (AttributeError, KeyError):
    st.error("Please set the GOOGLE_API_KEY environment variable.")
    st.stop()


# --- Gemini Function Declarations ---

get_performance_func = {
    "name": "get_campaign_performance",
    "description": "Get key performance metrics for a specified Google Ads campaign.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "campaign_name": {
                "type": "STRING",
                "description": "The name of the campaign to analyze."
            }
        },
        "required": ["campaign_name"]
    }
}

pause_campaign_func = {
    "name": "pause_campaign",
    "description": "Pause a currently active Google Ads campaign.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "campaign_name": {
                "type": "STRING",
                "description": "The name of the campaign to pause."
            }
        },
        "required": ["campaign_name"]
    }
}

enable_campaign_func = {
    "name": "enable_campaign",
    "description": "Enable a paused Google Ads campaign.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "campaign_name": {
                "type": "STRING",
                "description": "The name of the campaign to enable."
            }
        },
        "required": ["campaign_name"]
    }
}

change_budget_func = {
    "name": "change_budget",
    "description": "Change the daily budget for a specified Google Ads campaign.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "campaign_name": {
                "type": "STRING",
                "description": "The name of the campaign to modify."
            },
            "budget_amount": {
                "type": "NUMBER",
                "description": "The new daily budget amount in the local currency."
            }
        },
        "required": ["campaign_name", "budget_amount"]
    }
}


# --- Chatbot Business Logic ---

class RealEstateChatbot:
    """
    A chatbot that uses the Gemini API with function calling to manage
    simulated Google Ads campaigns for a real estate business.
    """
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-pro',
            tools=[get_performance_func, pause_campaign_func, enable_campaign_func, change_budget_func]
        )
        self.tools = {
            "get_campaign_performance": self.get_campaign_performance,
            "pause_campaign": self.pause_campaign,
            "enable_campaign": self.enable_campaign,
            "change_budget": self.change_budget,
        }

    def get_campaign_performance(self, campaign_name: str):
        """Placeholder for API call to get campaign performance."""
        # In a real application, this would query the Google Ads API.
        if "non_existent" in campaign_name.lower():
            return f"Error: Campaign '{campaign_name}' not found."
        return {
            "campaign": campaign_name,
            "clicks": "1,204",
            "impressions": "34,567",
            "ctr": "3.48%",
            "cost": "$2,450.78"
        }

    def pause_campaign(self, campaign_name: str):
        """Placeholder for API call to pause a campaign."""
        return f"Successfully paused campaign: '{campaign_name}'."

    def enable_campaign(self, campaign_name: str):
        """Placeholder for API call to enable a campaign."""
        return f"Successfully enabled campaign: '{campaign_name}'."

    def change_budget(self, campaign_name: str, budget_amount: float):
        """Placeholder for API call to change a campaign's budget."""
        return f"Successfully changed budget for '{campaign_name}' to ${budget_amount:,.2f}."

    def process_message(self, user_message: str, chat_history):
        """
        Sends the user's message and chat history to the Gemini model,
        handles the response, and returns either a text response or a
        pending function call.
        """
        # The genai library expects a specific format for history.
        history_for_api = []
        for message in chat_history:
            role = 'user' if message['role'] == 'user' else 'model'
            history_for_api.append({'role': role, 'parts': [message['parts']]})

        try:
            # Exclude the user's latest message from history for the API call
            response = self.model.generate_content(
                user_message,
                generation_config=genai.types.GenerationConfig(candidate_count=1),
                history=history_for_api[:-1]
            )
            
            response_part = response.candidates[0].content.parts[0]

            if response_part.function_call:
                return {"type": "function_call", "data": response_part.function_call}
            else:
                return {"type": "text", "data": response.text}
        except Exception as e:
            print(f"An error occurred: {e}")
            return {"type": "text", "data": "Sorry, I encountered an error. Please try again."}

    def execute_function_call(self, function_call):
        """
        Executes a function call proposed by the model and returns the result.
        """
        func_name = function_call.name
        func_args = {key: value for key, value in function_call.args.items()}
        
        if func_name in self.tools:
            try:
                result = self.tools[func_name](**func_args)
                return result
            except Exception as e:
                return f"Error executing function {func_name}: {e}"
        else:
            return f"Error: Unknown function '{func_name}'."


# --- Streamlit UI ---

st.set_page_config(page_title="Real Estate Ads Chatbot", layout="wide")
st.title("🏡 Real Estate Ads Campaign Manager")
st.caption("I can help you manage your Google Ads campaigns. Try asking to pause a campaign or check its performance.")

# Initialize chatbot and session state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = RealEstateChatbot()
if "history" not in st.session_state:
    st.session_state.history = []
if "pending_action" not in st.session_state:
    st.session_state.pending_action = None

chatbot = st.session_state.chatbot

# Display chat history
for message in st.session_state.history:
    with st.chat_message(message["role"]):
        st.markdown(message["parts"])

# User input
if prompt := st.chat_input("What would you like to do?"):
    st.session_state.history.append({"role": "user", "parts": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        response = chatbot.process_message(prompt, st.session_state.history)

    if response["type"] == "text":
        st.session_state.history.append({"role": "model", "parts": response["data"]})
        with st.chat_message("model"):
            st.markdown(response["data"])
    elif response["type"] == "function_call":
        st.session_state.pending_action = response["data"]
        func_name = response["data"].name
        func_args = {key: value for key, value in response["data"].args.items()}
        
        # Format a user-friendly confirmation message
        args_str = ", ".join(f"'{v}'" for k, v in func_args.items())
        recommendation = f"I recommend using the `{func_name}` tool with the following parameters: {args_str}. Shall I proceed?"
        
        st.session_state.history.append({"role": "model", "parts": recommendation})
        with st.chat_message("model"):
            st.markdown(recommendation)


# Pending Action Panel
if st.session_state.pending_action:
    with st.status("🚨 Pending Action", expanded=True):
        func_call = st.session_state.pending_action
        func_name = func_call.name
        func_args = {key: value for key, value in func_call.args.items()}
        
        st.write(f"**Tool:** `{func_name}`")
        st.write("**Parameters:**")
        st.json(func_args)

        if st.button("✅ Execute Action"):
            with st.spinner("Executing..."):
                result = chatbot.execute_function_call(st.session_state.pending_action)
                
                result_message = f"Tool `{func_name}` executed. Result: {result}"
                st.session_state.history.append({"role": "model", "parts": result_message})
                
                st.session_state.pending_action = None
                st.rerun()
