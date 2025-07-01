from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain 

# Configuration API Gemini
os.environ["GEMINI_API_KEY"] = "AIzaSyAU5xz5YO4_d-GXTFagwhn2TS1WNgtB950"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

prompt = PromptTemplate(
    input_variables=["question","chat_history"],
    template="""
Tu es un psychologue virtuel bienveillant.
Voici l'historique de la conversation : {chat_history}
Analyse l’émotion dans la phrase suivante et
donne une réponse douce, empathique et adaptée.
Si la personne est triste, sois rassurant.
Si elle est stressée, aide-la à se détendre.
Si elle est perdue, propose une réflexion.
Si elle est joyeuse, encourage-la à partager.

Phrase de l'utilisateur : {question}
Réponse :
"""
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True
)


app = Flask(__name__)
CORS(app)

def is_psychology_question(question):
    keywords = [
        "stress", "anxiété", "peur", "émotion", 
        "dépression", "colère", "tristesse"
        ,"triste","mal-être", "écoute", "solitude", 
        "angoisse", "fatigue", "motivation", "burn-out",
        "psy", "psychologue", "psychologie", "je vais mal",
        "je me sens","seul", "vide", "sens", "perdu", 
        "échec", "désespoir", "envie de rien",
        "je n'arrive pas", "je suis fatigué", 
        "je me pose des questions",
        "est-ce normal", "comment faire pour", 
        "je cherche", " motiver", "pas confiance",
        "confiance","doute","capacité","je m'appelle",
        "nom", "souviens","précédemment","pleure"
    ]
    return any(kw in question.lower() for kw in keywords)


def generer_reponse_psy(question):
     return chain.invoke({"question": question})["text"]

def chatbot_psy(question):
    if not is_psychology_question(question):
        return "Je suis un psychologue IA. Pose-moi une question liée à ce que tu ressens ou à ton bien-être émotionnel."
    return generer_reponse_psy(question)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/chatbot")
def chatbot():
    return render_template("index.html")



@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()
    question = data.get("question", "")
    response = chatbot_psy(question)

    # Corriger les réponses texte directes vs objets AIMessage
    if isinstance(response, str):
        return jsonify({"response": response})
    return jsonify({"response": response.content})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
