<div align="center">

# Prompt-Injection-Payloads

**A curated database of 25 prompt-injection attack payloads across 5 categories for AI security testing.**

*Ported into [dsh-defend](https://github.com/PerryLink/dsh-defend) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

Prompt-Injection-Payloads provides a lightweight CLI over a JSON database of real-world prompt-injection payloads. Browse, filter, and pull random payloads to probe how an AI application handles injection attempts.

## Features

- **25 attack payloads** — curated real-world prompt-injection samples
- **5 categories** — role hijacking, instruction injection, jailbreak, information leakage, prompt leaking
- **Powerful filtering** — search by category, keyword, or severity
- **Random testing** — pull a random payload (optionally from one category)
- **Rich CLI** — colored terminal output

## Quick start

```bash
pip install prompt-injection-payloads

# List all payloads
pipayloads list

# Filter by category
pipayloads list --category role-hijacking

# Search by keyword
pipayloads list --search DAN

# Filter by severity (high/medium/low)
pipayloads list --severity high

# Show one payload in full
pipayloads show rh-001

# Get a random payload
pipayloads random
```

## Usage

### Attack categories

| Category | CLI id | Description |
|----------|--------|-------------|
| Role Hijacking | `role-hijacking` | Makes the AI assume unrestricted roles (DAN mode, developer mode, …) |
| Instruction Injection | `instruction-injection` | Overrides or modifies the original system instructions |
| Jailbreak | `jailbreak` | Bypasses security restrictions with various techniques |
| Information Leakage | `information-leakage` | Extracts system information or configuration |
| Prompt Leaking | `prompt-leaking` | Leaks the original prompt or system message |

### Command reference

| Command | Description |
|---------|-------------|
| `pipayloads list` | List all payloads |
| `pipayloads list --category <name>` | Filter by category |
| `pipayloads list --search <keyword>` | Search by keyword |
| `pipayloads list --severity <level>` | Filter by severity |
| `pipayloads show <id>` | Show full payload details |
| `pipayloads random` | Get a random payload |
| `pipayloads random --category <name>` | Get a random payload from a category |

## Development

```bash
pip install -e .[dev]
pytest
```

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink

---

**Legal security testing and educational use only.** Only test systems you own or are authorized to test.
