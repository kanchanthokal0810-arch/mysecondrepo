"""Display a live digital clock in the terminal."""

from datetime import datetime
import time


def main():
    try:
        while True:
            now = datetime.now()
            print(f"\r{now:%Y-%m-%d %H:%M:%S}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()