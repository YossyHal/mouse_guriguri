import math

import pyautogui
from pynput import keyboard


class Main:
    def __init__(self):
        # ディスプレイのサイズを取得
        screenWidth, screenHeight = pyautogui.size()

        # マウスカーソルを画面の真ん中に移動
        self.x0, self.y0 = screenWidth // 2, screenHeight // 2
        pyautogui.moveTo(self.x0, self.y0)

        # 円の半径を設定
        self.radius = min(screenWidth, screenHeight) // 8

        # キーが入力されるまでプログラムを動かし続ける
        self.is_continue = True

    def run(self):
        # キーボードの入力を監視するオブジェクトを作成
        listener = keyboard.Listener(on_release=self.on_release)
        listener.start()

        # 円を描く軌道でマウスカーソルを動かし続けるループ処理
        while self.is_continue:
            self.move_around_circle()

        # キーが入力されたら止める
        listener.join()

    # 円を描くためにマウスカーソルを移動させる関数を定義
    def move_around_circle(self):
        for degree in range(0, 360, 30):
            # 度数からラジアンに変換
            radian = math.radians(degree)

            # マウスカーソルの座標を計算
            x = int(self.x0 + self.radius * math.cos(radian))
            y = int(self.y0 + self.radius * math.sin(radian))

            # マウスカーソルを移動
            pyautogui.moveTo(x, y)

            # マウス操作だけだとTeamsが離席状態になってしまうので、左Ctrlキーを押下する
            pyautogui.press("ctrlleft")

            # キーが入力されていたらループを止める
            if not self.is_continue:
                return

    def on_release(self, key):
        if key and key != keyboard.Key.ctrl_l:
            print(f"{key} released... STOP!!!!!!!!!!!")
            self.is_continue = False
            return False


if __name__ == "__main__":
    Main().run()
