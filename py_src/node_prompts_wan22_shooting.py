import json
import logging
import os
from .constants import get_category, get_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Wan22ShootingNode")


class Wan22ShootingNode:
    NAME = get_name("Wan22ShootingNode")
    CATEGORY = get_category()
    FUNCTION = "generate_shooting_prompt"
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("提示词", )

    @staticmethod
    def load_config():
        try:
            config_path = os.path.join(os.path.dirname(__file__), "../list",
                                       "wan22_shooting.json")
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(
                "Configuration file list/wan22_shooting.json not found.")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in list/wan22_shooting.json.")
            raise
        except Exception as e:
            logger.error(f"Error loading configuration: {str(e)}")
            raise

    @classmethod
    def INPUT_TYPES(cls):
        config = cls.load_config()
        return {
            "required": {
                "人物描述": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "场景类型": (config["场景类型选项"], {
                    "default": "——"
                }),
                "运动场景": (config["运动场景选项"], {
                    "default": "——"
                }),
                "人物情绪": (config["人物情绪选项"], {
                    "default": "——"
                }),
                "运镜方式": (config["运镜方式选项"], {
                    "default": "——"
                }),
                "光源类型": (config["光源类型选项"], {
                    "default": "——"
                }),
                "光线类型": (config["光线类型选项"], {
                    "default": "——"
                }),
                "镜头类型": (config["镜头类型选项"], {
                    "default": "——"
                }),
                "焦距": (config["焦距选项"], {
                    "default": "——"
                }),
                "色调": (config["色调选项"], {
                    "default": "——"
                }),
                "视觉风格": (config["视觉风格选项"], {
                    "default": "——"
                }),
                "特效镜头": (config["特效镜头选项"], {
                    "default": "——"
                }),
            }
        }

    def generate_shooting_prompt(self, 人物描述, 场景类型, 运动场景, 人物情绪, 运镜方式, 光源类型,
                                 光线类型, 镜头类型, 焦距, 色调, 视觉风格, 特效镜头):
        elements = [
            人物描述 if 人物描述 else "基于输入图像，保持人物外观和服饰特征，一个美丽的女人",
            f"在{场景类型}" if 场景类型 != "——" else "",
            f"进行{运动场景}" if 运动场景 != "——" else "",
            f"情绪为{人物情绪}" if 人物情绪 != "——" else "",
            f"使用{运镜方式}" if 运镜方式 != "——" else "",
            f"光源为{光源类型}" if 光源类型 != "——" else "",
            f"光线为{光线类型}" if 光线类型 != "——" else "",
            f"镜头为{镜头类型}" if 镜头类型 != "——" else "",
            f"焦距为{焦距}" if 焦距 != "——" else "", f"色调为{色调}" if 色调 != "——" else "",
            f"风格为{视觉风格}" if 视觉风格 != "——" else "",
            f"特效为{特效镜头}" if 特效镜头 != "——" else ""
        ]
        prompt_parts = [e for e in elements if e]
        prompt = "，".join(prompt_parts) if prompt_parts else ""
        return (prompt, )


NODE_CLASS_MAPPINGS = {"Wan22ShootingNode": Wan22ShootingNode}

NODE_DISPLAY_NAME_MAPPINGS = {"Wan22ShootingNode": "Wan2.2拍摄提示词"}
