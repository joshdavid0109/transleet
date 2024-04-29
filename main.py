from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

ilo_en_tokenizer = AutoTokenizer.from_pretrained("models/opus-mt-ilo-en")
ilo_en_model = AutoModelForSeq2SeqLM.from_pretrained("models/opus-mt-ilo-en")

en_ilo_tokenizer = AutoTokenizer.from_pretrained("models/opus-mt-en-ilo")
en_ilo_model = AutoModelForSeq2SeqLM.from_pretrained("models/opus-mt-en-ilo")

#TEST ILO TO EN
sentence_ilo="mayat a agsapa"

input_ids=ilo_en_tokenizer(sentence_ilo, return_tensors="pt")["input_ids"]
generated_sequence = ilo_en_model.generate(input_ids=input_ids)[0].numpy().tolist()

english_sentence=ilo_en_tokenizer.decode(generated_sequence, skip_special_tokens=True)
print(english_sentence)

#TEST EN TO ILO
sentence_en="good morning"

input_ids=en_ilo_tokenizer(sentence_en, return_tensors="pt")["input_ids"]
generated_sequence = en_ilo_model.generate(input_ids=input_ids)[0].numpy().tolist()

ilocano_sentence=en_ilo_tokenizer.decode(generated_sequence, skip_special_tokens=True)
print(ilocano_sentence)