import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "DATASETS"

def load_data():
    customers = pd.read_csv(DATA_DIR / "tragerinc_customer_info.csv")
    energy = pd.read_csv(DATA_DIR / "tragerinc_energy_usage.csv")
    chatbot = pd.read_csv(DATA_DIR / "tragerinc_chatbot_interactions.csv")
    support = pd.read_csv(DATA_DIR / "tragerinc_support_tickets.csv")

    return customers, energy, chatbot, support
