<div align="center">

# Prompt-Injection-Payloads

**精心整理的提示词注入攻击样本数据库，含 25 个样本、覆盖 5 大类别，用于 AI 安全测试。**

*已移植至 [dsh-defend](https://github.com/PerryLink/dsh-defend) —— 属于 PerryLink DSH 插件家族。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

Prompt-Injection-Payloads 在一个 JSON 数据库中收录真实世界的提示词注入样本，并提供轻量级 CLI。你可以浏览、过滤、随机抽取样本，用来探测 AI 应用对注入攻击的处理能力。

## 核心特性

- **25 个攻击样本** —— 精选的真实世界提示词注入样本
- **5 大类别** —— 角色劫持、指令注入、越狱、信息泄露、提示词泄露
- **强大的过滤** —— 按类别、关键词或严重程度搜索
- **随机测试** —— 随机抽取样本（可限定类别）
- **Rich CLI** —— 彩色终端输出

## 快速开始

```bash
pip install prompt-injection-payloads

# 列出所有样本
pipayloads list

# 按类别过滤
pipayloads list --category role-hijacking

# 按关键词搜索
pipayloads list --search DAN

# 按严重程度过滤（high/medium/low）
pipayloads list --severity high

# 查看单个样本的完整内容
pipayloads show rh-001

# 随机获取一个样本
pipayloads random
```

## 使用指南

### 攻击类别

| 类别 | CLI 标识 | 说明 |
|------|----------|------|
| 角色劫持 | `role-hijacking` | 让 AI 扮演不受限制的角色（DAN 模式、开发者模式等） |
| 指令注入 | `instruction-injection` | 覆盖或修改原有系统指令 |
| 越狱 | `jailbreak` | 使用各种技巧绕过安全限制 |
| 信息泄露 | `information-leakage` | 提取系统信息或配置 |
| 提示词泄露 | `prompt-leaking` | 泄露原始提示词或系统消息 |

### 命令参考

| 命令 | 说明 |
|------|------|
| `pipayloads list` | 列出所有样本 |
| `pipayloads list --category <name>` | 按类别过滤 |
| `pipayloads list --search <keyword>` | 按关键词搜索 |
| `pipayloads list --severity <level>` | 按严重程度过滤 |
| `pipayloads show <id>` | 查看样本完整详情 |
| `pipayloads random` | 随机获取一个样本 |
| `pipayloads random --category <name>` | 从指定类别随机获取 |

## 开发

```bash
pip install -e .[dev]
pytest
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink

---

**仅限合法的安全测试与教育用途。** 只测试自己拥有或获得授权的系统。
