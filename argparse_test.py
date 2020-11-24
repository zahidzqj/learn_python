# python -m py_compile .\argparse_test.py
import argparse
import sys
import os
import glob

def argparse_args():
	# 创建对象
 	parser = argparse.ArgumentParser()
 	parser.add_argument('--input', default='C:/Users/sister/Desktop/demo', type=str,help='input dir')
 	parser.add_argument('--num',default = 10, type = int, help = 'file number')
 	return parser.parse_args()

def main(args):
	path = args.input
	print('当前路径：',sys.path[0])
	print('工作路径：',os.getcwd())
	print('default input:',path)
	list_subdir = os.listdir(path)
	print('查看所有子目录：',list_subdir)
	# for dir_name in list_subdir:
	# 	file_join = os.path.join(path,dir_name)
	# 	print('遍历所有子目录',file_join)

	#遍历文件夹中的子文件夹以及文件，先返回
	for root,dirs,files in os.walk(path):
		print('根目录：',root)
		print('子目录：',dirs)
		print('子文件：',files)

	print('返回程序的参数',sys.argv)#[0]返回文件路径加文件名字
	print('返回绝对路径：',os.path.abspath(sys.argv[0]))

	search_files = glob.glob(os.path.join(path,'*.jpg'))
	print('获取符合匹配的文件路径：',search_files)

if __name__ == '__main__':
	main(argparse_args())
