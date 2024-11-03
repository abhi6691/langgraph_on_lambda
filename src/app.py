from datetime import datetime
import time
from langgraph.graph import END, StateGraph, START, MessagesState
from langchain_openai import ChatOpenAI
import os

from aws_lambda_powertools import Logger

logger = Logger(service="app")

def create_graph():
    # logger.info("Creating graph!!!")
    graph = StateGraph(MessagesState)

    def greeting_node(state: MessagesState):
        msg = state["messages"]
        return {"messages": f"Received message: {msg}"}
    
    def current_time_node(state: MessagesState):
        # Get the current time in the user's timezone
        user_time = datetime.now()
        time.sleep(5)
        # Determine the greeting based on the hour
        hour = user_time.hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        # Format the current time as a string
        current_time = user_time.strftime("%I:%M %p")
        message = f"{greeting}! The current time is {current_time})."
        return {"messages": message} 
    
    graph.add_node("greeting", greeting_node)
    graph.add_node("current_time", current_time_node)

    graph.add_edge(START, "greeting")   
    graph.add_edge("greeting", "current_time")
    graph.add_edge("current_time", END)
    
    return graph