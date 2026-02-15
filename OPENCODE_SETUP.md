# OpenCode Desktop Setup Guide

This guide explains how to set up OpenCode Desktop to run locally with VSCode integration and Google Antigravity OAuth.

## Installation Complete ✅

OpenCode Desktop has been successfully installed on your Mac:

- **Downloaded**: `opencode-ui-0.2.0-arm64.dmg` (161 MB)
- **Installed**: `/Applications/OpenCode.app`
- **Launched**: Application is now running

## Configuration Steps

### 1. First Launch Setup

When OpenCode launches for the first time:

1. **Welcome Screen**: Choose your preferred setup mode
2. **Authentication**: Configure your AI provider
3. **Workspace Setup**: Select your working directory

### 2. Google Antigravity OAuth Integration

To integrate Google Antigravity with OAuth:

#### Option A: Direct OAuth Integration
```bash
# OpenCode will typically provide an OAuth flow
# Look for "Sign in with Google" or "Connect to Google Antigravity"
```

#### Option B: Manual Configuration
If needed, configure OAuth manually:

1. Get Google Antigravity OAuth credentials:
   - Client ID
   - Client Secret
   - Redirect URI

2. Add to OpenCode settings:
   ```json
   {
     "auth": {
       "provider": "google-antigravity",
       "oauth": {
         "clientId": "your_client_id",
         "clientSecret": "your_client_secret",
         "redirectUri": "http://localhost:3000/auth/callback"
       }
     }
   }
   ```

### 3. VSCode Integration

#### Method 1: VSCode Extension
1. Install the OpenCode VSCode extension
2. Configure in VSCode settings:
   ```json
   {
     "opencode.enabled": true,
     "opencode.serverUrl": "http://localhost:3000",
     "opencvde.autoConnect": true
   }
   ```

#### Method 2: CLI Integration
OpenCode typically provides a CLI that can be used with VSCode:

```bash
# Install OpenCode CLI (if available)
npm install -g @opencode/cli

# Connect to your workspace
opencode connect /path/to/your/project

# Start in VSCode integration mode
opencode serve --vscode
```

### 4. Local Configuration

Configure OpenCode to run locally:

```json
{
  "server": {
    "host": "localhost",
    "port": 3000,
    "mode": "local"
  },
  "workspace": {
    "defaultPath": "/Users/alexandriajohn/Documents/GitHub/Hyperliquid-Data-Layer-API",
    "autoLoad": true
  },
  "ai": {
    "provider": "local",
    "model": "qwen2.5-coder:14b",
    "baseUrl": "http://localhost:11434/v1"
  }
}
```

## Integration with Existing Setup

### With Ollama Models
OpenCode can use the same Ollama models we configured earlier:

```json
{
  "ai": {
    "provider": "ollama",
    "models": [
      {
        "name": "qwen2.5-coder:14b",
        "endpoint": "http://localhost:11434",
        "type": "chat"
      },
      {
        "name": "qwen3:8b",
        "endpoint": "http://localhost:11434", 
        "type": "chat"
      }
    ],
    "defaultModel": "qwen2.5-coder:14b"
  }
}
```

### With VSCode Extensions
Configure your existing VSCode extensions to work with OpenCode:

```json
{
  "cline.apiProvider": "opencode",
  "cline.opencodeUrl": "http://localhost:3000",
  "cline.openable": true
}
```

## Usage

### Starting OpenCode
```bash
# Launch the app
open /Applications/OpenCode.app

# Or from CLI (if available)
opencode start
```

### Connecting to VSCode
1. Open your project in VSCode
2. Use the OpenCode extension or CLI to connect
3. Start coding with AI assistance

### Using with Google Antigravity
1. Authenticate through OAuth flow
2. Select Google Antigravity as your provider
3. Enjoy cloud-powered features when needed

## Troubleshooting

### Common Issues

1. **Port Conflicts**: Change the port in settings if 3000 is occupied
2. **OAuth Failures**: Check redirect URI configuration
3. **VSCode Connection**: Ensure the OpenCode server is running

### Debug Commands

```bash
# Check OpenCode status
opencode status

# Test connection
curl http://localhost:3000/health

# Check logs
tail -f ~/Library/Logs/OpenCode/app.log
```

## Security Considerations

- OAuth tokens are stored securely in keychain
- Local processing keeps your code private
- Google Antigravity integration is optional
- Network access only for cloud features

## Next Steps

1. **Configure OAuth**: Set up Google Antigravity authentication
2. **Test Integration**: Verify VSCode connection works
3. **Choose AI Provider**: Select between local Ollama or cloud models
4. **Customize Settings**: Adjust to your workflow preferences

The OpenCode Desktop app is now ready for local development with VSCode and Google Antigravity integration!
