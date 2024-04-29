from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_model_and_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

def translate_text(tokenizer, model, text):
    input_ids = tokenizer(text, return_tensors="pt")["input_ids"]
    generated_sequence = model.generate(input_ids=input_ids)[0].numpy().tolist()
    translated_text = tokenizer.decode(generated_sequence, skip_special_tokens=True)
    return translated_text

#load models and tokenizers
ilo_en_tokenizer, ilo_en_model = load_model_and_tokenizer("models/opus-mt-ilo-en")
en_ilo_tokenizer, en_ilo_model = load_model_and_tokenizer("models/opus-mt-en-ilo")

def eng_to_ilo(text):
    return translate_text(en_ilo_tokenizer, en_ilo_model, text)

def ilo_to_eng(text):
    return translate_text(ilo_en_tokenizer, ilo_en_model, text)


# TEST
sentence_ilo = "mayat a agsapa"
english_sentence = eng_to_ilo(sentence_ilo)
print("ILO-EN:", english_sentence)

sentence_en = "good morning"
ilocano_sentence = ilo_to_eng(sentence_en)
print("EN-ILO:", ilocano_sentence)
