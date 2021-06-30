

def insertone(obj,table_basse, con):
    seq = vars(obj)
    sec = executeStatement(seq,table_basse,1,con,0)
    return sec

def updateone(obj,table_basse, con,id):
    seq = vars(obj)
    sec = executeStatement(seq,table_basse,2,con,id)
    return sec

def deletedone(table_basse, con,id):
    sec = executeStatement('',table_basse,3,con,id)
    return sec

def getAll(sql,con):
    obj = ''
    cursor = con.cursor()
    cursor.execute(sql)
    print(cursor.columns)
    return ''


def executeStatement(obj,table_basse, tp,con, id):
    sql = ''
    atr = str()
    satr = str()
    values = list()
    if(tp == 1):
        sql = 'insert into ' + table_basse + '('
        for kv in obj:
            if(kv == 'id' or kv == 'add' or kv == 'edit' or kv == 'dele'):
                ''
            else:
                atr = atr +  kv + ','
                satr += '%s ,'
                values.append(obj[kv])
        sql = sql + atr[:-1] + ') VALUES (' + satr[:-1] + ')'

        cursor = con.cursor()
        cursor.execute(sql,values)
        id = cursor.lastrowid
        con.commit()
    elif(tp == 2):

        for kv in obj:
            if (kv == 'id' or kv == 'add' or kv == 'edit' or kv == 'dele'):
                ''
            else:
                atr = atr + kv + '=%s,'
                values.append(obj[kv])
        values.append(id)
        sql = 'UPDATE ' + table_basse + ' set ' + atr[:-1] + ' where id = %s'

        cursor = con.cursor()
        cursor.execute(sql, values)
        con.commit()
    else:
        sql = 'DELETE FROM ' + table_basse + ' where id = %s'
        values.append(id)
        cursor = con.cursor()
        cursor.execute(sql, values)
        con.commit()
    return id