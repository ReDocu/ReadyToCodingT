def solution(id_pw, db):

    check_db = dict(db)

    if check_db.get(id_pw[0]) == None:
        return 'fail'
    else:
        return 'login' if check_db.get(id_pw[0]) == id_pw[1] else 'wrong pw'