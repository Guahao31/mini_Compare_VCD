import Verilog_VCD
import sys
import os

global file_tester
global file_4_test

def main():
    if len(sys.argv) != 3:
        raise SystemExit('mini_Compare_VCD: 参数数量不正确，请正确输入参数\n    python main.py file_tester file_tobe_tested')
    file_tester = sys.argv[1]
    file_4_test = sys.argv[2]

    if not os.path.isfile(file_tester):
        raise SystemExit('无法打开标准vcd文件: ' + file_tester)
    if not os.path.isfile(file_4_test):
        raise SystemExit('无法打开待检测的vcd文件'+ file_4_test)

if __name__ == "__main__":
    main()