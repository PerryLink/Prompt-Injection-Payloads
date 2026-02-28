# Contributing to Prompt Injection Payloads

Thank you for your interest in contributing to this project!

感谢你对本项目的关注!

---

## Project Status | 项目状态

This is currently a **personal maintenance project** by [Chance Dean](https://github.com/PerryLink). While contributions are welcome, please note that response times may vary.

这是一个由 [Chance Dean](https://github.com/PerryLink) **个人维护的项目**。虽然欢迎贡献,但请注意响应时间可能会有所不同。

---

## How to Report Issues | 如何报告问题

If you find a bug or have a feature request, please:

如果你发现了 bug 或有功能建议,请:

1. **Check existing issues** - Search to see if the issue has already been reported | 检查现有 issue - 搜索是否已有人报告过
2. **Create a new issue** - Use the GitHub issue tracker | 创建新 issue - 使用 GitHub issue 追踪器
3. **Provide details** - Include: | 提供详细信息 - 包括:
   - Clear description of the problem | 问题的清晰描述
   - Steps to reproduce | 重现步骤
   - Expected vs actual behavior | 期望行为 vs 实际行为
   - Python version and OS | Python 版本和操作系统
   - Error messages or logs | 错误信息或日志

---

## Development Environment Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python 3.8 or higher | Python 3.8 或更高版本
- Git
- pip

### Setup Steps | 搭建步骤

1. **Fork and clone the repository** | Fork 并克隆仓库

```bash
git clone https://github.com/YOUR_USERNAME/prompt-injection-payloads.git
cd prompt-injection-payloads
```

2. **Create a virtual environment** | 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies** | 安装依赖

```bash
pip install -e ".[dev]"
```

4. **Run tests** | 运行测试

```bash
pytest tests/ -v
```

---

## Code Standards | 代码规范

### Style Guide | 代码风格

This project follows **PEP 8** - the official Python style guide.

本项目遵循 **PEP 8** - Python 官方代码风格指南。

Key points | 关键要点:

- Use 4 spaces for indentation (no tabs) | 使用 4 个空格缩进(不使用 tab)
- Maximum line length: 88 characters | 最大行长度: 88 字符
- Use descriptive variable names | 使用描述性的变量名
- Add docstrings for functions and classes | 为函数和类添加文档字符串
- Keep functions focused and small | 保持函数专注和简洁

### Testing | 测试

- Write tests for new features | 为新功能编写测试
- Ensure all tests pass before submitting PR | 提交 PR 前确保所有测试通过
- Aim for good test coverage | 追求良好的测试覆盖率

```bash
# Run tests with coverage
pytest tests/ -v --cov=src/prompt_injection_payloads
```

---

## Pull Request Process | 提交 Pull Request 流程

### Before Submitting | 提交前

1. **Create a feature branch** | 创建功能分支

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes** | 进行修改
   - Follow code standards | 遵循代码规范
   - Add tests if applicable | 如适用,添加测试
   - Update documentation | 更新文档

3. **Test your changes** | 测试你的修改

```bash
pytest tests/ -v
```

4. **Commit your changes** | 提交你的修改

```bash
git add .
git commit -m "feat: add new feature description"
```

Use conventional commit messages | 使用约定式提交信息:
- `feat:` - New feature | 新功能
- `fix:` - Bug fix | Bug 修复
- `docs:` - Documentation changes | 文档修改
- `test:` - Test changes | 测试修改
- `refactor:` - Code refactoring | 代码重构

### Submitting | 提交

1. **Push to your fork** | 推送到你的 fork

```bash
git push origin feature/your-feature-name
```

2. **Create a Pull Request** | 创建 Pull Request
   - Go to the original repository | 前往原始仓库
   - Click "New Pull Request" | 点击 "New Pull Request"
   - Select your branch | 选择你的分支
   - Fill in the PR template | 填写 PR 模板

3. **PR Description should include** | PR 描述应包括:
   - What changes were made | 做了什么修改
   - Why these changes are needed | 为什么需要这些修改
   - How to test the changes | 如何测试这些修改
   - Related issue numbers (if any) | 相关 issue 编号(如有)

---

## Adding New Payloads | 添加新 Payload

To contribute new attack payloads | 贡献新的攻击 payload:

1. **Edit the data file** | 编辑数据文件
   - File location: `src/prompt_injection_payloads/data/payloads.json`
   - 文件位置: `src/prompt_injection_payloads/data/payloads.json`

2. **Follow the JSON schema** | 遵循 JSON 格式

```json
{
  "id": "xx-001",
  "name": "Attack Name",
  "payload": "The actual attack text...",
  "description": "Detailed description of what this attack does",
  "tags": ["tag1", "tag2"],
  "severity": "high|medium|low",
  "references": ["https://source-url.com"]
}
```

3. **Ensure quality** | 确保质量
   - Payload must be real and tested | Payload 必须真实且经过测试
   - Include clear description | 包含清晰的描述
   - Add relevant tags | 添加相关标签
   - Provide source references | 提供来源参考

4. **Test the addition** | 测试添加

```bash
python -m prompt_injection_payloads list
python -m prompt_injection_payloads show xx-001
```

---

## Code Review Process | 代码审查流程

1. Maintainer will review your PR | 维护者将审查你的 PR
2. May request changes or clarifications | 可能会要求修改或澄清
3. Once approved, PR will be merged | 一旦批准,PR 将被合并
4. Your contribution will be acknowledged | 你的贡献将被认可

---

## Questions? | 有问题?

Feel free to reach out | 随时联系:

- **GitHub Issues**: For bugs and feature requests | 用于 bug 和功能请求
- **Email**: novelnexusai@outlook.com
- **GitHub**: [@PerryLink](https://github.com/PerryLink)

---

## License | 许可证

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

通过贡献,你同意你的贡献将在 Apache License 2.0 下授权。

---

Thank you for contributing! | 感谢你的贡献!
