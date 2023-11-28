from chatterbot.logic import LogicAdapter

class WeatherAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['what', 'is', 'weather']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters=None):
        from chatterbot.conversation import Statement

