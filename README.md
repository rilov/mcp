# 🛰️ MCP Trace Demo with LangChain

This project help you to understand MCP and explains  how  to **trace API calls** made from LangChain's MCP (Model Context Protocol) modules using a simple proxy setup. This will help you to understand the MCP and how the model interacts with it.

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
Verify installation:
uv --version
```

2. Create and Activate a Virtual Environment
Using uv:

```bash
Copy
Edit
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
Or using python:

```bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate
```
Install Dependencies

```bash


uv pip install -r requirements.txt
# OR
pip install -r requirements.txt
```
### 🏃 How to Run


Step 1: Start the Proxy Server
In Terminal 1, run:

```bash
Copy
Edit
python proxy.py
This will:

Start a Flask server on http://localhost:5000

Log every OpenAI API call and response payload
```
Step 2: Run the MCP Client
In Terminal 2, run:

```bash
Copy
Edit
python mcpclient.py
This will:

Start the weather MCP server (mcpweatherserver.py)


```
✅ What You’ll See
In the proxy terminal: full trace of requests/responses to OpenAI

In the client terminal: the final agent reply, something like:

Response from weather forecast service.. Nice weather today

📁 Project Structure

File	Description
proxy.py	HTTP proxy that logs OpenAI API calls
mcpclient.py	LangChain MCP client that interacts with the weather tool
mcpweatherserver.py	Minimal MCP tool server using FastMCP and stdio transport
requirements.txt	Required Python packages
🔍 Why This Project is Useful
Gain visibility into OpenAI API usage behind the scenes

Understand how MCP-based tools work with LangChain agents

Debug and trace tool-based interactions in real time

Perfect for learning LangChain + MCP + function calling

🧠 Tech Stack
LangChain

LangGraph

MCP (Model Context Protocol)

Flask for proxy

OpenAI API (proxied for traceability)

🧪 Example Trace (Proxy Output)
```bash

````

🚀 Future Ideas
Add more MCP tools (e.g., calendar, reminder, calculator)

Visualize call chains and LLM decisions

Integrate LangSmith tracing for richer insights

Happy Tracing! 🧙‍♂️✨

vbnet
Copy
Edit

Let me know if you'd like this saved as a file or want to include code badges, GitHub Actions, or demo screenshots!
