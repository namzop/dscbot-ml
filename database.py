import sqlite3 


def get_link(name):
    conn = sqlite3.connect('data.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT * FROM links WHERE name="{}"'.format(name))
    lmfao = c.fetchone()
    conn.commit()
    conn.close()
    if lmfao == [] or lmfao == None:
        return "Not Found"
    else:
        lmao = lmfao[1]
        return lmao
        


def make_new_link(name, link):
    conn = sqlite3.connect('data.db', check_same_thread=False)
    c = conn.cursor()
    sql = "INSERT INTO links(name, link) VALUES(?, ?)"
    val = (name, link)

    c.execute(sql, val)
    conn.commit()
    conn.close()
    return "Done!"



