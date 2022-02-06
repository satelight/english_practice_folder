from models import session,English
import pandas as pd

def evacuate_data():
    datas = session.query(English).all()
    insert_datas = []
    for data in datas:
        insert_data ={
            "english_sentence":data.english_sentence,
            "japanese_sentence":data.japanese_sentence,
        }
        insert_datas.append(insert_data)

    df = pd.DataFrame(insert_datas)
    df.to_csv("english.csv", index=False, header=[
            "english_sentence", "japanese_sentence"])

def restore_data():
    df = pd.read_csv("english_csv")
    english_table = English()

    # english_table.english_sentence = 
