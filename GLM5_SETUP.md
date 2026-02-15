# GLM-5 Integration Setup Guide

This guide explains how to use GLM-5 with VSCode and Cline in the Hyperliquid Data Layer API project.

## Overview

GLM-5 is now configured to work with VSCode through the Modal Research API. The setup includes:

- API endpoint: `https://api.us-west-2.modal.direct/v1`
- Model: `zai-org/GLM-5-FP8`
- Authentication via Bearer token

## Configuration Files

### 1. VSCode Settings (`.vscode/settings.json`)

The VSCode settings are automatically configured with:

```json
{
    "cline.apiProvider": "openai-compatible",
    "cline.apiBaseUrl": "https://api.us-west-2.modal.direct/v1",
    "cline.apiKey": "modalresearch_a5Tslxze8-s_XYAh3qcve3WVQsRUCW8VLPvwsDE9bXk",
    "cline.model": "zai-org/GLM-5-FP8",
    "cline.temperature": 0.7,
    "cline.maxTokens": 4000,
    "cline.systemPrompt": "You are GLM-5, a helpful AI assistant. Provide clear, accurate, and thoughtful responses to user queries.",
    "cline.enableAutoComplete": true,
    "cline.enableChatMode": true,
    "cline.contextWindow": 8192,
    "cline.streamingEnabled": true,
    "cline.requestTimeout": 30000,
    "cline.retryAttempts": 3,
    "cline.customHeaders": {
        "Content-Type": "application/json"
    }
}
```

### 2. Environment Variables (`.env.example`)

Added GLM-5 configuration to the environment variables:

```bash
# GLM-5 API Configuration (for VSCode/Cline integration)
# Modal Research API for GLM-5 model
GLM5_API_KEY=modalresearch_a5Tslxze8-s_XYAh3qcve3WVQsRUCW8VLPvwsDE9bXk
GLM5_API_BASE_URL=https://api.us-west-2.modal.direct/v1
GLM5_MODEL=zai-org/GLM-5-FP8
```

## Usage

### With Cline Extension

1. Install the Cline extension in VSCode
2. The settings are automatically applied from `.vscode/settings.json`
3. GLM-5 will be available as the default model

### Direct API Usage

You can also use GLM-5 directly with curl:

```bash
curl -X POST "https://api.us-west-2.modal.direct/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer modalresearch_a5Tslxze8-s_XYAh3qcve3WVQsRUCW8VLPvwsDE9bXk" \
  -d '{
    "model": "zai-org/GLM-5-FP8",
    "messages": [
      {"role": "user", "content": "How many r-s are in strawberry?"}
    ],
    "max_tokens": 500
  }'
```

### With Python

```python
import requests
import json

url = "https://api.us-west-2.modal.direct/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer modalresearch_a5Tslxze8-s_XYAh3qcve3WVQsRUCW8VLPvwsDE9bXk"
}

data = {
    "model": "zai-org/GLM-5-FP8",
    "messages": [
        {"role": "user", "content": "Your question here"}
    ],
    "max_tokens": 500
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result['choices'][0]['message']['content'])
```

## VSCode Extensions

Recommended extensions are included in `.vscode/extensions.json`:

- **saoudrizwan.claude-dev** - Claude Dev (alternative to Cline)
- **ms-python.python** - Python support
- **ms-python.vscode-pylance** - Python IntelliSense
- **ms-python.black-formatter** - Code formatting
- **esbenp.prettier-vscode** - General formatting
- **github.copilot** - GitHub Copilot
- **github.copilot-chat** - Copilot Chat

## Setup Verification

1. Open the project in VSCode
2. Install recommended extensions when prompted
3. Cline should automatically use GLM-5 as configured
4. Test with a simple question to verify connectivity

## Troubleshooting

### Common Issues

1. **API Key Not Working**: Verify the token is correct and has proper permissions
2. **Connection Timeout**: Check internet connectivity and API endpoint availability
3. **Model Not Found**: Ensure the model name `zai-org/GLM-5-FP8` is correct

### Debug Steps

1. Check VSCode settings are loaded: `Ctrl+,` → search for "cline"
2. Test API directly with curl command above
3. Check VSCode developer console for errors

## Security Notes

- The API key is included in VSCode settings for this project
- Consider using environment variables for production deployments
- The key should be kept confidential and not shared

## Integration with Existing AI Agents

The existing AI agents in `ai_agents/` use OpenRouter. You can extend them to use GLM-5 by:

1. Adding GLM-5 configuration to their OpenAI client setup
2. Using the same base URL and model configuration
3. Updating the environment variables accordingly

Example for existing agents:

```python
from openai import OpenAI

# GLM-5 client
glm5_client = OpenAI(
    api_key="modalresearch_a5Tslxze8-s_XYAh3qcve3WVQsRUCW8VLPvwsDE9bXk",
    base_url="https://api.us-west-2.modal.direct/v1"
)

response = glm5_client.chat.completions.create(
    model="zai-org/GLM-5-FP8",
    messages=[{"role": "user", "content": "Your message"}],
    max_tokens=500
)
