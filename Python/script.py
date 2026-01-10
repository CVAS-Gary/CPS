#!/usr/bin/env python3
"""計算檔案的行數"""

import sys
import os


def count_lines(filepath):
    """計算指定檔案的行數
    
    Args:
        filepath: 檔案路徑
        
    Returns:
        行數，如果發生錯誤則返回 -1
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = sum(1 for _ in f)
        return lines
    except FileNotFoundError:
        print(f"錯誤: 找不到檔案 '{filepath}'")
        return -1
    except Exception as e:
        print(f"錯誤: {e}")
        return -1


def main():
    if len(sys.argv) < 2:
        print("用法: python script.py <檔案路徑>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    if not os.path.isfile(filepath):
        print(f"錯誤: '{filepath}' 不是有效的檔案")
        sys.exit(1)
    
    lines = count_lines(filepath)
    
    if lines >= 0:
        print(f"檔案 '{filepath}' 共有 {lines} 行")


if __name__ == "__main__":
    main()
