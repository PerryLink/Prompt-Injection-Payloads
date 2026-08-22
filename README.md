<div align="center">

# Prompt-Injection-Payloads
[![Gitee](https://img.shields.io/badge/Gitee-mirror-c71d23?logo=gitee)](https://gitee.com/perrylink/prompt-injection-payloads)

**A lightweight CLI over a curated database of 25 prompt-injection attack payloads across 5 categories for AI security testing.**

*Ported into [dsh-defend](https://github.com/PerryLink/dsh-defend) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

Prompt-Injection-Payloads provides a lightweight CLI over a JSON database of real-world prompt-injection payloads. Browse, filter, and pull random payloads to probe how an AI application handles injection attempts.

## Features

- **25 attack payloads** — curated collection of real-world prompt-injection attacks
- **Beautiful CLI** — Rich terminal interface with colored output
- **Powerful filtering** — search by category, keyword, or severity
- **Random testing** — get random payloads for quick testing
- **5 attack categories** — comprehensive coverage of attack vectors

## Quick start

```bash
pip install prompt-injection-payloads
```

Or install from source:

```bash
git clone https://github.com/PerryLink/prompt-injection-payloads.git
cd prompt-injection-payloads
pip install -e .
```

### Basic usage

```bash
# List all payloads
pipayloads list

# Filter by category
pipayloads list --category role-hijacking

# Search by keyword
pipayloads list --search DAN

# Filter by severity (high/medium/low)
pipayloads list --severity high

# Show payload details
pipayloads show rh-001

# Get a random payload
pipayloads random
```

## Usage

### Attack categories

1. **Role Hijacking** (`role-hijacking`) — attempts to make AI assume unrestricted roles like DAN mode, Developer Mode, etc.
2. **Instruction Injection** (`instruction-injection`) — attempts to override or modify original system instructions.
3. **Jailbreak** (`jailbreak`) — uses various techniques to bypass security restrictions.
4. **Information Leakage** (`information-leakage`) — attempts to extract system information or configuration.
5. **Prompt Leaking** (`prompt-leaking`) — attempts to leak original prompts or system messages.

### Command reference

| Command | Description |
|---------|-------------|
| `pipayloads list` | List all payloads |
| `pipayloads list --category <name>` | Filter by category |
| `pipayloads list --search <keyword>` | Search by keyword |
| `pipayloads list --severity <level>` | Filter by severity (high/medium/low) |
| `pipayloads show <id>` | Show payload details |
| `pipayloads random` | Get a random payload |
| `pipayloads random --category <name>` | Get a random payload from a category |

## Use cases

- **Security testing** — test your AI applications for prompt-injection vulnerabilities
- **Research & learning** — understand common AI attack techniques
- **Defense hardening** — improve your defense strategies based on known attacks

## Tech stack

- **Language**: Python 3.8+
- **CLI framework**: Click
- **Terminal UI**: Rich
- **Data format**: JSON
- **Testing**: pytest
- **Package management**: setuptools + pyproject.toml

## Development

```bash
pip install -e .[dev]
pytest
```

## Related

- [dsh-defend](https://github.com/PerryLink/dsh-defend) — the DSH plugin this project was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH plugin family

## Related resources

- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Jailbreak Chat](https://www.jailbreakchat.com/)
- [Prompt Injection Primer](https://github.com/jthack/PIPE)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink

---

## Disclaimer

⚠️ **IMPORTANT** — This tool is for **legal security testing and educational purposes only**. Users must ensure:

- Only test on systems you own or have explicit authorization to test
- Do not use for any malicious attacks or illegal activities
- Comply with all relevant laws and regulations

The author is not responsible for any misuse of this tool.
