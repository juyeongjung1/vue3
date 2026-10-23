"""指定されたZoomIt 7.20の緑を #6B9E78 に変更したコピーを作成する。"""

import argparse
import hashlib
from pathlib import Path


ORIGINAL_SHA256 = "67f2e8d935b1d207c62915d7a6a8f74b2ea95ba5bc3c81b309ac39c57609f59b"
INSTRUCTION_OFFSET = 0x1ED7D
ORIGINAL_INSTRUCTION = bytes.fromhex("c7 07 00 ff 00 00")
MUTED_INSTRUCTION = bytes.fromhex("c7 07 6b 9e 78 00")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="元のZoomIt64.exe")
    parser.add_argument("output", type=Path, help="変更版の新規保存先")
    args = parser.parse_args()

    original = args.source.read_bytes()
    if hashlib.sha256(original).hexdigest() != ORIGINAL_SHA256:
        parser.error("対象のZoomIt 7.20と一致しません。ファイルは変更していません。")

    end = INSTRUCTION_OFFSET + len(ORIGINAL_INSTRUCTION)
    if original[INSTRUCTION_OFFSET:end] != ORIGINAL_INSTRUCTION:
        parser.error("緑色を指定する命令が一致しません。ファイルは変更していません。")

    modified = bytearray(original)
    modified[INSTRUCTION_OFFSET:end] = MUTED_INSTRUCTION
    # 既存ファイルを上書きせず、元の署名付き実行ファイルを保持する。
    with args.output.open("xb") as output:
        output.write(modified)
    if args.output.read_bytes() != modified:
        raise RuntimeError("保存後の検証に失敗しました。変更版を使用しないでください。")

    print(f"変更版を作成しました: {args.output}")
    print("緑: #00FF00 → #6B9E78（変更は色の即値3バイトのみ）")
    print(f"SHA256: {hashlib.sha256(modified).hexdigest()}")
    print("変更版ではMicrosoftの電子署名は無効になります。")


if __name__ == "__main__":
    main()
