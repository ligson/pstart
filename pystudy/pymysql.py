# coding=utf8
import MySQLdb


try:
    # 你好
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="password", db="nts", port=3306, charset='utf8')
    # conn.select_db('python')
    
    cur = conn.cursor()
    count = cur.execute("select id,name,is_register from consumer")
    
    # values=[]
    # cur.executemany('insert into test values(%s,%s)',values)
    # cur.execute('update test set info="I am rollen" where id=3')
    
    print count
    #     #你好
    #     result = cur.fetchone()
    #     print result

    # 你好
    results = cur.fetchmany(count)
    for r in results:
        print r
    
    print "=========================="
    for r in range(count):
        print "%d-----%s" % (r, results[r])
    
    print "++++++++++++++++++++++"
    
    # x or y: if x is false, then y, else x
    # x and y: if x is false, then x, else y
    # not x: if x is false, then True, else False
    
    for r in results:
        print "ID:%d  姓名:%s       是否注册：%s" % (r[0], r[1], (ord(r[2]) and "否" or "是"))
    
    
    
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
