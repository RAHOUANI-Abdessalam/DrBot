# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
import json
import random
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
import webbrowser
import urllib.parse

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

class Mymodel:
    mdl = Model("./models/")
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
    ) -> List[EventType]:
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

        return [SlotSet("requested_slot", None) and ActiveLoop(None) and print("slot submited resets")]
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
    def __init__(self):
        # This will be called when the action server is started
        Mymodel.mdl = Model("./models/")
    def name(self) -> Text:
        return "action_do_nothing"


    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[EventType]:
        #print(tracker.active_loop.get('name'))
        if Times.time > 0 and "user_symptoms_form" == tracker.active_loop.get('name'):
            Sentence.sentence = Sentence.sentence + tracker.latest_message.get('text') + " "
            print("new text: "+Sentence.sentence)

            async def process_message() -> str:
                result = await Mymodel.mdl.message(Sentence.sentence)
                #print(result['name']+'1')
                predicted_intent = result['name']
                # print(predicted_intent)
                return predicted_intent

            results = await asyncio.create_task(process_message())
            #UserUttered(text=Sentence.sentence)
            print('intent: '+results)
            if results == "fungal_infection":
                dispatcher.utter_message(response="utter_fungal_infection")
                Sentence.sentence=""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "allergy":
                dispatcher.utter_message(response="utter_allergy")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "gerd":
                dispatcher.utter_message(response="utter_gerd")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "chronic_cholestasis":
                dispatcher.utter_message(response="utter_chronic_cholestasis")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "drug_reaction":
                dispatcher.utter_message(response="utter_drug_reaction")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "peptic_ulcer_diseae":
                dispatcher.utter_message(response="utter_peptic_ulcer_diseae")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "aids":
                dispatcher.utter_message(response="utter_aids")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "diabetes":
                dispatcher.utter_message(response="utter_diabetes")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "gastroenteritis":
                dispatcher.utter_message(response="utter_gastroenteritis")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "bronchial_asthma":
                dispatcher.utter_message(response="utter_bronchial_asthma")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hypertension":
                dispatcher.utter_message(response="utter_hypertension")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "migraine":
                dispatcher.utter_message(response="utter_migraine")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "cervical_spondylosis":
                dispatcher.utter_message(response="utter_cervical_spondylosis")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "paralysis_(brain_hemorrhage)":
                dispatcher.utter_message(response="utter_paralysis_(brain_hemorrhage)")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "jaundice":
                dispatcher.utter_message(response="utter_jaundice")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "malaria":
                dispatcher.utter_message(response="utter_malaria")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "chicken_pox":
                dispatcher.utter_message(response="utter_chicken_pox")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "dengue":
                dispatcher.utter_message(response="utter_dengue")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "typhoid":
                dispatcher.utter_message(response="utter_typhoid")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hepatitis_a":
                dispatcher.utter_message(response="utter_hepatitis_a")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hepatitis_b":
                dispatcher.utter_message(response="utter_hepatitis_b")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hepatitis_c":
                dispatcher.utter_message(response="utter_hepatitis_c")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hepatitis_d":
                dispatcher.utter_message(response="utter_hepatitis_d")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hepatitis_e":
                dispatcher.utter_message(response="utter_hepatitis_e")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "alcoholic_hepatitis":
                dispatcher.utter_message(response="utter_alcoholic_hepatitis")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "tuberculosis":
                dispatcher.utter_message(response="utter_tuberculosis")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "common_cold":
                dispatcher.utter_message(response="utter_common_cold")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "pneumonia":
                dispatcher.utter_message(response="utter_pneumonia")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "dimorphic_hemmorhoids(piles)":
                dispatcher.utter_message(response="utter_dimorphic_hemmorhoids(piles)")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "heart_attack":
                dispatcher.utter_message(response="utter_heart_attack")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "varicose_veins":
                dispatcher.utter_message(response="utter_varicose_veins")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hypothyroidism":
                dispatcher.utter_message(response="utter_hypothyroidism")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hyperthyroidism":
                dispatcher.utter_message(response="utter_hyperthyroidism")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "hypoglycemia":
                dispatcher.utter_message(response="utter_hypoglycemia")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "osteoarthristis":
                dispatcher.utter_message(response="utter_osteoarthristis")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "arthritis":
                dispatcher.utter_message(response="utter_arthritis")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "(vertigo)_paroymsal_positional_vertigo":
                dispatcher.utter_message(response="utter_(vertigo)_paroymsal_positional_vertigo")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "acne":
                dispatcher.utter_message(response="utter_acne")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "urinary_tract_infection":
                dispatcher.utter_message(response="utter_urinary_tract_infection")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "psoriasis":
                dispatcher.utter_message(response="utter_psoriasis")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            elif results == "impetigo":
                dispatcher.utter_message(response="utter_impetigo")
                Sentence.sentence = ""
                return [SlotSet("requested_slot", None) and ActiveLoop(None)]
            Times.time = Times.time - 1
            return [SlotSet("requested_slot", "symptoms")]
            #print(tracker.active_loop.get('name'))
            #pass       # Empty implementation
        elif "user_symptoms_form" == tracker.active_loop.get('name') and Times.time <= 0:
            dispatcher.utter_message(text="Your symptoms are very diverse, please go to a general doctor for a comprehensive diagnostic examination!!")
            Times.time = 4
            Sentence.sentence = ""
            return [SlotSet("requested_slot", None) and ActiveLoop(None)]
        else:
            #print(tracker.active_loop.get('name'))
            outOfScope1="I'm sorry, I didn't quite understand what you're asking. Could you please rephrase your question?"
            outOfScope2="I'm sorry, but that is beyond the scope of my expertise. Can you please provide me with more details on what you need help with?"
            outOfScope3="I'm sorry, I don't have the knowledge to provide you with the information you're requesting. Can I help you with anything else?"
            outOfScope4="I'm sorry, I'm not programmed to answer that question. Can I help you with something else?"
            listOutOfScope=[outOfScope1,outOfScope2,outOfScope3,outOfScope4]
            dispatcher.utter_message(text=random.choice(listOutOfScope))
            return [SlotSet("requested_slot", None) and ActiveLoop(None)]

