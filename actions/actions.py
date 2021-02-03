from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk.forms import Action, FormAction
import mysql.connector
import traceback
import requests
import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, UserUtteranceReverted, Restarted
from rasa_sdk.executor import CollectingDispatcher
from DB import DataUpdate

class ValidateForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["firstname", "lastname","feedback"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action): 
    def name(self) -> Text: 
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]: 
        # update to Database 
        DataUpdate(tracker.get_slot("firstname"),tracker.get_slot("lastname"),tracker.get_slot("feedback")) 
        # bot reply to user with data collected.
        dispatcher.utter_message(template="utter_details_thanks")
        return []

class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Hey there I am your assistant, how may I help you today")

        return [UserUtteranceReverted()] 

class ActionRestart(Action):

  def name(self) -> Text:
      return "action_restart"

  async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:

      # custom behavior

      return [Restarted()]