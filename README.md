# マウスぐりぐり

プログラムで自動的にマウスをぐりぐりしたり適当なキーを押下し続けるだけのプログラム

## 用途

- Google Colab のセッションが切れないようにする
- Teams のステータスを `連絡可能` で維持し、 `退席中` にならないようにする

## Windows での環境構築

```sh
# 1. 仮想環境を作成
py -3.10 -m venv .venv

# 2. 仮想環境をアクティベート
.venv\Scripts\activate.ps1

# 3. pipを最新版に更新
python -m pip install --upgrade pip setuptools

# 4. ライブラリをインストール
python -m pip install -r requirements.txt
# python -m pip install pyautogui
# python -m pip install pynput
# python -m pip install black
# python -m pip install flake8
# python -m pip install pyinstaller
```

## exe化

```sh
pyinstaller mouse_guriguri.py --onefile --noconsole
```
