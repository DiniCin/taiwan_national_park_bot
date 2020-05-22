import os, time
from tnpb.bot import TNPBot



def main():
    time.sleep(10)
    tnp_bot = TNPBot()

    resp = tnp_bot.get_query_result(id=os.getenv("ID"), email=os.getenv("EMAIL"))
    tnp_bot.send_application(resp)
    
if __name__ == "__main__":
    main()
