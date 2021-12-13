import os,sys

home_path = os.getcwd()
proj_path = os.path.join(home_path,"codes/news_recsys/news_rec_server/")

stop_words_path = proj_path + "conf/stop_words.txt"
bad_case_news_log_path = proj_path + "logs/news_bad_cases.log"

sys.path.append(proj_path)
sys.path.append(os.path.dirname(__file__))
