# 🛰️ MCP Trace Demo with LangChain

This project demonstrates how to **trace API calls** made from LangChain's MCP (Model Context Protocol) modules using a simple proxy setup.

It includes:

- A **proxy server** that intercepts and logs OpenAI API traffic
- An **MCP client** that uses LangChain agents to interact with tools
- A **basic weather tool server** exposed via the MCP protocol

---

## 📦 Requirements

Install dependencies using [`uv`](https://github.com/astral-sh/uv) (recommended) or `pip`.

---

## ⚙️ Setup Instructions

### 1. Install `uv` (Recommended)

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
