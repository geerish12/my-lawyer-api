import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("service-account.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    "1. The State": ["Mauritius shall be a sovereign democratic State which shall be known as the Republic of Mauritius."],
    "2. Constitution is supreme law": ["This Constitution is the supreme law of Mauritius and if any other law is inconsistent with this Constitution, that other law shall, to the extent of the inconsistency, be void."],
    "3. Fundamental rights and freedoms of individual": [
        "It is hereby recognised and declared that in Mauritius there have existed and shall continue to exist without discrimination by reason of race, place of origin, political opinions, colour, creed or sex, but subject to respect for the rights and freedoms of others and for the public interest, each and all of the following human rights and fundamental freedoms—",
        ["(a) the right of the individual to life, liberty, security of the person and the protection of the law;",
         "(b) freedom of conscience, of expression, of assembly and association and freedom to establish schools;",
         "(c) the right of the individual to protection for the privacy of his home and other property and from deprivation of property without compensation,"]
    ],
    "4. Protection of right to life": [
        "(1) No person shall be deprived of his life intentionally save in execution of the sentence of a Court in respect of a criminal offence of which he has been convicted.",
        "(2) A person shall not be regarded as having been deprived of his life in contravention of this section, if he dies as the result of the use, to such extent and in such circumstances as are permitted by law, of such force as is reasonably justifiable—",
        ["(a) for the defence of any person from violence or for the defence of property;",
         "(b) in order to effect a lawful arrest or to prevent the escape of a person lawfully detained;",
         "(c) for the purpose of suppressing a riot, insurrection or mutiny; or",
         "(d) in order to prevent the commission by that person of a criminal offence,"],
        "or if he dies as the result of a lawful act of war."
    ],
    "5. Protection of right to personal liberty": [
        "(1) No person shall be deprived of his personal liberty save as may be authorised by law—",
        ["(a) in consequence of his unfitness to plead to a criminal charge or in execution of the sentence or order of a Court, whether in Mauritius or elsewhere, in respect of a criminal offence of which he has been convicted;",
         "(b) in execution of the order of a Court punishing him for contempt of that Court or of another Court;",
         "(c) in execution of the order of a Court made to secure the fulfilment of any obligation imposed on him by law;",
         "(d) for the purpose of bringing him before a Court in execution of the order of a Court;",
         "(e) upon reasonable suspicion of his having committed, or being about to commit, a criminal offence;",
         "(f) in the case of a person who has not attained the age of 18 years, for the purpose of his education or welfare;",
         "(g) for the purpose of preventing the spread of an infectious or contagious disease;",
         "(h) in the case of a person who is, or is reasonably suspected to be, of unsound mind or addicted to drugs or alcohol, for the purpose of his care or treatment or the protection of the community;",
         "(i) for the purpose of preventing the unlawful entry of that person into Mauritius, or for the purpose of effecting the expulsion, extradition or other lawful removal of that person from Mauritius or for the purpose of restricting that person while he is being conveyed through Mauritius in the course of his extradition or other lawful removal as a convicted prisoner from one country to another country;",
         "(j) in the case of a person who is not a citizen, for the purpose of the regulation of his right to enter or remain in Mauritius or for the purpose of the implementation of any obligation or commitment of the Republic of Mauritius under any treaty or other international agreement;"],
        "or for the purpose of preventing the unlawful entry of that person into Mauritius, or for the purpose of effecting the expulsion, extradition or other lawful removal of that person from Mauritius or for the purpose of restricting that person while he is being conveyed through Mauritius in the course of his expulsion, extradition or other lawful removal from one country to another country."
    ],
    "6. Protection from slavery and forced labour": [
        "(1) No person shall be held in slavery or servitude.",
        "(2) No person shall be required to perform forced labour."]
}

# Add data to the "constitution" collection
def add_data_to_firestore(data, parent_ref):
    for key, value in data.items():
        doc_ref = parent_ref.document(key)
        
        if isinstance(value, list):
            add_data_to_firestore(value, doc_ref.collection('subarray'))
        else:
            doc_ref.set({"text": value})

        print(f"Document '{key}' added to the database.")

root_ref = db.collection("constitution")
add_data_to_firestore(data, root_ref)