import Verilog_VCD
import sys
import logging
import os

global file_tester
global file_4_test

def read_in_filename(argv: list):
    # Get the tester and tested file
    # return with (str, str) as file_tester and file_4_test
    if len(argv) != 3:
        logging.error('mini_Compare_VCD: 参数数量不正确，请正确输入参数\n    python main.py file_tester file_tobe_tested')
    file_tester = argv[1]
    file_4_test = argv[2]

    if not os.path.isfile(file_tester):
        logging.error('无法打开标准vcd文件: ' + file_tester)
        exit(1)
    if not os.path.isfile(file_4_test):
        logging.error('无法打开待检测的vcd文件'+ file_4_test)
        exit(1)

    logging.info('已成功找到文件: 标准文件' + file_tester + '; 待检测文件' + file_4_test)
    return (file_tester, file_4_test)

def test_sigs(sigs_tester, sigs_4_test):
    # test if all of the sigs_tester are included in the file being tested
    # return with a boolean var.
    res = True
    res_list = []
    for sig in sigs_tester:
        if sig not in sigs_4_test:
            res = False
            res_list.append(sig)

    return res, res_list

def main():
    # The level of log, can be commented when no need to read INFO log
    logging.basicConfig(level=logging.INFO)
    file_tester, file_4_test = read_in_filename(sys.argv)

    sigs_tester, sigs_4_test = Verilog_VCD.list_sigs(file_tester), Verilog_VCD.list_sigs(file_4_test)
    # print(sigs_tester)
    # print(sigs_4_test)
    test_sigs_res, test_sigs_list = test_sigs(sigs_tester, sigs_4_test)
    if not test_sigs_res:
        error_msg = 'mini_Compare_VCD: 需要将以下信号添加进被检测的vcd文件\n\t'
        for sig in test_sigs_list:
            error_msg += str(sig) + ' '
        logging.error(error_msg)
        exit(1)

    vcd_tester = Verilog_VCD.parse_vcd(file_tester)
    timescale, endtime = Verilog_VCD.get_timescale(), Verilog_VCD.get_endtime()
    print(timescale, endtime)
        




    
if __name__ == "__main__":
    main()