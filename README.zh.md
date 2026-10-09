<div align="center">

# Prompt-Injection-Payloads

**轻量级 CLI 工具，内置 25 个提示词注入攻击样本数据库、覆盖 5 大类别，用于 AI 安全测试。**

*已移植至 [dsh-defend](https://github.com/PerryLink/dsh-defend) —— 属于 PerryLink DSH 插件家族。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

Prompt-Injection-Payloads 在一个 JSON 数据库中收录真实世界的提示词注入样本，并提供轻量级 CLI。你可以浏览、过滤、随机抽取样本，用来探测 AI 应用对注入攻击的处理能力。

## 核心特性

- **25 个攻击样本** —— 精选的真实世界提示词注入攻击样本
- **美观的 CLI** —— Rich 终端界面，支持彩色输出
- **强大的过滤** —— 按类别、关键词或严重程度搜索
- **随机测试** —— 随机获取样本进行快速测试
- **5 大攻击类别** —— 全面覆盖攻击向量

## 快速开始

```bash
pip install "git+https://github.com/PerryLink/Prompt-Injection-Payloads.git"
# （PyPI 未发布，源码直装）
```

或从源码安装：

```bash
git clone https://github.com/PerryLink/prompt-injection-payloads.git
cd prompt-injection-payloads
pip install -e .
```

### 基本使用

```bash
# 列出所有样本
pipayloads list

# 按类别过滤
pipayloads list --category role-hijacking

# 按关键词搜索
pipayloads list --search DAN

# 按严重程度过滤（high/medium/low）
pipayloads list --severity high

# 查看样本详情
pipayloads show rh-001

# 随机获取一个样本
pipayloads random
```

## 使用指南

### 攻击类别

1. **角色劫持**（`role-hijacking`）—— 试图让 AI 扮演不受限制的角色，如 DAN 模式、开发者模式等。
2. **指令注入**（`instruction-injection`）—— 试图覆盖或修改原有系统指令。
3. **越狱提示**（`jailbreak`）—— 通过各种技巧绕过安全限制。
4. **信息泄露**（`information-leakage`）—— 试图提取系统信息或配置。
5. **提示词泄露**（`prompt-leaking`）—— 试图泄露原始提示词或系统消息。

### 命令参考

| 命令 | 说明 |
|------|------|
| `pipayloads list` | 列出所有样本 |
| `pipayloads list --category <name>` | 按类别过滤 |
| `pipayloads list --search <keyword>` | 按关键词搜索 |
| `pipayloads list --severity <level>` | 按严重程度过滤（high/medium/low） |
| `pipayloads show <id>` | 查看样本详情 |
| `pipayloads random` | 随机获取一个样本 |
| `pipayloads random --category <name>` | 从指定类别随机获取 |

## 使用场景

- **安全测试** —— 测试你的 AI 应用是否存在提示词注入漏洞
- **研究学习** —— 了解常见的 AI 攻击手法
- **防御加固** —— 基于已知攻击样本改进防御策略

## 技术栈

- **开发语言**：Python 3.8+
- **CLI 框架**：Click
- **终端界面**：Rich
- **数据格式**：JSON
- **测试框架**：pytest
- **包管理**：setuptools + pyproject.toml

## 开发

```bash
pip install -e .[dev]
pytest
```

## 相关项目

- [dsh-defend](https://github.com/PerryLink/dsh-defend) —— 本项目被移植进的 DSH 插件
- [PerryLink](https://github.com/PerryLink) —— PerryLink DSH 插件家族

## 相关资源

- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Jailbreak Chat](https://www.jailbreakchat.com/)
- [Prompt Injection Primer](https://github.com/jthack/PIPE)

## 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink

---

## 免责声明

⚠️ **重要提示** —— 本工具仅用于**合法的安全测试和教育目的**。使用者需确保：

- 仅在自己拥有或获得明确授权的系统上进行测试
- 不得用于任何恶意攻击或非法活动
- 遵守所有相关法律法规

作者不对任何滥用行为承担责任。
