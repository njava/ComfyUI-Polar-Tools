import logging
from typing import Dict, Any, Tuple
import os

from .constants import get_category, get_name

# 设置日志配置
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ImageSizeNode")


class ImageSizeNode:

    NAME = get_name("ImageSizeNode")
    CATEGORY = get_category()

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        return {
            'optional': {},
            "required": {
                "dimensions": (
                    [
                        # 'Custom',
                        '1080 x 1920  (主流抖音)',
                        '1440 x 2560  (2K)',
                        '576 x 1024  (WAN2.2 原生)',
                        '720 x 1280  (WAN2.2 720P)',
                        '1080 x 1920  (WAN2.2 全高清)',
                        '1080 x 1440 (小红书)',
                        '1024 x 1536 (Liblib)',
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
                    "default": 1.0,
                    "min": 0.5,
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
