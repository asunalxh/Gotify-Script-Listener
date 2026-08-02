# Gotify CLI

基于 [Gotify](https://gotify.net) 的命令行通知工具，用于监听脚本执行，在启动和结束时自动推送消息，支持正则捕获输出实时发送通知。

> 本项目由 AI Agent 编写。

## 安装

```bash
./gotify install          # 安装到 ~/.local/bin（默认）
./gotify install --system # 安装到 /usr/local/bin
```

## 快速开始

```bash
gotify init --global      # 创建全局配置，输入 Server URL 和 App Token
gotify "部署完成"           # 发送一条消息
```

## 使用方式

```bash
# 发送消息
gotify <消息内容>
echo "hello" | gotify

# 监听命令执行
gotify run <命令...>
gotify --global run <命令...>

# 失败自动重启（最多重试 N 次，默认 3）
gotify run --restart --retries 3 make build

# 结束后自动关机
gotify run --shutdown make build

# 配置管理
gotify config                     # 查看当前配置
gotify config <key>               # 查看单项
gotify config <key> <value>       # 设置项目配置
gotify --global config <key> <v>  # 设置全局配置
```

## 通知行为

发起 `run` 时，共发送三次通知：

| 时机 | 标题示例 | 内容 |
|------|---------|------|
| 启动 | `make started` | Command started: make build |
| 重启 | `make restarting` | make failed (exit: 1), restarting (attempt 1/3) |
| 完成 | `make completed` | make build finished |
| 失败 | `make failed (exit: 1)` | make build (exit: 1) |

## 正则捕获

在配置文件中添加 `watch` 字段，命令输出匹配时实时发送通知：

```json
{
    "server_url": "https://gotify.example.com",
    "app_token": "your-token",
    "priority": 5,
    "title": "my-project",
    "watch": ["ERROR", "FAIL", "panic"]
}
```

匹配到 `ERROR` 时立即推送匹配行。

## 配置文件

| 路径 | 用途 |
|------|------|
| `~/.config/gotify/config.json` | 全局配置 |
| `.gotify.json` | 项目配置 |

`--global` 标志指定操作全局配置，不加则操作项目配置，两者不合并。

## 卸载

```bash
gotify uninstall
```
