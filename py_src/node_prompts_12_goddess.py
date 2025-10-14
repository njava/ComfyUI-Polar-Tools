import json
import logging
import os
from .constants import get_category, get_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TwelveGoddessFeaturesNode")


class TwelveGoddessFeaturesNode:
    NAME = get_name("TwelveGoddessFeaturesNode")
    CATEGORY = get_category()
    FUNCTION = "generate_goddess_prompt"
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("提示词", )

    # Load configuration from JSON file
    @staticmethod
    def load_config():
        try:
            config_path = os.path.join(os.path.dirname(__file__), "../list",
                                       "twelve_goddess.json")
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(
                "Configuration file list/twelve_goddess.json not found.")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in list/twelve_goddess.json.")
            raise
        except Exception as e:
            logger.error(f"Error loading configuration: {str(e)}")
            raise

    # Node input parameters definition
    @classmethod
    def INPUT_TYPES(cls):
        config = cls.load_config()
        inputs = {
            "required": {
                "模型选择": (config["模型选项"], {
                    "default": "Qwen-Image"
                }),
                "花神选择": (config["花神选项"], {
                    "default": "无"
                }),
                "花朵": (config["花朵选项"], {
                    "default": "无"
                }),
                "头饰": (list(config["头饰选项"].keys()), {
                    "default": "无"
                }),
                "耳环": (list(config["耳环选项"].keys()), {
                    "default": "无"
                }),
                "妆容": (list(config["妆容选项"].keys()), {
                    "default": "无"
                }),
                "口红": (list(config["口红选项"].keys()), {
                    "default": "无"
                }),
                "眼睛": (list(config["眼睛选项"].keys()), {
                    "default": "无"
                }),
                "鼻子": (list(config["鼻子选项"].keys()), {
                    "default": "无"
                }),
                "眉毛": (list(config["眉毛选项"].keys()), {
                    "default": "无"
                }),
                "面容": (list(config["面容选项"].keys()), {
                    "default": "无"
                }),
                "发型": (list(config["发型选项"].keys()), {
                    "default": "无"
                }),
                "体型": (list(config["体型选项"].keys()), {
                    "default": "无"
                }),
                "衣服": (list(config["衣服选项"].keys()), {
                    "default": "无"
                }),
                "配饰": (list(config["配饰选项"].keys()), {
                    "default": "无"
                }),
                "整体风格": (list(config["整体风格选项"].keys()), {
                    "default": "无"
                })
            }
        }
        return inputs

    # Generate goddess feature prompt for the selected model
    def generate_goddess_prompt(self, 模型选择, 花神选择, 花朵, 头饰, 耳环, 妆容, 口红, 眼睛, 鼻子,
                                眉毛, 面容, 发型, 体型, 衣服, 配饰, 整体风格):
        config = self.load_config()

        # Set default feature values based on selected goddess
        defaults = config["特征"].get(花神选择, {}) if 花神选择 != "无" else {}
        flower = 花朵 if 花朵 != "无" #else defaults.get("花朵", "无")
        # Get scene template from mapping or goddess defaults
        scene_template = config["花朵场景映射"].get(flower, defaults.get(
            "场景模板", "无")) if flower != "无" else "无"
        if flower != "无" and scene_template != "无":
            scene = scene_template.format(花朵=flower)
        else:
            scene = ""

        # Map feature inputs to their detailed descriptions
        feature_inputs = {
            "头饰":
            config["头饰选项"].get(头饰, "") if 头饰 != "无" else config["头饰选项"].get(
                defaults.get("头饰", "无"), ""),
            "耳环":
            config["耳环选项"].get(耳环, "") if 耳环 != "无" else config["耳环选项"].get(
                defaults.get("耳环", "无"), ""),
            "妆容":
            config["妆容选项"].get(妆容, "") if 妆容 != "无" else config["妆容选项"].get(
                defaults.get("妆容", "无"), ""),
            "口红":
            config["口红选项"].get(口红, "") if 口红 != "无" else config["口红选项"].get(
                defaults.get("口红", "无"), ""),
            "眼睛":
            config["眼睛选项"].get(眼睛, "") if 眼睛 != "无" else config["眼睛选项"].get(
                defaults.get("眼睛", "无"), ""),
            "鼻子":
            config["鼻子选项"].get(鼻子, "") if 鼻子 != "无" else config["鼻子选项"].get(
                defaults.get("鼻子", "无"), ""),
            "眉毛":
            config["眉毛选项"].get(眉毛, "") if 眉毛 != "无" else config["眉毛选项"].get(
                defaults.get("眉毛", "无"), ""),
            "面容":
            config["面容选项"].get(面容, "") if 面容 != "无" else config["面容选项"].get(
                defaults.get("面容", "无"), ""),
            "发型":
            config["发型选项"].get(发型, "") if 发型 != "无" else config["发型选项"].get(
                defaults.get("发型", "无"), ""),
            "体型":
            config["体型选项"].get(体型, "") if 体型 != "无" else config["体型选项"].get(
                defaults.get("体型", "无"), ""),
            "衣服":
            config["衣服选项"].get(衣服, "") if 衣服 != "无" else config["衣服选项"].get(
                defaults.get("衣服", "无"), ""),
            "配饰":
            config["配饰选项"].get(配饰, "") if 配饰 != "无" else config["配饰选项"].get(
                defaults.get("配饰", "无"), ""),
            "整体风格":
            config["整体风格选项"].get(整体风格, "") if 整体风格 != "无" else
            config["整体风格选项"].get(defaults.get("整体风格", "无"), "")
        }

        # Combine selected features, excluding empty descriptions
        desc_parts = [value for key, value in feature_inputs.items() if value]
        description = ", ".join(
            desc_parts
        ) if desc_parts else "8K ultra photorealistic cinematic portrait,beautiful woman in traditional Hanfu"

        # Use model-specific template
        template = config["提示词模板"].get(模型选择, config["提示词模板"]["Qwen-Image"])
        prompt = template.format(描述=description, 场景模板=scene)

        return (prompt, )


NODE_CLASS_MAPPINGS = {"TwelveGoddessFeaturesNode": TwelveGoddessFeaturesNode}

NODE_DISPLAY_NAME_MAPPINGS = {"TwelveGoddessFeaturesNode": "十二花神特征"}

manifest = {
    "name": "十二花神特征",
    "version": "1.0",
    "description":
    "十二花神特征节点，用于生成汉服十二女神（花神）的提示词，支持Qwen-Image、Qwen-Image-Edit和Flux，带花神联动默认值及动态花朵场景",
    "author": ""
}
