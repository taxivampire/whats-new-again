# What's New, Again?

第十次发维护版，怎么用英语写「修复了 bug，优化了体验」？

给需要自己写 App Store 更新说明的独立开发者做的 Codex Skill。你可以用中文说「照旧」，它会参考同一个 App 最近写过的稿子，给一条能直接粘贴的英文 What’s New。

[English](README.md) · [6 款 App 的真实文案对照](references/app-store-examples.md)

| 同一个 App 的三次维护版 | 实际生成的英文稿 |
| --- | --- |
| 第一版 | We fixed a few bugs and made the app a little easier to use. |
| 下一版 | A few bug fixes and a little polish. |
| 再下一版 | This update smooths out some rough edges and fixes a handful of bugs. |

安装命令需要 Node.js，本地草稿历史需要 Python 3。在你写发版说明的项目目录里安装：

```sh
npx skills add taxivampire/whats-new-again --skill whats-new-again --agent codex
```

在同一项目打开新的 Codex 聊天，输入：

```text
$whats-new-again 照旧。
```

只修了 bug，可以直接说「这次只写修复」。有具体改动要告诉用户，就写明触发场景。只想试试，可以加「仅预览」，这条草稿就不会存进历史。

历史由 Python 3 保存在项目的 `.whats-new/history.sqlite3`。它按 App 和语言读取最近八条稿子避开相似句式，也会检查全部历史是否出现过相同措辞。如果一个目录里管理多个 App，每次带上同一个 App 名称即可。
