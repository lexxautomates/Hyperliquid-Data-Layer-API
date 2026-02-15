# Ollama Qwen2.5-Coder Setup Guide

This guide explains how to configure Claude Code/VSCode to use local Ollama with Qwen2.5-Coder model.

## Overview

Ollama is now configured with Qwen2.5-Coder as the primary coding assistant. All other LLMs have been removed to keep the setup clean and focused.

## Current Setup

### Available Models
- **qwen2.5-coder:14b** - Primary coding model (9.0 GB)
- **qwen3:8b** - Secondary model (5.2 GB)

### Removed Models
- llama3.2:latest
- llama3.2:1b  
- llama3:latest
- mistral-nemo:latest
- glm4:latest

## Configuration Files

### VSCode Settings (`.vscode/settings-ollama.json`)

```json
{
    "cline.apiProvider": "openai-compatible",
    "cline.apiBaseUrl": "http://localhost:11434/v1",
    "cline.apiKey": "ollama",
    "cline.model": "qwen2.5-coder:14b",
    "cline.temperature": 0.1,
    "cline.maxTokens": 8000,
    "cline.systemPrompt": "You are Qwen2.5-Coder, a specialized coding assistant. Provide clear, accurate, and well-structured code solutions. Focus on best practices, efficiency, and maintainability.",
    "cline.enableAutoComplete": true,
    "cline.enableChatMode": true,
    "cline.contextWindow": 32768,
    "cline.streamingEnabled": true,
    "cline.requestTimeout": 120000,
    "cline.retryAttempts": 3,
    "cline.customHeaders": {
        "Content-Type": "application/json"
    },
    "ollama.models": [
        "qwen2.5-coder:14b",
        "qwen3:8b"
    ],
    "ollama.defaultModel": "qwen2.5-coder:14b",
    "ollama.baseUrl": "http://localhost:11434",
    "ollama.preferredModel": "qwen2.5-coder:14b"
}
```

## Usage

### Switching to Ollama Configuration

1. Open VSCode settings (`Ctrl+,` or `Cmd+,`)
2. Search for "cline"
3. Either:
   - Use the workspace settings from `.vscode/settings-ollama.json`
   - Or manually copy the settings to your user settings

### Starting Ollama Service

Ollama should be running automatically. If not:

```bash
# Start Ollama service
ollama serve

# Check if service is running
curl http://localhost:11434/api/tags
```

### Testing the Configuration

```bash
# Test with direct API call
curl -X POST http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-coder:14b",
    "messages": [{"role": "user", "content": "Write a hello world function"}],
    "stream": false
  }'

# Test with ollama CLI
ollama run qwen2.5-coder:14b "Your coding question here"
```

## Model Characteristics

### Qwen2.5-Coder (14B)
- **Specialization**: Coding and programming tasks
- **Context Window**: 32K tokens
- **Strengths**: Code generation, debugging, optimization
- **Temperature**: 0.1 (more deterministic coding)
- **Max Tokens**: 8000 (longer code responses)

### Qwen3 (8B)
- **Specialization**: General purpose assistant
- **Use Case**: Backup model for non-coding tasks
- **Size**: Smaller, faster responses

## Integration with Existing AI Agents

To use Qwen2.5-Coder with existing AI agents in `ai_agents/`:

```python
from openai import OpenAI

# Qwen2.5-Coder via Ollama
qwen_client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

response = qwen_client.chat.completions.create(
    model="qwen2.5-coder:14b",
    messages=[{"role": "user", "content": "Your coding question"}],
    max_tokens=8000,
    temperature=0.1
)
```

## Performance Considerations

### Hardware Requirements
- **RAM**: Minimum 16GB recommended (models are 9GB + 5GB)
- **Storage**: 14GB for both models
- **CPU**: Modern multi-core processor recommended

### Optimization Tips
1. Close unnecessary applications to free RAM
2. Use qwen2.5-coder:14b for complex coding tasks
3. Use qwen3:8b for simpler queries to save resources
4. Set appropriate timeout values (120s recommended)

## Troubleshooting

### Common Issues

1. **Model Not Found**: Ensure the model is properly pulled
   ```bash
   ollama pull qwen2.5-coder:14b
   ```

2. **Service Not Running**: Start Ollama service
   ```bash
   ollama serve
   ```

3. **Memory Issues**: Close other applications or use smaller model

4. **VSCode Not Using Ollama**: Check that workspace settings are applied

### Debug Commands

```bash
# Check service status
curl http://localhost:11434/api/tags

# Check running models
ollama ps

# Test direct generation
ollama run qwen2.5-coder:14b "test prompt"
```

## Switching Back to Cloud Models

If you need to switch back to GLM-5 or other cloud models:

1. Rename `settings.json` to `settings-ollama.json`
2. Rename the desired settings file to `settings.json`
3. Restart VSCode or reload settings

## Maintenance

### Updating Models
```bash
# Check for updates
ollama pull qwen2.5-coder:14b

# Remove old versions if needed
ollama rm qwen2.5-coder:14b:old-tag
```

### Monitoring Usage
```bash
# Check model sizes
ollama list

# Monitor system resources
ollama ps
```

## Security Notes

- Ollama runs locally, so your code stays private
- No API keys required for local models
- Network access only for model downloads
- Consider firewall rules if security is a concern

## Next Steps

1. Test the configuration with a simple coding task
2. Integrate with your development workflow
3. Explore the model's capabilities with different coding challenges
4. Consider setting up automated testing with the model

The setup is now optimized for local coding assistance with Qwen2.5-Coder!
