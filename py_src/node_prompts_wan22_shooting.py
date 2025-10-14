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
                "场景类型": (list(config["场景类型选项"].keys()), {
                    "default": "无"
                }),
                "运动场景": (list(config["运动场景选项"].keys()), {
                    "default": "无"
                }),
                "人物情绪": (list(config["人物情绪选项"].keys()), {
                    "default": "无"
                }),
                "运镜方式": (list(config["运镜方式选项"].keys()), {
                    "default": "无"
                }),
                "光源类型": (list(config["光源类型选项"].keys()), {
                    "default": "无"
                }),
                "光线类型": (list(config["光线类型选项"].keys()), {
                    "default": "无"
                }),
                "镜头类型": (list(config["镜头类型选项"].keys()), {
                    "default": "无"
                }),
                "焦距": (list(config["焦距选项"].keys()), {
                    "default": "无"
                }),
                "色调": (list(config["色调选项"].keys()), {
                    "default": "无"
                }),
                "视觉风格": (list(config["视觉风格选项"].keys()), {
                    "default": "无"
                }),
                "特效镜头": (list(config["特效镜头选项"].keys()), {
                    "default": "无"
                }),
            }
        }

    def generate_shooting_prompt(self, 人物描述, 场景类型, 运动场景, 人物情绪, 运镜方式, 光源类型,
                                 光线类型, 镜头类型, 焦距, 色调, 视觉风格, 特效镜头):
        config = self.load_config()

        # Map input selections to their detailed descriptions
        elements = [
            人物描述 if 人物描述 else "基于输入图像，保持人物外观和服饰特征，一个美丽的女人",
            config["场景类型选项"].get(场景类型, "") if 场景类型 != "无" else "",
            config["运动场景选项"].get(运动场景, "") if 运动场景 != "无" else "",
            config["人物情绪选项"].get(人物情绪, "") if 人物情绪 != "无" else "",
            config["运镜方式选项"].get(运镜方式, "") if 运镜方式 != "无" else "",
            config["光源类型选项"].get(光源类型, "") if 光源类型 != "无" else "",
            config["光线类型选项"].get(光线类型, "") if 光线类型 != "无" else "",
            config["镜头类型选项"].get(镜头类型, "") if 镜头类型 != "无" else "",
            config["焦距选项"].get(焦距, "") if 焦距 != "无" else "",
            config["色调选项"].get(色调, "") if 色调 != "无" else "",
            config["视觉风格选项"].get(视觉风格, "") if 视觉风格 != "无" else "",
            config["特效镜头选项"].get(特效镜头, "") if 特效镜头 != "无" else ""
        ]

        # Filter out empty elements and join with commas
        prompt_parts = [e for e in elements if e]
        prompt = "，".join(prompt_parts) if prompt_parts else ""
        return (prompt, )


NODE_CLASS_MAPPINGS = {"Wan22ShootingNode": Wan22ShootingNode}

NODE_DISPLAY_NAME_MAPPINGS = {"Wan22ShootingNode": "Wan2.2拍摄提示词"}

manifest = {
    "name": "Wan2.2拍摄提示词",
    "version": "1.0",
    "description": "Wan2.2拍摄提示词节点，用于生成汉服拍摄场景的提示词，支持多种场景、光线、运镜和特效配置",
    "author": ""
}
