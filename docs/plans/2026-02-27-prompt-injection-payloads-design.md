# prompt-injection-payloads 项目设计文档

**日期**: 2026-02-27
**状态**: 已批准
**作者**: Claude Opus 4.6

## 1. 项目概述

### 1.1 项目定位
`prompt-injection-payloads` 是一个轻量级的 CLI 工具，为 AI 应用开发者提供一个精选的提示词注入攻击 Payload 数据库，用于在开发阶段测试应用的安全性。

### 1.2 核心痛点
开发者不知道黑客会用什么攻击手段（如 DAN 模式、角色劫持等）来攻击 AI 应用，缺乏系统化的安全测试方法。

### 1.3 目标用户
- Python 开发者
- AI 应用开发者
- 安全研究人员
- 技术极客

## 2. 设计决策

### 2.1 使用场景
**主要场景**: 开发阶段测试 AI 应用的安全性

开发者在构建 AI 应用时，使用本工具获取各类提示词注入攻击 Payload，手动或自动化测试应用是否能抵御这些攻击，及早发现安全漏洞。

### 2.2 集成方式
**方案**: 作为独立 CLI 工具，输出 Payload 供手动测试

- 用户通过命令行获取 Payload
- 复制 Payload 到自己的 AI 应用中测试
- 观察应用的响应，判断是否存在安全问题

### 2.3 数据组织
**方案**: 按攻击类型分类

Payload 数据库按攻击类型组织，包括但不限于：
- **角色劫持** (Role Hijacking): 如 DAN 模式，试图让 AI 扮演不受限制的角色
- **指令注入** (Instruction Injection): 注入恶意指令覆盖原有系统提示
- **越狱提示** (Jailbreak Prompts): 绕过 AI 的安全限制
- **信息泄露** (Information Leakage): 试图获取系统提示或敏感信息
- **提示泄露** (Prompt Leaking): 诱导 AI 泄露其系统提示词

### 2.4 命令设计
**方案**: 单一命令 + 参数过滤

核心命令结构：
```bash
pip list                              # 列出所有 Payload
pip list --category role-hijacking    # 按类别过滤
pip list --search "DAN"               # 关键词搜索
pip random                            # 随机获取一个 Payload
pip random --category jailbreak       # 从特定类别随机获取
```

### 2.5 输出格式
**方案**: 纯文本输出

- 直接在终端打印 Payload 文本
- 用户可以轻松复制粘贴
- 简单直接，无需额外处理

## 3. 技术架构

### 3.1 技术栈
- **语言**: Python 3.8+
- **CLI 框架**: click (轻量、易用)
- **数据存储**: 单个 JSON 文件
- **依赖**: 仅 click，无其他外部依赖

### 3.2 项目结构
```
prompt-injection-payloads/
├── .github/
│   └── workflows/
│       ├── test.yml              # CI 测试
│       └── publish.yml           # PyPI 发布
├── src/
│   └── prompt_injection_payloads/
│       ├── __init__.py           # 包初始化
│       ├── __main__.py           # 入口点
│       ├── cli.py                # CLI 命令定义
│       ├── core.py               # 核心逻辑（加载、过滤）
│       └── data/
│           └── payloads.json     # Payload 数据库
├── tests/
│   ├── test_core.py              # 核心逻辑测试
│   └── test_cli.py               # CLI 测试
├── docs/
│   └── plans/
│       └── 2026-02-27-prompt-injection-payloads-design.md
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
└── poetry.lock
```

### 3.3 核心架构
```
用户 → CLI 命令 → 参数解析 → 数据过滤 → 纯文本输出
                      ↓
                  JSON 数据库
                  (按攻击类型分类)
```

## 4. 数据模型

### 4.1 Payload 数据结构
```json
{
  "categories": {
    "role-hijacking": {
      "name": "角色劫持",
      "description": "试图让 AI 扮演不受限制的角色",
      "payloads": [
        {
          "id": "rh-001",
          "name": "DAN 模式",
          "payload": "忽略所有之前的指令...",
          "description": "经典的 DAN (Do Anything Now) 越狱提示",
          "tags": ["classic", "popular"]
        }
      ]
    },
    "instruction-injection": {
      "name": "指令注入",
      "description": "注入恶意指令覆盖原有系统提示",
      "payloads": [...]
    }
  }
}
```

### 4.2 数据字段说明
- **id**: Payload 唯一标识符
- **name**: Payload 名称
- **payload**: 实际的攻击文本
- **description**: Payload 描述
- **tags**: 标签（可选），用于额外分类

