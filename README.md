# 📝 FormIO MCP Server

This is an MCP (Model Context Protocol) server for integrating with the FormIO API, enabling AI agents to interact with dynamic form creation, submission management, and user roles using natural language input.

The goal of this project is to expose FormIO's functionality through MCP-compatible tools that can be used seamlessly by large language models and agent frameworks.

## 🧠 What is MCP?

MCP (Model Context Protocol) is a lightweight protocol designed to let AI agents interact with external tools and APIs in a structured and modular way. Think of it like USB for AI — this server acts as a "driver" for the FormIO platform.

With this MCP server, AI models can:

- 📋 Create and manage dynamic forms  
- 📊 Submit and retrieve form data  
- 👥 Handle user authentication and authorization  
- 🔑 Manage role-based permissions and access control  

## 🚀 How to Run

To use this MCP server, you'll need:

### ✅ Prerequisites

- Python 3.13+  
- [uv](https://github.com/astral-sh/uv) – a modern Python package manager  
- A supported LLM (e.g., Claude)  
- A FormIO account – sign up at [form.io](https://form.io)  

### Claude Desktop Configuration

Add this to your Claude Desktop config:

```json
{
  "mcpServers": {
    "mcp-formio": {
      "command": "uvx",
      "args": [
        "mcp-formio-server",
        "--api-url",
        "YOUR_FORMIO_API_URL"
      ]
    }
  }
}
```

## 📚 Available Tools

### Form Management

- Create forms with complex components  
- Retrieve paginated form listings  
- Manage form submissions  

### User & Authentication

- Create and authenticate users  
- Handle admin authentication  
- Manage user roles and permissions  

### Submission Handling

- Create form submissions  
- Retrieve and load submission data  
- Get paginated lists of submissions  

## 🤝 Contributions Welcome!

Whether you're passionate about form management, AI agent development, or robust API integrations — we'd love your help improving this project. You can contribute by:

- Adding support for additional FormIO endpoints  
- Improving the structure of tool responses  
- Writing better tests and usage examples  
- Sharing feedback or ideas via Issues or Discussions  

Feel free to fork, explore, and open a PR. Let's empower agents with better data collection and management capabilities!

**MCP-FORGE – Building tools for the future of intelligent automation.**
