# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse


def init():  # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    #定义一个全局变量
    _global_dict[key] = value


def get_value(key):
    #获得一个全局变量，不存在则提示读取对应变量失败
    try:
        return _global_dict[key]
    except:
        print('Read' + key + 'failed\r\n')


def get_argument():
    parser = argparse.ArgumentParser(description='Preprocessor')
    parser.add_argument('--use_gpu',
                        dest='use_gpu',
                        help='Whether to use GPU to accelerate',
                        action='store_true')

    return parser.parse_args()