##### check nearst dr actions
class ActionCheckNearstDr(Action):
    def name(self) -> Text:
        return "action_nearst_dermatologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'dermatologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []

class ActionCheckNearstDr2(Action):
    def name(self) -> Text:
        return "action_nearst_medecin_generaliste"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'medecin generaliste'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []

class ActionCheckNearstDr3(Action):
    def name(self) -> Text:
        return "action_nearst_allergologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'allergologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr4(Action):
    def name(self) -> Text:
        return "action_nearst_immunologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'immunologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr5(Action):
    def name(self) -> Text:
        return "action_nearst_gastro_enterologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'gastro enterologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr6(Action):
    def name(self) -> Text:
        return "action_nearst_hepatologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'hepatologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr7(Action):
    def name(self) -> Text:
        return "action_nearst_infectiologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'infectiologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr8(Action):
    def name(self) -> Text:
        return "action_nearst_pneumologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'pneumologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr9(Action):
    def name(self) -> Text:
        return "action_nearst_cardiologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'cardiologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr10(Action):
    def name(self) -> Text:
        return "action_nearst_neurologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'neurologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr11(Action):
    def name(self) -> Text:
        return "action_nearst_orthopediste"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'orthopediste'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr12(Action):
    def name(self) -> Text:
        return "action_nearst_proctologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'proctologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr13(Action):
    def name(self) -> Text:
        return "action_nearst_chirurgien_generaliste"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'chirurgien generaliste'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr14(Action):
    def name(self) -> Text:
        return "action_nearst_chirurgien_vasculaire"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'chirurgien vasculaire'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []
class ActionCheckNearstDr15(Action):
    def name(self) -> Text:
        return "action_nearst_endocrinologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'endocrinologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []

class ActionCheckNearstDr16(Action):
    def name(self) -> Text:
        return "action_nearst_rhumatologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'rhumatologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []

class ActionCheckNearstDr17(Action):
    def name(self) -> Text:
        return "action_nearst_orl_specialist"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'orl specialist'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []

class ActionCheckNearstDr18(Action):
    def name(self) -> Text:
        return "action_nearst_urologue"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        base_url = 'https://www.google.com/maps/search/'
        specialist = 'urologue'
        query = urllib.parse.quote(f'nearest {specialist}')
        search_url = base_url + query
        webbrowser.open(search_url)
        return []



