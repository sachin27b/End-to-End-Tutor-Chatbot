from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings, load_data, split_data
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS

from src.prompt import *
import os

app = Flask(__name__)
embeddings = download_hugging_face_embeddings()
PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

pages = load_data("data/Neural Networks from Scratch in Python.pdf")
docs = split_data(pages)
db = FAISS.from_documents(docs, embeddings)


llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})


qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=db.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)

# @app.route("/")
# def index():
#     return render_template('index.html')



# @app.route("/get", methods=["GET", "POST"])
# def chat():
#     msg = request.form["msg"]
#     input = msg
#     print(input)
#     result=qa({"query": input})
#     print("Response : ", result["result"])
#     return str(result["result"])


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        msg = request.form["msg"]
    else:
        msg = request.args.get("msg")
    
    input = msg
    print(input)
    result = qa({"query": input})
    print("Response: ", result["result"])
    return str(result["result"])
if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)