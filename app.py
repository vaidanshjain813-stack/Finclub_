from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

openai.api_key = "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

PROMPT_TEMPLATE = """You are a professional Indian Chartered Accountant. Answer the following query in a simple, clear way. Use {lang} language.

Query: {query}
Answer:
"""

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query", "")
    lang = data.get("lang", "English")

    prompt = PROMPT_TEMPLATE.format(query=query, lang=lang)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )
        answer = response["choices"][0]["message"]["content"]
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host:"0.0.0.0, port=8080)
