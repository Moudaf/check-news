# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

# import pandas as pd
# from rasa.shared.core.trackers import DialogueTracker

from rasa.shared.core.events import ActionExecuted, UserUttered
# from rasa.shared.core.trackers import DialogueTracker

from typing import Any, Text, Dict, List
import os
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionVerificationInfo1(Action):

    def name(self) -> Text:
        return "action_verification_info_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_1": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_1": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_1": "pas"}',"title": "Je ne comprends pas", },
        ]
        dispatcher.utter_message(text="Cet information parle d'un organisme ?",buttons=buttons)

        return [] 

class ActionVerificationInfo2(Action):

    def name(self) -> Text:
        return "action_verification_info_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="Connaissez-vous cet organisme ?",
            buttons=[
                    {"payload": '/affirmatif{"info_2": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_2": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_2": "pas"}',"title": "Je ne comprends pas", },
            ],
        )

        return [] 
    
class ActionVerificationInfo3(Action):

    def name(self) -> Text:
        return "action_verification_info_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_3": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_3": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_3": "pas"}',"title": "Je ne comprends pas", },
        ]
        dispatcher.utter_message(text="Cet organisme à t-il un site web officiel? ",buttons=buttons)

        return [] 

class ActionVerificationInfo4(Action):

    def name(self) -> Text:
        return "action_verification_info_4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="Cet info c'est trouve t-elle dans ce site? ",
            buttons=[
                    {"payload": '/affirmatif{"info_4": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_4": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_4": "pas"}',"title": "Je ne comprends pas", },
            ],
        )

        return [] 
    
class ActionVerificationInfo5(Action):

    def name(self) -> Text:
        return "action_verification_info_5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_5": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_5": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_5": "pas"}',"title": "Je ne comprends pas", },
        ]
        dispatcher.utter_message(text="Cette Info contient-elle une adresse URL ?",buttons=buttons)

        return [] 

class ActionVerificationInfo6(Action):

    def name(self) -> Text:
        return "action_verification_info_6"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="Faites des recherche sur cette adresse",
            buttons=[
                    {"payload": '/affirmatif{"info_6": "oui"}',"title": "OK", },
            ],
        )

        return [] 
    
class ActionVerificationInfo7(Action):

    def name(self) -> Text:
        return "action_verification_info_7"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_7": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_7": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_7": "pas"}',"title": "Je ne comprends pas", },
        ]
        dispatcher.utter_message(text="L'origine de l'information est t'elle mentionnée? ",buttons=buttons)

        return [] 

class ActionVerificationInfo8(Action):

    def name(self) -> Text:
        return "action_verification_info_8"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="Cet origine dit la même chose? ",
            buttons=[
                    {"payload": '/affirmatif{"info_8": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_8": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_8": "pas"}',"title": "Je ne comprends pas", },
            ],
        )

        return [] 
    
class ActionVerificationInfo9(Action):

    def name(self) -> Text:
        return "action_verification_info_9"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_9": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_9": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_9": "pas"}',"title": "Je ne comprends pas", },
        ]
        dispatcher.utter_message(text="Comprennez-vous ce qu'ils disent dans l'info? ",buttons=buttons)

        return [] 

class ActionVerificationInfo10(Action):

    def name(self) -> Text:
        return "action_verification_info_10"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="At-il laisser quelques chose pour vous faire croire à cette info? ",
            buttons=[
                    {"payload": '/affirmatif{"info_10": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_10": "non"}',"title": "Non", },
                    {"payload": '/comprends_pas{"info_1O": "pas"}',"title": "Je ne comprends pas", },
            ],
        )

        return [] 
    
class ActionVerificationInfo11(Action):

    def name(self) -> Text:
        return "action_verification_info_11"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_11": "oui"}',"title": "OK", },
        ]
        dispatcher.utter_message(text=" Faites des recherche sur cet organisme",buttons=buttons)

        return [] 


                                    
                                    ############### debut action je ne comprends pas #############
class ActionVerificationPas1(Action):

    def name(self) -> Text:
        return "action_verification_pas_1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_1": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_1": "non"}',"title": "Non", },
        ]
        dispatcher.utter_message(text="Cette information parle d'une entreprise ?",buttons=buttons)

        return [] 

class ActionVerificationPas2(Action):

    def name(self) -> Text:
        return "action_verification_pas_2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="Connaissez-vous cette entreprise ?",
            buttons=[
                    {"payload": '/affirmatif{"info_2": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_2": "non"}',"title": "Non", },
            ],
        )

        return [] 
    
