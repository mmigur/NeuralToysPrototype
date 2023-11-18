import g4f

import config

class NeuralToysModel:
    def __init__(
            self, 
            age: int, 
            name: str
        ) -> None:
        self.age = str(age) + "лет."
        self.name = name

    def answer_to_questions(self, questions: str) -> str:
        content_question = questions + \
                           config.KIDS_MODE + \
                           self.age + \
                           self.name

        response = g4f.ChatCompletion.create(
            model=config.GPT_MODEL_NAME,
            messages=[{"role": "user", "content": content_question}],
            stream=config.STREAM
        )

        return "".join(response)
    
    def get_advide(self) -> str:
        content_question = config.ADVICE_TEMPLATE + \
                           config.KIDS_MODE + \
                           self.age + \
                           self.name
        
        response = g4f.ChatCompletion.create(
            model=config.GPT_MODEL_NAME,
            messages=[{"role": "user", "content": content_question}],
            stream=config.STREAM
        )

        return "".join(response)