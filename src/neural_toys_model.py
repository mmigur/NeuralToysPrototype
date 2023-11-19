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
        """
        Функция для ответа на вопрос ребенка простым языком.
        Принимает: вопрос ребенка.
        Возвращает: ответ, который ребенок может понять.
        """
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
        """
        Функция, которая дает совет ребенку, помогающим ему существовать.
        Возвращает: совет для ребенка.
        """
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
    

    def generate_story(
            main_characters: str, 
            mission_of_main_characters: str,
            universe: str,
            additional_characters: str,
            user_additions: str
        ) -> str:
        """
        Функция, генерирующая сказку для ребенка по запросам его родителя.
        Принимает: описание главного героя, задачу которую он будет решать,
                   описание мира в котором будет происходит сказка,
                   дополнительные персонажи участвующие в сказке,
                   и пожелания пользователя.
        Возвращает: сказу с параметрами пользователями.
        """
        content_question = config.STORY_PROMT_PART_1 + \
                           main_characters + \
                           config.STORY_PROMT_PART_2 + \
                           mission_of_main_characters + \
                           config.STORY_PROMT_PART_3 + \
                           universe + config.STORY_PROMT_PART_4 + \
                           additional_characters + \
                           user_additions
        
        response = g4f.ChatCompletion.create(
            model=config.GPT_MODEL_NAME,
            messages=[{"role": "user", "content": content_question}],
            stream=config.STREAM
        )

        return "".join(response)
