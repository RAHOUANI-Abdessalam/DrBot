# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet,EventType
from rasa_sdk.executor import CollectingDispatcher
from twilio.rest import Client

class ValidateForm(Action):
    def name (self) -> Text:
        return "user_details_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List [EventType]:
        required_slots = ["name", "phone_number"]
        for slot_name in required_slots:
            if tracker.slots.get (slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet ("requested_slot", slot_name)]
    # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Mobile_number=tracker.get_slot("phone_number"))
        ##test sending message ////////////////////////////////////////////////////
        account_sid = 'ACd275031e6553d3cd9e344d56eec57a09'
        auth_token = 'cbf52f9db5b2d83219e74f98cde197e1'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+16075233346',
            body="Patient "+ tracker.get_slot("name") +" want an appointment",
            to=tracker.get_slot("phone_number"))
        #.utter_message(text="message of reserving an appointment has been sent seccessefully to {}".string.format(tracker.get_slot("phone_number")))

        return []
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []
