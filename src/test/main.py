from canalDispatch.binlogdispatch import  BinlogDispatch
from canalDispatch.events import Event
import pymysql.cursors
from canalDispatch.eventimpl import EventImpl

class SampleEventHandle(EventImpl):
    def insertHandle(self, event:Event):
        print(event.debugstring())
        print("insert")
    def updateHandle(self, event:Event):
        print("update")
        print(event.debugstring())
    def deleteHandle(self, event:Event):
        print("delete")
        print(event.debugstring())
def main():
    dispatch = BinlogDispatch("127.0.0.1", 11111)
    ##dispatch.addEventListener(events.INSERT_EVENT, insertHandle)
    dispatch.addEventListener(handle = SampleEventHandle())
    dispatch.Start()
def test():
    connecntion = pymysql.connect(
                            host='127.0.0.1',user='root', 
                            port=4406,
                            password='000000', db='test', 
                            charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
                            )
    try:
        with connecntion.cursor() as cursor:
            sql = "insert into test (name) values(%s)"
            cursor.execute(sql,('test6'))
        connecntion.commit()
    finally:
        connecntion.close()
if __name__=="__main__":
    test()