import json
import logging
import os
from .constants import get_category, get_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MultipleAnglesNode")


class MultipleAnglesNode:
    NAME = get_name("MultipleAnglesNode")
    CATEGORY = get_category()
    FUNCTION = "generate_multiple_angles_prompt"
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("提示词", )

    @staticmethod
    def load_config():
        try:
            config_path = os.path.join(os.path.dirname(__file__), "../list",
                                       "multiple_angles.json")
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(
                "Configuration file list/multiple_angles.json not found.")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in list/multiple_angles.json.")
            raise
        except Exception as e:
            logger.error(f"Error loading configuration: {str(e)}")
            raise

    @classmethod
    def INPUT_TYPES(cls):
        config = cls.load_config()
        return {
            "required": {
                "角度类型": (list(config["角度选项"].keys()), {
                    "default": "无"
                }),
            }
        }

    def generate_multiple_angles_prompt(self, 角度类型):
        config = self.load_config()

        # Map input selection to its detailed description
        element = config["角度选项"].get(角度类型, "") if 角度类型 != "无" else ""

        # Generate prompt for switching shots
        prompt = f" {element}" if element else ""
        return (prompt, )


NODE_CLASS_MAPPINGS = {"MultipleAnglesNode": MultipleAnglesNode}

NODE_DISPLAY_NAME_MAPPINGS = {"MultipleAnglesNode": "Multiple Angles Node"}

manifest = {
    "name": "Multiple Angles Node",
    "version": "1.0",
    "description": "Multiple Angles Node，用于生成切换镜头的提示词，支持多种角度配置，多角度镜头转换提示词。使用dx8152/Qwen-Edit-2509-Multiple-angles lora",
    "author": ""
}