import sqlite3


def get_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    # 預埋漏洞：SQL 字串拼接直接帶入 execute，Semgrep 應該抓到這行
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")

    return cursor.fetchone()


def get_user_safe(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()

    # 正確寫法（對照用）
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

    return cursor.fetchone()
