import os, time
from tnpb.bot import TNPBot



def main():
    time.sleep(10)
    serial_num = False
    
    for i in range(10):
        try:
            tnp_bot = TNPBot()
            resp = tnp_bot.get_query_result(id=os.getenv("ID"),
                                            email=os.getenv("EMAIL"))
            serial_num = tnp_bot.send_application(resp)
            
        except AttributeError:
            print("Failed in the {} th session".format(i+1))
            pass
        if serial_num:
            break
    
if __name__ == "__main__":
    main()
