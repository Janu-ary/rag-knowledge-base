from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("rag_demo/pumpkin_book.pdf")
pages = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(pages)

print(f"共 {len(chunks)} 块，开始向量化...")

embedding = ZhipuAIEmbeddings(
    api_key="fb9b96ec43ed48038bba73fa0cae4ec4.ZmpsmO77vCY69GPg",
    model="embedding-3"
)

# 分批处理，每批50条
batch_size = 50
db = None
for i in range(0, len(chunks), batch_size):
    batch = chunks[i:i+batch_size]
    if db is None:
        db = Chroma.from_documents(batch, embedding, persist_directory="./chroma_db")
    else:
        db.add_documents(batch)
    print(f"已处理 {min(i+batch_size, len(chunks))}/{len(chunks)} 块")

print("向量库建好了")