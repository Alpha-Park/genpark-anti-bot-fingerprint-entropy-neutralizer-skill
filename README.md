# GenPark AI Agent Skill - Anti-Bot Fingerprint Entropy Neutralizer

Validates browser fingerprints (Webdriver flags, WebGL renderer strings, OS concurrency) and synthesizes realistic overrides for headless agents.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[Browser Session Telemetry Probe] --> B[Bot Heuristic Auditor: navigator.webdriver]
    B --> C[Reference Profile Matching Windows/Mac]
    C --> D[Generate Deterministic Prototype Overrides]
    D --> E[Apply CDP Network/Runtime Interceptions]
```

## Features
- **Headless Detection Mitigation**: Eliminates automated flags like `navigator.webdriver`.
- **Zero External Dependencies**: Pure Python standard library implementation.
