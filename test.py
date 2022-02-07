from models import session,English
import pandas as pd

def evacuate_data():
    datas = session.query(English).all()
    insert_datas = []
    for data in datas:
        insert_data ={
            "data.id":{
                        "english_sentence":data.english_sentence,
                        "japanese_sentence":data.japanese_sentence,
                        }
        } 
        insert_datas.append(insert_data)

    df = pd.DataFrame(insert_datas)
    df.to_json("english.json",force_ascii=False)

def restore_data():
    df = pd.read_json("english.json")
    print(df["english_sentence"])

    # english_table.english_sentence = 

# evacuate_data()
restore_data()