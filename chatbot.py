from rasa import train
from rasa.core import run
from rasa.model import get_model

def train_chatbot():
    train('config.yml', 'data', 'models')

def run_chatbot():
    model_path = get_model()
    run(model_path)

if __name__ == "__main__":
    train_chatbot()