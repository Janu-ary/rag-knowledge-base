from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_community.vectorstores import Chroma
from openai import OpenAI

# 加载向量库
embedding = ZhipuAIEmbeddings(api_key="fb9b96ec43ed48038bba73fa0cae4ec4.ZmpsmO77vCY69GPg", model="embedding-3")
db = Chroma(persist_directory="./chroma_db", embedding_function=embedding)

# 用户提问
question = "什么是梯度下降？"

# 搜索最相关的3个块
results = db.similarity_search(question, k=3)

print("找到的相关内容：")
for i, r in enumerate(results):
    print(f"\n--- 第{i+1}块 ---")
    print(r.page_content)

# 拼成prompt发给模型
context = "\n\n".join([r.page_content for r in results])
prompt = f"""根据以下内容回答问题，如果内容中没有相关信息就说不知道。

内容：
{context}

问题：{question}
"""

client = OpenAI(api_key="fb9b96ec43ed48038bba73fa0cae4ec4.ZmpsmO77vCY69GPg", base_url="https://open.bigmodel.cn/api/paas/v4/")
response = client.chat.completions.create(
    model="glm-4-plus",
    messages=[{"role": "user", "content": prompt}]
)
print("\n模型回答：")
print(response.choices[0].message.content)