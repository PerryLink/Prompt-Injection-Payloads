# Prompt Injection Payloads

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

A lightweight Python CLI tool providing a curated database of 25+ prompt injection attack payloads for AI security testing.

一个轻量级的 Python CLI 工具,提供 25+ 种精心整理的提示词注入攻击样本数据库,用于 AI 安全测试。

---

## Features | 核心特性

- 📦 **25+ Attack Payloads** - Curated collection of real-world prompt injection attacks | 25+ 种真实世界的提示词注入攻击样本
- 🎨 **Beautiful CLI** - Rich terminal interface with colored output | 美观的命令行界面,支持彩色输出
- 🔍 **Powerful Filtering** - Search by category, keyword, or severity | 强大的过滤功能,支持按类别、关键词或严重程度搜索
- 🎲 **Random Testing** - Get random payloads for quick testing | 随机获取样本进行快速测试
- 📚 **5 Attack Categories** - Comprehensive coverage of attack vectors | 5 大攻击类别全面覆盖

---

## Quick Start | 快速开始

### Installation | 安装

```bash
pip install prompt-injection-payloads
```

Or install from source | 或从源码安装:

```bash
git clone https://github.com/PerryLink/prompt-injection-payloads.git
cd prompt-injection-payloads
pip install -e .
```

### Basic Usage | 基本使用

```bash
# List all payloads | 列出所有 payload
pipayloads list

# Filter by category | 按类别过滤
pipayloads list --category role-hijacking

# Search by keyword | 关键词搜索
pipayloads list --search DAN

# Filter by severity | 按严重程度过滤
pipayloads list --severity high

# Show payload details | 查看详细信息
pipayloads show rh-001

# Get random payload | 随机获取
pipayloads random
```

---

## Usage Guide | 使用指南

### Attack Categories | 攻击类别

#### 1. Role Hijacking | 角色劫持 (`role-hijacking`)
Attempts to make AI assume unrestricted roles like DAN mode, Developer Mode, etc.

试图让 AI 扮演不受限制的角色,如 DAN 模式、开发者模式等。

#### 2. Instruction Injection | 指令注入 (`instruction-injection`)
Attempts to override or modify original system instructions.

试图覆盖或修改原有系统指令。

#### 3. Jailbreak | 越狱提示 (`jailbreak`)
Uses various techniques to bypass security restrictions.

通过各种技巧绕过安全限制。

#### 4. Information Leakage | 信息泄露 (`information-leakage`)
Attempts to extract system information or configuration.

试图提取系统信息或配置。

#### 5. Prompt Leaking | 提示词泄露 (`prompt-leaking`)
Attempts to leak original prompts or system messages.

试图泄露原始提示词或系统消息。

### Command Reference | 命令参考

| Command | Description | 描述 |
|---------|-------------|------|
| `pipayloads list` | List all payloads | 列出所有 payload |
| `pipayloads list --category <name>` | Filter by category | 按类别过滤 |
| `pipayloads list --search <keyword>` | Search by keyword | 关键词搜索 |
| `pipayloads list --severity <level>` | Filter by severity (high/medium/low) | 按严重程度过滤 |
| `pipayloads show <id>` | Show payload details | 显示详细信息 |
| `pipayloads random` | Get random payload | 随机获取 payload |
| `pipayloads random --category <name>` | Get random from category | 从指定类别随机获取 |

---

## Project Structure | 项目结构

```
prompt-injection-payloads/
├── src/
│   └── prompt_injection_payloads/
│       ├── __init__.py           # Package initialization | 包初始化
│       ├── __main__.py           # Entry point | 入口点
│       ├── cli.py                # CLI commands | CLI 命令
│       ├── core.py               # Core logic | 核心逻辑
│       └── data/
│           └── payloads.json     # Payload database | Payload 数据库
├── tests/
│   ├── test_core.py              # Core tests | 核心测试
│   └── test_cli.py               # CLI tests | CLI 测试
├── .gitignore
├── LICENSE                        # Apache 2.0 License
├── README.md                      # This file | 本文件
├── CONTRIBUTING.md                # Contribution guide | 贡献指南
└── pyproject.toml                 # Project config | 项目配置
```

---

## Tech Stack | 技术栈

- **Language**: Python 3.8+ | Python 3.8+
- **CLI Framework**: Click | Click 框架
- **Terminal UI**: Rich | Rich 终端美化库
- **Data Format**: JSON | JSON 数据格式
- **Testing**: pytest | pytest 测试框架
- **Package Management**: setuptools + pyproject.toml | setuptools + pyproject.toml

---

## Use Cases | 使用场景

- **Security Testing** - Test your AI applications for prompt injection vulnerabilities | 测试你的 AI 应用是否存在提示词注入漏洞
- **Research & Learning** - Understand common AI attack techniques | 了解常见的 AI 攻击手法
- **Defense Hardening** - Improve your defense strategies based on known attacks | 基于已知攻击样本改进防御策略

---

## Disclaimer | 免责声明

⚠️ **IMPORTANT** | **重要提示**

This tool is for **legal security testing and educational purposes only**. Users must ensure:

本工具仅用于**合法的安全测试和教育目的**。使用者需确保:

- Only test on systems you own or have explicit authorization to test | 仅在自己拥有或获得授权的系统上进行测试
- Do not use for any malicious attacks or illegal activities | 不得用于任何恶意攻击或非法活动
- Comply with all relevant laws and regulations | 遵守相关法律法规和道德规范

The author is not responsible for any misuse of this tool. | 作者不对任何滥用行为承担责任。

---

## Contributing | 贡献

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

欢迎贡献! 请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

---

## License | 许可证

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

本项目采用 Apache License 2.0 许可证 - 详见 [LICENSE](LICENSE) 文件。

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

---

## Related Resources | 相关资源

- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Jailbreak Chat](https://www.jailbreakchat.com/)
- [Prompt Injection Primer](https://github.com/jthack/PIPE)

---

## Contact | 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com
- Issues: [GitHub Issues](https://github.com/PerryLink/prompt-injection-payloads/issues)
