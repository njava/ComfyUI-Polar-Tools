from .py_src.node_prompts_onegirl import PromptsOneGirlNode
from .py_src.node_image_size import ImageSizeNode
from .py_src.node_prompts_wan22_shooting import Wan22ShootingNode
from .py_src.node_prompts_gufeng_beauty import GufengBeautyNode

NODE_CLASS_MAPPINGS = {
    ImageSizeNode.NAME: ImageSizeNode,
    PromptsOneGirlNode.NAME: PromptsOneGirlNode,
    Wan22ShootingNode.NAME: Wan22ShootingNode,
    GufengBeautyNode.NAME: GufengBeautyNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    ImageSizeNode.NAME: "图片尺寸|ImageSize",
    PromptsOneGirlNode.NAME: "一个女孩|OneGirlModel",
    Wan22ShootingNode.NAME: "Wan2.2视频镜头|Wan2.2",
    GufengBeautyNode.NAME: "古风美女|GuFengBeauty"
}

print("\033[34mComfyUI 🐻‍❄️Polar's Tools: \033[92mLoaded\033[0m")
print()
