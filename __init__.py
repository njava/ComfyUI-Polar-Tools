from .py_src.onegirl_model_flux_prompts_note import OneGirlModelFluxPromptsNode
from .py_src.size_node import SizeNode

NODE_CLASS_MAPPINGS = {
    SizeNode.NAME: SizeNode,
    OneGirlModelFluxPromptsNode.NAME: OneGirlModelFluxPromptsNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    SizeNode.NAME: "图片尺寸|ImageSize",
    OneGirlModelFluxPromptsNode.NAME: "一个女模特提示词"
}

print("\033[34mComfyUI 🐻‍❄️Polar's Tools: \033[92mLoaded\033[0m")
print()
