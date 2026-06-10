# ---------------------------------------------------------
# Custom Actions File for Rasa
# ---------------------------------------------------------
# This file is used when you want Python-based dynamic replies.
# Example: checking order status from a database or API.
# In this beginner project, most replies are fixed in domain.yml.
# ---------------------------------------------------------

from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from typing import Any, Text, Dict, List


class ActionCheckOrderStatus(Action):
    """
    Sample custom action for checking order status.
    This is optional for beginners.
    """

    def name(self) -> Text:
        # This name is used inside domain.yml and stories/rules.
        return "action_check_order_status"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Send message back to the user.
        dispatcher.utter_message(text="Your order is being processed.")

        # Return empty list because we are not changing slots/events.
        return []
