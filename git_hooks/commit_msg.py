import sys
import re


def main():
    commit_msg_filepath = sys.argv[1]

    with open(commit_msg_filepath, "r+", encoding="utf-8") as f:
        commit_msg = f.read()

        pattern = re.compile(r"(LINTUP-\d+)", re.IGNORECASE)
        matches = pattern.findall(commit_msg)

        if matches:
            for match in matches:
                task_name = match.upper()
                url = f"https://tracker.yandex.ru/{task_name}"
                link = f"[{task_name}]({url})"
                commit_msg = re.sub(match, link, commit_msg, flags=re.IGNORECASE)

            f.seek(0)
            f.write(commit_msg)
            f.truncate()


if __name__ == "__main__":
    main()
