# Learn MCP Server 🚀

A simple project to understand MCP server fundamentals and JSON-RPC communication.

---

## 📌 What is MCP?

**MCP (Model Context Protocol)** is a standard way for AI models to communicate with external tools and systems.

It provides:
- Structured communication
- Tool calling system
- Secure interaction between client and server

In simple words:
> MCP allows AI and applications to talk in a structured and organized way.

---

## 🎯 Why We Use MCP?

We use MCP to:

- Connect AI with external systems
- Send structured requests
- Receive structured responses
- Standardize communication format

---

## 📦 What is JSON-RPC?

**JSON-RPC** is a lightweight protocol that uses JSON format to send requests and receive responses.

It is:
- Stateless
- Simple
- Transport-independent (can run over HTTP or WebSocket)

---

## 🔢 JSON-RPC Format Structure

A JSON-RPC request looks like this:

```json
{
  "jsonrpc": "2.0",
  "method": "",
  "params": {},
  "id": 1
}
```

- **jsonrpc** → Version (usually "2.0")
- **method** → Name of the method to call
- **params** → Parameters sent to the method
- **id** → Unique request identifier

If the server responds successfully:
- **result** → Contains returned data

If something goes wrong:
- **error** → Contains error object with code and message

---

## 🔔 What is a JSON-RPC Notification?

If we **do not send an `id`**, it is considered a **Notification**.

Notification means:
- Client sends request
- Server does NOT send response
- No result or error returned

Why use notification?
- When response is not required
- Logging events
- Fire-and-forget actions

---

## 🌐 What is HTTP?

**HTTP (HyperText Transfer Protocol)** is a request-response protocol.

How it works:
1. Client sends request
2. Server sends response
3. TCP connection closes after response

Important:
- HTTP builds a TCP connection
- After one response, connection is usually closed
- Stateless communication

---

## 🔐 HTTPS

**HTTPS** is the secure version of HTTP.

It:
- Uses SSL/TLS encryption
- Protects data
- Runs on port 443

---

## 🔄 What is WebSocket?

**WebSocket** is a protocol that keeps a TCP connection open.

| HTTP | WebSocket |
|------|-----------|
| Connection closes after response | Connection stays open |
| Request → Response | Continuous communication |
| One-way per request | Bidirectional |
| Not duplex | Full duplex |

WebSocket is:
- Persistent
- Bidirectional
- Full-duplex (both sides send data anytime)

Used for:
- Real-time apps
- Live chat
- Streaming systems

---

## 🔁 JSON-RPC over WebSocket

When JSON-RPC runs over WebSocket:

- TCP connection remains active
- Communication becomes bidirectional
- Multiple requests and responses can happen
- Full duplex communication

---

## 🧠 Core MCP Concepts

| Concept | Description |
|---------|-------------|
| **Prompts** | Structured instructions given to the AI |
| **Resources** | External data sources the server can access |
| **Tools** | Functions exposed by the MCP server |

---

## 🛠️ Commands

### Setup & Installation

```bash
# Add MCP dependencies
uv add mcp
uv add "mcp-cli"
```

### Run the Server

```bash
# Run with uvicorn (development mode)
uv run uvicorn main:mcp_app --port 8000 --reload

# Run with MCP dev server
mcp dev server.py
```

---

## 🔗 Resources

- **Panaversity MCP Repo**: [learn-agentic-ai - Hello MCP Server](https://github.com/panaversity/learn-agentic-ai/tree/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/01_hello_mcp_server/hello-mcp)

---

## 📺 Project Video

Watch the project walkthrough on YouTube:

[![Watch on YouTube](https://youtu.be/FJVn-CF37WU?si=JWdufCNHShkBcKZg)]

---

## 📚 Summary

We learned:

- What MCP is
- Why MCP is used
- What JSON-RPC is
- JSON-RPC structure
- What notification is
- HTTP vs HTTPS
- HTTP vs WebSocket
- TCP connection behavior
- Bidirectional and full-duplex communication

This repository is created to understand MCP server concepts in a simple and clear way.
