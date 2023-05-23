# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import json
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import requests
from rasa.shared.utils.io import json_to_string
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, Restarted, AllSlotsReset, UserUttered, LoopInterrupted, ActionExecuted, \
    Form, ActiveLoop
from rasa_sdk.executor import CollectingDispatcher
from twilio.rest import Client
from rasa.core.agent import Agent
import asyncio

class Sentence:
    sentence = ""
class Times:
    time = 4
class Model:

    def __init__(self, model_path: str) -> None:
        self.agent = Agent.load(model_path)
        print("NLU model loaded")


    async def message(self, message: str) -> Dict[str, str]:
              message = message.strip()
              result = await self.agent.parse_message(message)
              return {"name": result.get("intent").get("name")}

class ValidateSymptomForm(Action):
    def name (self) -> Text:
        return "user_symptom_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List [EventType]:
        Sentence.sentence=""
        required_slots = ["symptoms"]
        i = 1
        while i <= 3:
            i += 1
            SlotSet("requested_slot", required_slots)
            return [SlotSet("requested_slot", required_slots)]
    # All slots are filled.
        # for deactivate the loop : LoopInterrupted()
        return [SlotSet("requested_slot", None)]
class IntentTrigger(Action):
    def name(self) -> Text:
        return "action_3symptoms_intent"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        delimiter = ' '
        symptoms = [entity['value'] for entity in tracker.latest_message['entities']]
        symptoms2 = delimiter.join(symptoms)
        print(symptoms2)
        mdl = Model("./models/")
        #sentence = "fatigue bruising cramps obesity swollen_legs swollen_blood_vessels prominent_veins_on_calf"
        #sentence = "i have head painless lump and Pain while eating and Itching soreness, redness or rash"

        async def process_message() -> str:
            result = await mdl.message(symptoms2)
            print(result['name'])
            predicted_intent = result['name']
            #print(predicted_intent)
            return predicted_intent
            #if predicted_intent == "fungal_infection":
                #dispatcher.utter_message(response="utter_fungal_infection")


            # Retrieve the appropriate utterance based on the predicted intent
#            utterance = domain['responses'][predicted_intent][0]['text']
#            print(utterance)
#            dispatcher.utter_message(utterance)
#            return result


        results = await asyncio.create_task(process_message())
        print(results)
        if results == "fungal_infection":
            dispatcher.utter_message(response="utter_fungal_infection")
        elif results == "allergy":
            dispatcher.utter_message(response="utter_allergy")
        elif results == "gerd":
            dispatcher.utter_message(response="utter_gerd")
        elif results == "chronic_cholestasis":
            dispatcher.utter_message(response="utter_chronic_cholestasis")
        elif results == "drug_reaction":
            dispatcher.utter_message(response="utter_drug_reaction")
        elif results == "peptic_ulcer_diseae":
            dispatcher.utter_message(response="utter_peptic_ulcer_diseae")
        elif results == "aids":
            dispatcher.utter_message(response="utter_aids")
        elif results == "diabetes":
            dispatcher.utter_message(response="utter_diabetes")
        elif results == "gastroenteritis":
            dispatcher.utter_message(response="utter_gastroenteritis")
        elif results == "bronchial_asthma":
            dispatcher.utter_message(response="utter_bronchial_asthma")
        elif results == "hypertension":
            dispatcher.utter_message(response="utter_hypertension")
        elif results == "migraine":
            dispatcher.utter_message(response="utter_migraine")
        elif results == "cervical_spondylosis":
            dispatcher.utter_message(response="utter_cervical_spondylosis")
        elif results == "paralysis_(brain_hemorrhage)":
            dispatcher.utter_message(response="utter_paralysis_(brain_hemorrhage)")
        elif results == "jaundice":
            dispatcher.utter_message(response="utter_jaundice")
        elif results == "malaria":
            dispatcher.utter_message(response="utter_malaria")
        elif results == "chicken_pox":
            dispatcher.utter_message(response="utter_chicken_pox")
        elif results == "dengue":
            dispatcher.utter_message(response="utter_dengue")
        elif results == "typhoid":
            dispatcher.utter_message(response="utter_typhoid")
        elif results == "hepatitis_a":
            dispatcher.utter_message(response="utter_hepatitis_a")
        elif results == "hepatitis_b":
            dispatcher.utter_message(response="utter_hepatitis_b")
        elif results == "hepatitis_c":
            dispatcher.utter_message(response="utter_hepatitis_c")
        elif results == "hepatitis_d":
            dispatcher.utter_message(response="utter_hepatitis_d")
        elif results == "hepatitis_e":
            dispatcher.utter_message(response="utter_hepatitis_e")
        elif results == "alcoholic_hepatitis":
            dispatcher.utter_message(response="utter_alcoholic_hepatitis")
        elif results == "tuberculosis":
            dispatcher.utter_message(response="utter_tuberculosis")
        elif results == "common_cold":
            dispatcher.utter_message(response="utter_common_cold")
        elif results == "pneumonia":
            dispatcher.utter_message(response="utter_pneumonia")
        elif results == "dimorphic_hemmorhoids(piles)":
            dispatcher.utter_message(response="utter_dimorphic_hemmorhoids(piles)")
        elif results == "heart_attack":
            dispatcher.utter_message(response="utter_heart_attack")
        elif results == "varicose_veins":
            dispatcher.utter_message(response="utter_varicose_veins")
        elif results == "hypothyroidism":
            dispatcher.utter_message(response="utter_hypothyroidism")
        elif results == "hyperthyroidism":
            dispatcher.utter_message(response="utter_hyperthyroidism")
        elif results == "hypoglycemia":
            dispatcher.utter_message(response="utter_hypoglycemia")
        elif results == "osteoarthristis":
            dispatcher.utter_message(response="utter_osteoarthristis")
        elif results == "arthritis":
            dispatcher.utter_message(response="utter_arthritis")
        elif results == "(vertigo)_paroymsal_positional_vertigo":
            dispatcher.utter_message(response="utter_(vertigo)_paroymsal_positional_vertigo")
        elif results == "acne":
            dispatcher.utter_message(response="utter_acne")
        elif results == "urinary_tract_infection":
            dispatcher.utter_message(response="utter_urinary_tract_infection")
        elif results == "psoriasis":
            dispatcher.utter_message(response="utter_psoriasis")
        elif results == "impetigo":
            dispatcher.utter_message(response="utter_impetigo")
        elif results == "nlu_fallback":
            dispatcher.utter_message(text="Your symptoms are so variates, please go to a generalist doctor for a diagnostic clinic")
        elif results == "goodbye":
            dispatcher.utter_message(text="Your symptoms are so variates, please go to a generalist doctor for a diagnostic clinic")
        else:
            dispatcher.utter_message(text="Your symptoms are so variates, please go to a generalist doctor for a diagnostic clinic")

        return []
