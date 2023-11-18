from neural_toys_model import NeuralToysModel

def main():
    neural_toys_model = NeuralToysModel(age=10, name="Максим")
    print(f"Совет для ребенка - {neural_toys_model.get_advide()}", flush=True)
    print(f"Почему небо синее? - {neural_toys_model.answer_to_questions(questions='Почему небо синее?')}", flush=True)
    
if __name__ == "__main__":
    main()