class ActionVerificationPas3(Action):

    def name(self) -> Text:
        return "action_verification_pas_3"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_3": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_3": "non"}',"title": "Non", },
        ]
        dispatcher.utter_message(text="Cette entreprise à t-elle un site web officiel? ",buttons=buttons)

        return [] 

class ActionVerificationPas4(Action):

    def name(self) -> Text:
        return "action_verification_pas_4"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="Cette info est dans ce site? ",
            buttons=[
                    {"payload": '/affirmatif{"info_4": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_4": "non"}',"title": "Non", },
            ],
        )

        return [] 
    
class ActionVerificationPas5(Action):

    def name(self) -> Text:
        return "action_verification_pas_5"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_5": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_5": "non"}',"title": "Non", },
        ]
        dispatcher.utter_message(text="Cette Info contient-elle des symbole présenter sous cette forme **www.exemple.xyz/blabla** ?",buttons=buttons)

        return [] 

# class ActionVerificationInfo6(Action):

#     def name(self) -> Text:
#         return "action_verification_info_6"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
#         dispatcher.utter_message(
#             text="Faites des recherche sur cette adresse",
#             buttons=[
#                     {"payload": '/affirmatif{"info_6": "oui"}',"title": "OK", },
#             ],
#         )

#         return [] 
    
class ActionVerificationPas7(Action):

    def name(self) -> Text:
        return "action_verification_pas_7"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_7": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_7": "non"}',"title": "Non", },
        ]
        dispatcher.utter_message(text="l'auteur a mentionner les sources de cette info? ",buttons=buttons)

        return [] 

class ActionVerificationPas8(Action):

    def name(self) -> Text:
        return "action_verification_pas_8"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="Ces sources disent la même chose? ",
            buttons=[
                    {"payload": '/affirmatif{"info_8": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_8": "non"}',"title": "Non", },
            ],
        )

        return [] 
    
class ActionVerificationPas9(Action):

    def name(self) -> Text:
        return "action_verification_pas_9"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        buttons=[
                    {"payload": '/affirmatif{"info_9": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_9": "non"}',"title": "Non", },
        ]
        dispatcher.utter_message(text="Ce qu'ils disent dans l'info a un sens? ",buttons=buttons)

        return [] 

class ActionVerificationPas10(Action):

    def name(self) -> Text:
        return "action_verification_pas_10"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        dispatcher.utter_message(
            text="Il vous force à croire à ce qu'il dit dans cette info? ",
            buttons=[
                    {"payload": '/affirmatif{"info_10": "oui"}',"title": "Oui", },
                    {"payload": '/negatif{"info_10": "non"}',"title": "Non", },
            ],
        )

        return [] 
    
# class ActionVerificationInfo11(Action):

#     def name(self) -> Text:
#         return "action_verification_info_11"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         buttons=[
#                     {"payload": '/affirmatif{"info_11": "oui"}',"title": "OK", },
#         ]
#         dispatcher.utter_message(text=" Faites des recherche sur cet organisme",buttons=buttons)

#         return [] 


                                    ############### fin action je ne comprends pas#############
                                    

# class ActionSaveConversation(Action):

#     def name(self) -> Text:
#         return "action_save_conversation"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         conversation = tracker.events

#         # Assurez-vous que le fichier 'chats.txt' existe
#         if not os.path.isfile('chats.txt'):
#             with open('chats.txt', 'w') as file:
#                 file.write("New Client\n")

#         chat_data = ''

#         for event in conversation:
#             if event["event"] == "user":
#                 chat_data += 'User: ' + event['text'] + '\n'
#             elif event['event'] == 'bot':
#                 try:
#                     chat_data += 'Bot: ' + event['text'] + '\n'
#                 except KeyError:
#                     pass

#         with open('chats.txt', 'a', encoding="utf-8") as file:
#             file.write(chat_data)

# #         return []


# class SaveConversationAction(Action):

#     def name(self) -> Text:
#         return "action_save_conversation"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: DialogueTracker,
#             domain: Dict[Text, Any]) -> None:

#         # Obtenir les informations de la conversation
#         conversation_id = tracker.sender_id
#         user_uttered = tracker.latest_message.data["text"]
#         bot_uttered = tracker.active_loop_name

#         # Créer un nouveau DataFrame
#         conversation_df = pd.DataFrame({
#             "conversation_id": [conversation_id],
#             "user_uttered": [user_uttered],
#             "bot_uttered": [bot_uttered]
#         })

#         # Enregistrer le DataFrame dans un fichier Excel
#         conversation_df.to_excel("conversations.xlsx", index=False)

#         # Envoyer un message de confirmation à l'utilisateur
#         dispatcher.utter_message("La conversation a été sauvegardée avec succès.")



# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []