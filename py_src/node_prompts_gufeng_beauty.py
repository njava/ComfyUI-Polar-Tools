import json
import logging
import os
from .constants import get_category, get_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("GufengBeautyNode")


class GufengBeautyNode:
    NAME = get_name("GufengBeautyNode")
    CATEGORY = get_category()
    FUNCTION = "generate_beauty_prompt"
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("人物描述", )

    @staticmethod
    def load_config():
        try:
            config_path = os.path.join(os.path.dirname(__file__), "../list",
                                       "gufeng_beauty.json")
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(
                "Configuration file list/gufeng_beauty.json not found.")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in list/gufeng_beauty.json.")
            raise
        except Exception as e:
            logger.error(f"Error loading configuration: {str(e)}")
            raise

    @classmethod
    def INPUT_TYPES(cls):
        config = cls.load_config()
        return {
            "required": {
                "主体年龄": (config["主体年龄选项"], {
                    "default": "——"
                }),
                "发型": (config["发型选项"], {
                    "default": "——"
                }),
                "体型": (config["体型选项"], {
                    "default": "——"
                }),
                "面部特征": (config["面部特征选项"], {
                    "default": "——"
                }),
                "服饰类型": (config["服饰类型选项"], {
                    "default": "——"
                }),
                "服饰细节": (config["服饰细节选项"], {
                    "default": "——"
                }),
            }
        }

    def generate_beauty_prompt(self, 主体年龄, 发型, 体型, 面部特征, 服饰类型, 服饰细节):
        subject_parts = [
            主体年龄 if 主体年龄 != "——" else "", 发型 if 发型 != "——" else "",
            体型 if 体型 != "——" else "", 面部特征 if 面部特征 != "——" else "",
            f"穿着{服饰类型}" if 服饰类型 != "——" else "", 服饰细节 if 服饰细节 != "——" else ""
        ]
        subject_desc = "基于输入图像，保持人物外观和服饰特征，一个美丽的女人" + ("，" + "，".join(
            [p for p in subject_parts if p]) if any(subject_parts) else "")
        return (subject_desc, )


NODE_CLASS_MAPPINGS = {"GufengBeautyNode": GufengBeautyNode}

NODE_DISPLAY_NAME_MAPPINGS = {"GufengBeautyNode": "古风美女提示词"}
