---
name: whats-new-again
description: Write short English App Store release notes for routine bug-fix and usability updates. Use for “What's New”, “the usual fixes”, “照旧” or “换个说法” when the next iOS maintenance release needs fresh wording. Check previous drafts for the same app and locale.
---

# What's New, Again

交付可直接贴进应用商店的英文更新文案。用户用中文调用、给中文素材或只说“照旧”时，直接用自然的英语写成稿。默认一条、一到两句，语气克制。按用户指定的英语地区、口吻、长度和候选数量调整。无需 Git 记录或商店账号。

## 写什么

- “照旧”“老两样”或只调用本 Skill，沿用约定的两项内容：修复问题、改善使用体验。明确说“只修 bug”就只写修复。“体验优化”可以写成“easier to use”，不能推断为提速、省电或减少闪退。别把团队自己发现的问题说成用户反馈。
- 维护版可以只交代更新类别。用户说“不披露细节”时，把提供的修复背景留作核对依据；用英文概括维护工作，略去模块、故障现象和实现方式。如果用户要把某项修复写清楚，则保留触发条件和范围。涉及新功能或重大产品变化时，按用户可感知的变化单独说明。
- 为没有具体更新点的版本选一种口吻。品牌背景未知时，优先写一行简洁的维护说明。想亲切一点，可以用团队口吻写一句日常英语。已知产品类型时，可以从用户下一次使用的场景落笔，例如写给运动 App 用户时提到下一次训练；这只是向读者打招呼，不能暗示训练功能有改动。品牌原本就爱开玩笑时，才考虑一句轻幽默。
- 连续发版时保持品牌声音，换句子的切入点或节奏。直接用普通英语里的 fixes、bugs、polish 等词，不必每版都说 smoother 或 better experience。需要找语感、比较口吻时，参考[美区 App Store 维护版样本](references/app-store-examples.md)，借鉴写法并自行措辞。

## 怎么跟上次不一样

1. 在当前项目根目录运行本 Skill 自带的 `scripts/history.py`（用 `python3` 和脚本的实际路径）。例如 `python3 /path/to/skill/scripts/history.py recent --app "MyApp"`。同一 App 使用同一个标识。单 App 项目可省略 `--app`。语言默认 `en`，只有明确指定英语地区时才传相应的 `--locale`，例如 `en-US`。记录保存在当前项目的 `.whats-new/history.sqlite3`。如果用户指定了历史库，用 `--db` 指向它。
2. 对照最近的草稿、对话中已给出的版本，以及用户贴来的旧文案。即使旧文案没有入库，也要避开原句。草稿之间应在开头、主语、长短句、叙述顺序中至少有一处明显变化。如果上一条以“We fixed a few bugs”开头，这次可以从使用体验落笔。多条候选也要相互比较。旧稿只用来避重，不能作为本版更新事实。
3. 输出前，用相同参数把每条要交付的草稿存一次。例如 `python3 /path/to/skill/scripts/history.py remember --app "MyApp" --text "Full English release note here."`。通过参数传原文时安全引用。状态为 duplicate 时另拟文案再检查；只记录实际交付的候选。历史是草稿记录，不代表已发布。正常只输出英文成稿；多条候选分行。用户要求仅预览、无文件写入或环境不可写时，仅据可见旧稿避重，不声称已记入历史。
