#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
客服后端服务器持续运行脚本
"""

import subprocess
import time
import sys

def run_server():
    """运行客服后端服务器"""
    while True:
        try:
            print("启动深夜密友客服系统API服务器...")
            # 使用subprocess运行服务器，确保它在前台运行
            process = subprocess.Popen([
                sys.executable, 
                "customer_service_api.py"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # 读取输出
            for line in process.stdout:
                print(line, end='')
                
            # 等待进程结束
            process.wait()
            
            # 如果进程退出，等待5秒后重启
            print("服务器意外停止，5秒后重新启动...")
            time.sleep(5)
            
        except KeyboardInterrupt:
            print("\n服务器停止运行")
            break
        except Exception as e:
            print(f"服务器运行错误: {e}")
            print("5秒后重新启动...")
            time.sleep(5)

if __name__ == "__main__":
    run_server()