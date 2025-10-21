import json
import logging
import os
from .constants import get_category, get_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DynamicCinematicKeyframeNode")


class DynamicCinematicKeyframeNode:
    NAME = get_name("DynamicCinematicKeyframeNode")
    CATEGORY = get_category()
    FUNCTION = "generate_keyframe_prompt"
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("提示词", )

    @staticmethod
    def load_config():
        try:
            config_path = os.path.join(os.path.dirname(__file__), "../list", "character_keyframe_actions.json")
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error("Configuration file list/character_keyframe_actions.json not found.")
            raise
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in list/character_keyframe_actions.json.")
            raise
        except Exception as e:
            logger.error(f"Error loading configuration: {str(e)}")
            raise

    @classmethod
    def INPUT_TYPES(cls):
        config = cls.load_config()
        return {
            "required": {
                "角色1描述": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "角色1动作": (list(config["动作模板选项"].keys()), {
                    "default": "无"
                }),
                "角色2描述": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "角色2动作": (list(config["动作模板选项"].keys()), {
                    "default": "无"
                }),
                "角色3描述": ("STRING", {
                    "default": "",
                    "multiline": True
                }),
                "角色3动作": (list(config["动作模板选项"].keys()), {
                    "default": "无"
                }),
            }
        }

    def generate_keyframe_prompt(self, 角色1描述, 角色1动作, 角色2描述, 角色2动作, 角色3描述, 角色3动作):
        config = self.load_config()
        keyframe1_elements = []
        keyframe2_elements = []

        # Helper function to format a single character's keyframe actions
        def format_character_keyframes(description, action_name):
            if not description:
                return None, None
            action = config["动作模板选项"].get(action_name, {})
            if action:
                keyframe1 = action.get("关键帧1", {})
                keyframe2 = action.get("关键帧2", {})
                prompt1 = f"{keyframe1.get('镜头运动', '').replace('[角色X]', description)}, 姿势: {keyframe1.get('姿势', '')}, 表情: {keyframe1.get('表情', '')}, 光线: {keyframe1.get('光线', '')}, {keyframe1.get('分辨率', '')}"
                prompt2 = f"{keyframe2.get('镜头运动', '').replace('[角色X]', description)}, 姿势: {keyframe2.get('姿势', '')}, 表情: {keyframe2.get('表情', '')}, 光线: {keyframe2.get('光线', '')}, {keyframe2.get('分辨率', '')}"
                return prompt1, prompt2
            else:
                prompt1 = f"慢镜头特写于{description}的脸部, 姿势: 静立不动, 表情: 陷入沉思，表情微妙变化, 光线: 戏剧化光线, 4K，超现实"
                prompt2 = f"镜头缓慢推进于{description}的脸部, 姿势: 轻微转头, 表情: 眼神深邃，笑容淡雅, 光线: 侧光勾勒轮廓, 4K，超现实"
                return prompt1, prompt2

        # Process each character and collect keyframe actions
        for desc, action in [(角色1描述, 角色1动作), (角色2描述, 角色2动作), (角色3描述, 角色3动作)]:
            prompt1, prompt2 = format_character_keyframes(desc, action)
            if prompt1 and prompt2:
                keyframe1_elements.append(prompt1)
                keyframe2_elements.append(prompt2)

        # Combine keyframes into two segments
        elements = []
        if keyframe1_elements:
            elements.append(f"关键帧1: {', '.join(keyframe1_elements)}")
        if keyframe2_elements:
            elements.append(f"关键帧2: {', '.join(keyframe2_elements)}")

        # Join segments with semicolons
        prompt = "; ".join(elements) if elements else ""
        return (prompt, )


NODE_CLASS_MAPPINGS = {"DynamicCinematicKeyframeNode": DynamicCinematicKeyframeNode}

NODE_DISPLAY_NAME_MAPPINGS = {"DynamicCinematicKeyframeNode": "动态电影化关键帧提示词"}

manifest = {
    "name": "动态电影化关键帧提示词",
    "version": "1.0",
    "description": "动态电影化关键帧提示词节点，为最多三个角色生成结构化的两帧动作提示词，分为关键帧1和关键帧2两段，支持动态角色增减和动作模板选择",
    "author": ""
}