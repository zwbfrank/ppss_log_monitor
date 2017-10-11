
import re
import send_mail as sm

# # 匹配模式
pattern_error = r'.*\[ERROR\].*'
pattern_warning = r'.*WARNING.*'
# patter

# 获取服务器日志路径
log_path ="test_log.log"

# 读取日志文件存入list或dict以便分析
def get_log_lists(log_path):
	try:
		with open(log_path,'r',errors='ignore') as f_obj:
			log_lists = f_obj.readlines()
	except FileNotFoundError:
		pass
	else:
		return log_lists


# 分析日志
def analysis_log(log_lists): 
	for log_list in log_lists:
		if log_list:
			# 日志错误信息匹配模式
			if re.match(pattern_error,log_list):
				pass
			# 警告信息匹配模式
			elif re.match(pattern_warning,log_list):
				# sm.send_email(log_list)
				print("hello")
		# else:
		# 	return
		# 	pass
		
if __name__ == '__main__':

	# sm.send_email('hello')

	log_lists = get_log_lists(log_path)
	analysis_log(log_lists)