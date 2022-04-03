"""
@Module: main
@Function: 
@Author: Chengxi Zhang
@Created: 2022/3/31 7:20 PM
"""
import pandas as pd
from configparser import ConfigParser


conf = ConfigParser()
conf.read('config/base.txt')


if __name__ == '__main__':
    pd.read_csv('')