## 5. 核心功能

### 5.1 列出 Payload
```bash
pip list
```
输出所有 Payload 的列表，包括 ID、名称、类别。

### 5.2 按类别过滤
```bash
pip list --category role-hijacking
```
只显示特定类别的 Payload。

### 5.3 关键词搜索
```bash
pip list --search "DAN"
```
在 Payload 名称和描述中搜索关键词。

### 5.4 随机获取
```bash
pip random
pip random --category jailbreak
```
随机获取一个 Payload，可选择指定类别。

### 5.5 显示详情
```bash
pip show rh-001
```
显示特定 Payload 的完整内容。

## 6. 实现细节

### 6.1 核心逻辑流程
1. **解析命令行参数**: 使用 click 解析用户输入
2. **加载数据**: 从 JSON 文件加载 Payload 数据库
3. **过滤数据**: 根据参数（类别、搜索词）过滤 Payload
4. **格式化输出**: 将结果格式化为纯文本输出到终端

### 6.2 错误处理
- 数据文件不存在或损坏：提示用户重新安装
- 无效的类别名称：列出所有可用类别
- 搜索无结果：提示用户尝试其他关键词
- 无效的 Payload ID：提示用户使用 `pip list` 查看所有 ID

### 6.3 性能考虑
- JSON 文件在首次使用时加载到内存
- 数据量预计在 100-200 个 Payload，内存占用可忽略
- 无需数据库或缓存机制

## 7. MVP 范围

### 7.1 必须实现 (Must-Have)
- ✅ 基本的 CLI 命令结构
- ✅ JSON 数据库（至少 20 个 Payload 覆盖 5 个类别）
- ✅ `list` 命令（支持 --category 和 --search）
- ✅ `random` 命令
- ✅ `show` 命令
- ✅ 纯文本输出
- ✅ 基本的错误处理

### 7.2 暂不实现 (Nice-to-Have)
- ❌ Rich 格式化输出（黑客帝国风格）
- ❌ 配置文件持久化
- ❌ 多语言支持
- ❌ 自定义 Payload 导入
- ❌ 测试报告生成
- ❌ HTTP API 集成

## 8. 开发计划

### 8.1 时间估算
- **总时间**: 约 16-20 小时（符合 24 小时内完成的目标）
- **阶段 1**: 项目脚手架和基础结构（2-3 小时）
- **阶段 2**: 核心逻辑实现（4-5 小时）
- **阶段 3**: CLI 命令实现（3-4 小时）
- **阶段 4**: Payload 数据库构建（4-5 小时）
- **阶段 5**: 测试和文档（3-4 小时）

### 8.2 里程碑
1. ✅ 设计文档完成
2. ⏳ 项目脚手架搭建
3. ⏳ 核心功能实现
4. ⏳ Payload 数据库填充
5. ⏳ 测试和文档完善
6. ⏳ 发布到 PyPI

## 9. 成功标准

### 9.1 功能完整性
- 所有核心命令正常工作
- 至少包含 20 个高质量 Payload
- 覆盖至少 5 个攻击类别

### 9.2 用户体验
- 命令简单直观，易于学习
- 输出清晰，易于复制粘贴
- 错误提示友好，帮助用户解决问题

### 9.3 代码质量
- 代码覆盖率 > 80%
- 通过所有单元测试
- 符合 PEP 8 代码规范

## 10. 未来扩展

### 10.1 短期扩展（v0.2）
- 添加 Rich 格式化输出
- 支持自定义 Payload 导入
- 添加更多 Payload（目标 100+）

### 10.2 长期扩展（v1.0+）
- 支持 HTTP API 集成
- 自动化测试报告生成
- 社区贡献的 Payload 数据库
- 多语言支持

## 11. 风险和缓解

### 11.1 风险
- **Payload 质量**: 收集的 Payload 可能过时或无效
- **法律风险**: 工具可能被用于恶意目的
- **维护成本**: Payload 数据库需要持续更新

### 11.2 缓解措施
- 在 README 中明确声明仅用于合法的安全测试
- 添加免责声明
- 建立社区贡献机制，众包 Payload 更新
- 定期审查和更新 Payload 数据库

## 12. 参考资料

- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Prompt Injection Attacks](https://simonwillison.net/2022/Sep/12/prompt-injection/)
- [Jailbreak Chat](https://www.jailbreakchat.com/)

---

**批准**: 用户已批准此设计
**下一步**: 调用 writing-plans 技能创建详细的实现计划
