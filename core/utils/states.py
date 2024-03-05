from aiogram.fsm.state import StatesGroup, State

class MyStates(StatesGroup):
    START = State()
    ADDBOT = State()
    BOTSELECT = State()

    ADMIN_COMMANDS = State()
    SUB_OFF = State()
    SUB_CONTINUE = State()
    SUB_MONTH = State()
    SUB_TRANSFORM = State()
    SUB_NEWADMIN = State()

    CAPCHA = State()
    NEWCAPCHA = State()

    WELCOME_SELECT = State()

    NEW_WELCOME_TEXT = State()
    NEW_WELCOME_BUTTON = State()
    NEW_WELCOME_DELAY = State()
    NEW_WELCOME_DELETE = State()

    СHANGE_WELCOME_TEXT = State()
    СHANGE_WELCOME_BUTTONS = State()
    СHANGE_WELCOME_DELAY = State()
    CHANGE_WELCOME_DELETE = State()

    NEW_SPAM_TEXT = State()
    NEW_SPAM_BUTTON = State()
    NEW_SPAM_DELAY = State()
    NEW_SPAM_DELETE = State()