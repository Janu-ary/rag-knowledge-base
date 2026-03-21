from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 加载PDF
loader = PyPDFLoader("rag_demo/pumpkin_book.pdf")
pages = loader.load()

print(f"PDF共 {len(pages)} 页")

# 切块
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,    # 每块最多500字
    chunk_overlap=50   # 块之间重叠50字，防止切断句子
)
chunks = splitter.split_documents(pages)

print(f"切成了 {len(chunks)} 块")
print("第一块内容：")
print(chunks[0].page_content)