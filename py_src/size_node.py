import logging
from typing import Dict, Any, Tuple
import os

from .constants import get_category, get_name

# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SizeNode")


class SizeNode:

    NAME = get_name("SizeNode")
    CATEGORY = get_category()

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            'optional': {},
            "required": {
                "dimensions": (
                    [
                        # 'Custom',
                        '633 x 1125  (抖音|16:9)',
                        '1080 x 1920  (小红书)',
                        '1536 x 640   (landscape)',
                        '1344 x 768   (landscape)',
                        '1216 x 832   (landscape)',
                        '1152 x 896   (landscape)',
                        '1024 x 1024  (square)',
                        ' 896 x 1152  (portrait)',
                        ' 832 x 1216  (portrait)',
                        ' 768 x 1344  (portrait)',
                        ' 640 x 1536  (portrait)',
                    ],
                    {
                        "default": '1024 x 1024  (square)'
                    }),
                "clip_scale": ("FLOAT", {
                    "default": 2.0,
                    "min": 1.0,
                    "max": 10.0,
                    "step": .5
                }),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("WIDTH", "HEIGHT")
    FUNCTION = "generate"

    def generate(self, dimensions, clip_scale):
        if True:
            result = [x.strip() for x in dimensions.split('x')]
            width = int(result[0])
            height = int(result[1].split(' ')[0])
        return (
            int(width * clip_scale),
            int(height * clip_scale),
        )
