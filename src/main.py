import Verilog_VCD
import sys
import logging
import os

global file_tester
global file_4_test

def main():
    # 设置日志等级，不需要INFO可将下行注释
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) != 3:
        logging.error('mini_Compare_VCD: 参数数量不正确，请正确输入参数\n    python main.py file_tester file_tobe_tested')
    file_tester = sys.argv[1]
    file_4_test = sys.argv[2]

    if not os.path.isfile(file_tester):
        logging.error('无法打开标准vcd文件: ' + file_tester)
        exit(1)
    if not os.path.isfile(file_4_test):
        logging.error('无法打开待检测的vcd文件'+ file_4_test)
        exit(1)

    logging.info('已成功找到文件: 标准文件' + file_tester + '; 待检测文件' + file_4_test)

if __name__ == "__main__":
    main()