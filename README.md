# RAG 知识库问答系统

基于 **检索增强生成（RAG）** 技术构建的本地知识库问答系统，支持 PDF 文档解析、向量化存储与多轮对话问答。本项目使用智谱 AI（GLM-4-plus）作为大语言模型，ChromaDB 作为向量数据库。

---

## 功能特性

- **PDF 文档解析**：自动加载 PDF 并切块，保留上下文重叠
- **向量化存储**：使用智谱 AI `embedding-3` 模型将文本向量化，持久化存储到 ChromaDB
- **语义检索**：基于相似度搜索，精准召回相关知识片段
- **多轮对话**：Streamlit Web UI 支持带历史记录的连续问答
- **命令行问答**：`ask.py` 支持快速终端查询

---

## 项目结构

```
rag-knowledge-base-main/
├── rag_demo/
│   ├── build_db.py          # 构建向量数据库（PDF → ChromaDB）
│   ├── ask.py               # 命令行问答脚本
│   ├── split_pdf.py         # PDF 分块测试工具
│   ├── streamlit_app.py     # Streamlit 多轮对话 Web UI
│   ├── zhipuai_embedding.py # 智谱 AI Embedding 自定义封装
│   ├── pumpkin_book.pdf     # 示例知识库文档（南瓜书）
│   └── .env                 # API 密钥配置（不提交到 Git）
├── chroma_db/               # 向量数据库持久化目录
├── requirements.txt         # Python 依赖
└── README.md
```

---

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

> 推荐 Python 3.10+

### 2. 配置 API 密钥

编辑 `rag_demo/.env`，填入你的智谱 AI API Key：

```env
ZHIPUAI_API_KEY=你的_API_KEY
```

> 在 [智谱 AI 开放平台](https://open.bigmodel.cn/) 注册并获取 API Key。

### 3. 构建向量数据库

将你的 PDF 放入 `rag_demo/` 目录（默认使用 `pumpkin_book.pdf`），然后运行：

```bash
cd rag_demo
python build_db.py
```

构建完成后，向量数据库将保存到 `chroma_db/` 目录。

### 4. 问答

**方式一：命令行**

```bash
cd rag_demo
python ask.py
```

**方式二：Streamlit Web UI**

```bash
cd rag_demo
streamlit run streamlit_app.py
```

浏览器访问 `http://localhost:8501`，即可进行多轮对话。

---

## 技术栈

| 组件 | 技术 |
|------|------|
| 大语言模型 | 智谱 AI GLM-4-plus |
| Embedding 模型 | 智谱 AI embedding-3 |
| 向量数据库 | ChromaDB |
| RAG 框架 | LangChain |
| PDF 解析 | PyMuPDF / PyPDFLoader |
| Web UI | Streamlit |

---

## RAG 流程说明

```
PDF 文档
   ↓ PyPDFLoader
文本分块（chunk_size=500，overlap=50）
   ↓ ZhipuAI Embedding
向量存储（ChromaDB）
   ↓ 相似度检索（Top-K）
召回相关文本片段
   ↓ 拼接 Prompt
GLM-4-plus 生成回答
```

---

## 注意事项

- `.env` 文件包含 API 密钥，**不要提交到公开代码仓库**
- 首次构建向量库需要调用 Embedding API，会产生少量 token 费用
- `chroma_db/` 目录可以复用，无需重复构建
