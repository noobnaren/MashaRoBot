import html
import random
import MashaRoBot.modules.truth_and_dare_string as truth_and_dare_string
from MashaRoBot import dispatcher
from telegram import ParseMode, Update, Bot
from MashaRoBot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

@run_async
def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))
    


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__help__ = """
 Here is the info about the Truth or Dare module:
 
 • /dare*:* Get a dare that you will have to do now.
 
 • /truth*:* Get a question that you will have to tell truth about.
"""

__mod_name__ = "Truth or Dare"
