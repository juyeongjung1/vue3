"""コミット済みのVue教材とAPIから配布用ZIPを作成する。"""

import argparse
import io
from pathlib import Path
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]
LFS_HEADER = b"version https://git-lfs.github.com/spec/v1\n"


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, stdout=subprocess.PIPE, check=True
    ).stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="origin/main", help="配布元のコミット（既定: origin/main）")
    parser.add_argument("--output", type=Path, help="作成するZIPのパス（既存ファイルは上書きしない）")
    args = parser.parse_args()
    revision = git("rev-parse", "--verify", f"{args.ref}^{{commit}}").decode().strip()
    output = args.output or ROOT / "distribution" / f"vue3-course-{revision[:12]}.zip"

    raw_archive = git(
        "-c", "filter.lfs.process=", "-c", "filter.lfs.smudge=",
        "-c", "filter.lfs.required=false", "archive", "--format=zip", revision
    )
    with zipfile.ZipFile(io.BytesIO(raw_archive)) as source:
        projects = {
            Path(name).parts[0]
            for name in source.namelist()
            if len(Path(name).parts) == 2 and name.endswith("/package.json")
        }
        root_files = {"README.md", ".gitignore", "vue3-course.code-workspace"}
        files = []
        for entry in source.infolist():
            path = Path(entry.filename)
            if entry.is_dir() or (path.parts[0] not in projects and entry.filename not in root_files):
                continue
            data = source.read(entry)
            if data.startswith(LFS_HEADER):
                raise RuntimeError(f"配布対象にGit LFSのポインターがあります: {entry.filename}")
            files.append((entry, data))

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for entry, data in files:
            archive.writestr(entry, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    print(f"配布元: {revision}")
    print(f"作成先: {output.resolve()}")
    print(f"容量: {output.stat().st_size / 1024 / 1024:.1f} MiB / {len(files)} ファイル")


if __name__ == "__main__":
    main()
