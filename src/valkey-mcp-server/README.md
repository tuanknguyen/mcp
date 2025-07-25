# Amazon ElastiCache/MemoryDB Valkey MCP Server

An AWS Labs Model Context Protocol (MCP) server for Amazon ElastiCache [Valkey](https://valkey.io/) datastores.

## Features
This MCP server provides tools to operate on Valkey data types. For example, it allows an agent to operate with Valkey Strings using commands such as SET, SETRANGE, GET, GETRANGE, APPEND, INCREMENT and more.

### Supported Data Types
- `Strings`- Store, retrieve, append, increment, decrement, length and more.
- `Lists`- Manage List collections with push/pop operations.
- `Sets and Sorted Sets`- Store and retrieve items from Sets.
- `Hashes`- Store and retrieve items in Hashes. Check for existence of items in a hash, increment item values in a Hash, and more.
- `Streams`- Store, retrieve, trim items in Streams.
- `Bitmaps`- Bitmaps let you perform bitwise operations on strings.
- `JSONs`- Store and retrieve JSON documents with path-based access.
- `HyperLogLog`- Store and count items in HyperLogs.

### Advanced Features
- **Cluster Support**: Support for standalone and clustered Valkey deployments.
- **SSL/TLS Security**: Configure secure connections using SSL/TLS.
- **Connection Pooling**: Pools connections by default to enable efficient connection management.
- **Readonly Mode**: Prevent write operations to ensure data safety.

## Prerequisites

1. Install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/) or the [GitHub README](https://github.com/astral-sh/uv#installation)
2. Install Python using `uv python install 3.10`
3. Access to a Valkey datastore.
4. For instructions to connect to an Amazon ElastiCache/MemoryDB Valkey datastore [click here](https://github.com/awslabs/mcp/blob/main/src/valkey-mcp-server/ELASTICACHECONNECT.md).


## Installation

| Cursor | VS Code |
|:------:|:-------:|
| [![Install MCP Server](https://cursor.com/deeplink/mcp-install-light.svg)](https://cursor.com/install-mcp?name=awslabs.valkey-mcp-server&config=eyJjb21tYW5kIjoidXZ4IGF3c2xhYnMudmFsa2V5LW1jcC1zZXJ2ZXJAbGF0ZXN0IiwiZW52Ijp7IlZBTEtFWV9IT1NUIjoiMTI3LjAuMC4xIiwiVkFMS0VZX1BPUlQiOiI2Mzc5IiwiRkFTVE1DUF9MT0dfTEVWRUwiOiJFUlJPUiJ9LCJhdXRvQXBwcm92ZSI6W10sImRpc2FibGVkIjpmYWxzZX0%3D) | [![Install on VS Code](https://img.shields.io/badge/Install_on-VS_Code-FF9900?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=Valkey%20MCP%20Server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.valkey-mcp-server%40latest%22%5D%2C%22env%22%3A%7B%22VALKEY_HOST%22%3A%22127.0.0.1%22%2C%22VALKEY_PORT%22%3A%226379%22%2C%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%2C%22autoApprove%22%3A%5B%5D%2C%22disabled%22%3Afalse%7D) |

Here are some ways you can work with MCP across AWS tools (e.g., for Amazon Q Developer CLI MCP, `~/.aws/amazonq/mcp.json`):

```json
{
  "mcpServers": {
    "awslabs.valkey-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.valkey-mcp-server@latest"
      ],
      "env": {
        "VALKEY_HOST": "127.0.0.1",
        "VALKEY_PORT": "6379",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    }
  }
}
```

To run in readonly mode:

```json
{
  "mcpServers": {
    "awslabs.valkey-mcp-server": {
      "command": "uvx",
      "args": [
        "awslabs.valkey-mcp-server@latest",
        "--readonly"
      ],
      "env": {
        "VALKEY_HOST": "127.0.0.1",
        "VALKEY_PORT": "6379",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "autoApprove": [],
      "disabled": false
    }
  }
}
```

Or using Docker after a successful `docker build -t awslabs/valkey-mcp-server .`:

```json
{
  "mcpServers": {
    "awslabs.valkey-mcp-server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "--interactive",
        "--env",
        "FASTMCP_LOG_LEVEL=ERROR",
        "--env",
        "VALKEY_HOST=127.0.0.1",
        "--env",
        "VALKEY_PORT=6379",
        "awslabs/valkey-mcp-server:latest"
      ],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

To run in readonly mode with Docker:

```json
{
  "mcpServers": {
    "awslabs.valkey-mcp-server": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "--interactive",
        "--env",
        "FASTMCP_LOG_LEVEL=ERROR",
        "--env",
        "VALKEY_HOST=127.0.0.1",
        "--env",
        "VALKEY_PORT=6379",
        "awslabs/valkey-mcp-server:latest",
        "--readonly"
      ],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Configuration

The server can be configured using the following environment variables:

| Name | Description | Default Value |
|------|-------------|---------------|
| `VALKEY_HOST` | ElastiCache Primary Endpoint or MemoryDB Cluster Endpoint or Valkey IP or hostname | `"127.0.0.1"` |
| `VALKEY_PORT` | Valkey port | `6379` |
| `VALKEY_USERNAME` | Default database username | `None` |
| `VALKEY_PWD` | Default database password | `""` |
| `VALKEY_USE_SSL` | Enables or disables SSL/TLS | `False` |
| `VALKEY_CA_PATH` | CA certificate for verifying server | `None` |
| `VALKEY_SSL_KEYFILE` | Client's private key file | `None` |
| `VALKEY_SSL_CERTFILE` | Client's certificate file | `None` |
| `VALKEY_CERT_REQS` | Server certificate verification | `"required"` |
| `VALKEY_CA_CERTS` | Path to trusted CA certificates | `None` |
| `VALKEY_CLUSTER_MODE` | Enable Valkey Cluster mode | `False` |

## Example Usage

Here are some example natural language queries that the server can handle:

```
"Store user profile data in a hash"
"Add this event to the activity stream"
"Cache API response for 5 minutes"
"Store JSON document with nested fields"
"Add score 100 to user123 in leaderboard"
"Get all members of the admins set"
```

## Development

### Running Tests
```bash
uv venv
source .venv/bin/activate
uv sync
uv run --frozen pytest
```

### Building Docker Image
```bash
docker build -t awslabs/valkey-mcp-server .
```

### Running Docker Container
```bash
docker run -p 8080:8080 \
  -e VALKEY_HOST=host.docker.internal \
  -e VALKEY_PORT=6379 \
  awslabs/valkey-mcp-server
```

To run in readonly mode:
```bash
docker run -p 8080:8080 \
  -e VALKEY_HOST=host.docker.internal \
  -e VALKEY_PORT=6379 \
  awslabs/valkey-mcp-server --readonly
```
