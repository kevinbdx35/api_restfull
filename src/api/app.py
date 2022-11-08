from src.api.utils.factory import create_app
import sys


__VERSION = "0.18"

__MODE = sys.argv[1] if len(sys.argv) > 1 and str(sys.argv[1]).lower() in ("dev", "test") else "prod"

app = create_app(__MODE)


@app.route("/")
def root_print():
    return f"You are on CodingAPI version {__VERSION} (humbly brought to you by the Dream Team)"


if __name__ == "__main__":
    """
    Launch the main app for Coding API
    """
    app.run(host="127.0.0.1", port=7654)
