# Game_Updating_Calendar

本项目会自动生成多个 **每 42 天重复一次** 的日历事件（ICS 文件），包括：

- 原神更新
- 星铁更新
- 绝区零更新

所有事件都从 **2025-11-18** 开始，每次循环 42 天。

所有 ICS 文件自动生成并发布在：https://<yourname>.github.io/game_updating_calendar/ics/

## 项目目录结构

game_updating_calendar/
│
├── events.json # 事件配置文件（你只需改这里）
├── main.py # 自动读取配置并生成 ICS
├── server.py # 用于 GitHub Actions，内容可为空
├── requirements.txt # 可为空
│
├── ics/ # 自动生成的 ICS 文件存放路径
│ ├── genshin.ics
│ ├── starrail.ics
│ └── zzz.ics
│
└── .github/workflows/
└── deploy.yml # CI/CD 自动发布配置

---

## 使用方式

启用 GitHub Pages 后，订阅链接格式为：

https://<你的GitHub用户名>.github.io/<仓库名>/ics/<事件名>.ics


示例（请替换为你的实际用户名）：

| 事件 | 订阅链接 |
|------|----------|
| 原神更新 | `https://<username>.github.io/game_updating_calendar/ics/genshin.ics` |
| 星铁更新 | `https://<username>.github.io/game_updating_calendar/ics/starrail.ics` |
| 绝区零更新 | `https://<username>.github.io/game_updating_calendar/ics/zzz.ics` |

将 ICS 链接导入到你的日历应用即可自动订阅与同步。

---

## 如何新增事件

你只需要修改 `events.json`：

```json
{
  "<name>": {
    "title": "<title>",
    "start_date": "<YYYY-mm-dd>",
    "interval": 42
  }
}
```
保存并推送到 main 分支后：

GitHub Actions 自动执行 Python 生成新的 ICS

自动发布到 GitHub Pages

新的订阅链接自动生效：

https://<username>.github.io/game_updating_calendar/ics/paint.ics
整个过程无需任何手动步骤。