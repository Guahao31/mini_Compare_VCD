import json
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

def get_value_change_dict(vcd):
    # Get vcd from the struct 
    # return with a dict that nets_name -> [ time , value ]
    res_dict = {}
    for element in vcd.values():
        nets = element['nets']
        nets = nets[0]
        nets_name = nets['hier'] + '.' + nets['name']
        t_v = []
        tv_table = element['tv']
        for tv in tv_table:
            t_v.append(tuple([tv[0], int(tv[1], 2)]))
        res_dict[nets_name] = t_v

    return res_dict

def main():
    # The level of log, can be commented when no need to read INFO log
    logging.basicConfig(level=logging.INFO)
    file_tester, file_4_test = read_in_filename(sys.argv)

    # Get the signals for tester and tested file
    sigs_tester, sigs_4_test = Verilog_VCD.list_sigs(file_tester), Verilog_VCD.list_sigs(file_4_test)
    # test if all of the signals in tester are in file tested
    test_sigs_res, test_sigs_list = test_sigs(sigs_tester, sigs_4_test)
    if not test_sigs_res:
        error_msg = 'mini_Compare_VCD: 需要将以下信号添加进被检测的vcd文件\n\t'
        for sig in test_sigs_list:
            error_msg += str(sig) + ' '
        logging.error(error_msg)
        exit(1)

    # Get the dict that nets_name: value_changed_list
    vcd_tester = Verilog_VCD.parse_vcd(file_tester)
    timescale, endtime = Verilog_VCD.get_timescale(), Verilog_VCD.get_endtime()
    dict_tester = get_value_change_dict(vcd_tester)
    # print(json.dumps(vcd_tester, indent=4))
    vcd_4_test = Verilog_VCD.parse_vcd(file_4_test)
    dict_4_test = get_value_change_dict(vcd_4_test)
    
    


    
if __name__ == "__main__":
    main()