#        print(results)
#        print(results["name"])
#        #intente = results["name"]
#        message = UserUttered(sentence , results)
#        print(message)
#        return [message]


class ValidateForm(Action):
    def name (self) -> Text:
        return "user_details_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List [EventType]:
        required_slots = ["name", "phone_number"]
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
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

        ## messag to doctor
        message = client.messages.create(
            from_='+16075233346',
            body="Patient "+ tracker.get_slot("name") +" with the Mobile number "+ tracker.get_slot("phone_number") +" want an appointment",
            to='+213777038502')
        #.utter_message(text="message of reserving an appointment has been sent seccessefully to {}".string.format(tracker.get_slot("phone_number")))

        ### mssage to patient
        #message2 = client.messages.create(
         #   from_='+16075233346',
          #  body="your request for an appointment was sent seccessfully to the number +213777038502, if u didn't get a response please call in the mentioned number",
           # to=tracker.get_slot("phone_number"))

        return []
class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []

class ActionRestarted(Action):
    def name(self) -> Text:
        return "action_restart"
    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class ActionSlotsReset(Action):
    def name(self) -> Text:
        return "action_slots_reset"
    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]

class ActionLoopReset(Action):
    def name(self) -> Text:
        return "action_loop_reset"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[None]:
        # for deactivate the loop we use: LoopInterrupted()
        return [tracker.active_loop.clear()]

class ActionDoNothing(Action):
    def name(self) -> Text:
        return "action_do_nothing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:
        #print(tracker.active_loop.get('name'))
        if Times.time > 0 and "user_symptoms_form" == tracker.active_loop.get('name'):
            Times.time = Times.time - 1
            #print(tracker.active_loop.get('name'))
            pass       # Empty implementation
        elif "user_symptoms_form" == tracker.active_loop.get('name') and Times.time <= 0:
            dispatcher.utter_message(text="Your symptoms are very diverse, please go to a general doctor for a comprehensive diagnostic examination!!")
            Times.time = 4
            return [SlotSet("requested_slot", None) and ActiveLoop(None)]
        else:
            #print(tracker.active_loop.get('name'))
            return [SlotSet("requested_slot", None) and ActiveLoop(None)]


