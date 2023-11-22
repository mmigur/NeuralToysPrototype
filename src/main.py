from fastapi import FastAPI
from src.neural_toys_model import NeuralToysModel

app = FastAPI(
    title="NeuralToys", 
    version="0.1.0"
)

@app.get("/answer_to_question")
async def answer_to_question(
        question: str, 
        age: int, 
        name: str
    ):
    neural_toys_model = NeuralToysModel(age=age, name=name)
    return {"status": 200, "answer": neural_toys_model.answer_to_questions(questions=question)}

@app.get("/get_advice")
async def get_advice(
        age: int, 
        name: str
    ):
    neural_toys_model = NeuralToysModel(age=age, name=name)
    return {"status": 200, "advice": neural_toys_model.get_advide()}

@app.get("/get_story")
async def get_story(
        main_characters: str,
        mission_of_main_characters: str,
        universe: str,
        additional_characters: str,
        user_additions: str,
        age: int,
        name: str
    ):
    neural_toys_model = NeuralToysModel(age=age, name=name)
    story = neural_toys_model.generate_story(
        main_characters=main_characters,
        mission_of_main_characters=mission_of_main_characters,
        universe=universe,
        additional_characters=additional_characters,
        user_additions=user_additions
    )
    return {"status": 200, "story": story}

@app.get("/get_interesting_fact")
async def get_interesting_fact(
        age: int,
        name: str
    ):
    neural_toys_model = NeuralToysModel(age=age, name=name)
    interesting_fact = neural_toys_model.get_interesting_fact()
    return {"status": 200, "interesting_fact": interesting_fact}