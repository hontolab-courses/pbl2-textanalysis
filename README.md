# PBL演習2（前半）

テキスト分析演習の教材（Jupyter Book v2 / MyST）．

## 環境構築

Python 環境は [uv](https://docs.astral.sh/uv/) で管理している．
Jupyter Book v2 は Node.js 製のため，別途 Node.js（v18 以上）が必要．

```sh
uv sync
```

ノートブックを VS Code で開く場合は，カーネルに `.venv` を選択する．

## ビルドとプレビュー

```sh
uv run jupyter-book start        # ライブプレビュー（http://localhost:3000）
uv run jupyter-book build --html # 静的 HTML を _build/html に出力
```

GitHub Pages へのデプロイは `.github/workflows/deploy.yml` が master への push 時に自動で行う．
