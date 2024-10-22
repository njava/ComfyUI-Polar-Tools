import json
import logging
from typing import Dict, Any, Tuple
import os

from .constants import get_category, get_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("OneGirlModelFluxPromptsNode")


class OneGirlModelFluxPromptsNode:

    NAME = get_name("OneGirlModelFluxPromptsNode")
    CATEGORY = get_category()

    @classmethod
    def INPUT_TYPES(cls) -> Dict[str, Any]:
        # 获取当前文件的目录
        current_dir = os.path.dirname(__file__)
        # 构建 clothing.json 文件的完整路径
        options_file_path = os.path.join(current_dir, '../list/model.json')
        logger.debug(options_file_path)

        # 从 JSON 文件加载下拉列表选项
        try:
            with open(options_file_path, 'r', encoding='utf-8') as file:
                cls.options = json.load(file)
        except FileNotFoundError:
            logger.error(f"File not found: {options_file_path}")
            cls.options = {}

        max_float_value = 1.8

        return {
            'optional': {},
            "required": {
                "Style": (list(cls.options.get("风格Style", {}).keys()), ),
                "Characters":
                (list(cls.options.get("角色Characters", {}).keys()), ),
                "Eyes":
                (list(cls.options.get("模特眼神 | Eyes Expressions",
                                      {}).keys()), ),
                "Expressions":
                (list(cls.options.get("模特表情 | Expressions", {}).keys()), ),
                "Hairstyle":
                (list(cls.options.get("模特发型|Hairstyle", {}).keys()), ),
                "BodyType":
                (list(cls.options.get("模特体型|Body type", {}).keys()), ),
                "Action": (list(cls.options.get("模特动作|Action", {}).keys()), ),
                "Composition":
                (list(cls.options.get("构图Composition", {}).keys()), ),
                "SceneSpring":
                (list(cls.options.get("场景Scene_spring", {}).keys()), ),
                "SceneSummer":
                (list(cls.options.get("场景Scene_summer", {}).keys()), ),
                "SceneAutumn":
                (list(cls.options.get("场景Scene_autumn", {}).keys()), ),
                "SceneWinter": (list(
                    cls.options.get("场景Scene_winter", {}).keys()), ),
                "SceneT": (list(cls.options.get("场景Scene_T", {}).keys()), ),
                "SceneRoom": (list(cls.options.get("场景Scene_room",
                                                   {}).keys()), ),
                "SceneOffice": (list(
                    cls.options.get("场景Scene_office", {}).keys()), ),
                "SceneSimple": (list(
                    cls.options.get("场景Scene_simple", {}).keys()), ),
                "SceneGuizhou": (list(
                    cls.options.get("场景Scene_Guizhou", {}).keys()), ),
                "HatColor": (list(cls.options.get("颜色Color", {}).keys()), ),
                "Hat": (list(cls.options.get("帽子Flux", {}).keys()), ),
                "Hat_weight": ("FLOAT", {
                    "default": 1.0,
                    "step": 0.1,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "ClothesPattern": (list(
                    cls.options.get("图案Patterns", {}).keys()), ),
                "ClothesColor": (list(cls.options.get("颜色Color",
                                                      {}).keys()), ),
                "Clothes": (list(cls.options.get("衣服Flux", {}).keys()), ),
                "Clothes_weight": ("FLOAT", {
                    "default": 1.0,
                    "step": 0.1,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "PantsColor": (list(cls.options.get("颜色Color", {}).keys()), ),
                "Pants": (list(cls.options.get("裤子", {}).keys()), ),
                "Pants_weight": ("FLOAT", {
                    "default": 1.0,
                    "step": 0.1,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "ShoesColor": (list(cls.options.get("颜色Color", {}).keys()), ),
                "Shoes": (list(cls.options.get("鞋子", {}).keys()), ),
                "Shoes_weight": ("FLOAT", {
                    "default": 1.0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "BackpackColor": (list(cls.options.get("颜色Color",
                                                       {}).keys()), ),
                "Backpack": (list(cls.options.get("背包", {}).keys()), ),
                "Backpack_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "OtherClothes": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "forceInput": False
                }),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("clip_l", "t5xxl")
    FUNCTION = "get_prompt"

    def get_prompt(self,
                   Style="",
                   Characters="",
                   Expressions="",
                   Eyes="",
                   Hairstyle="",
                   BodyType="",
                   Action="",
                   Composition="",
                   SceneSpring="",
                   SceneSummer="",
                   SceneAutumn="",
                   SceneWinter="",
                   SceneT="",
                   SceneRoom="",
                   SceneOffice="",
                   SceneSimple="",
                   SceneGuizhou="",
                   HatColor="",
                   Hat="",
                   Hat_weight=1,
                   Clothes="",
                   ClothesPattern="",
                   ClothesColor="",
                   Clothes_weight=1,
                   Pants="",
                   PantsColor="",
                   Pants_weight=1,
                   ShoesColor="",
                   Shoes="",
                   Shoes_weight=1,
                   BackpackColor="",
                   Backpack="",
                   Backpack_weight=1,
                   OtherClothes="",
                   **kwargs):

        byz_clothes = []
        image_style = ''
        image_characters = ''
        image_composition = ''

        characters_expressions = None
        characters_hairstyle = None
        characters_bodytype = None
        characters_action = None
        characters_eyes = None

        scene_template = "{clothes}"

        if Style != "None":
            image_style = self.options.get("风格Style", {}).get(Style, "")
        if Characters != "None":
            image_characters = self.options.get("角色Characters",
                                                {}).get(Characters, "")
        if Composition != "None":
            image_composition = self.options.get("构图Composition",
                                                 {}).get(Composition, "")

        if Expressions != "None":
            characters_expressions = self.options.get("模特表情 | Expressions",
                                                      {}).get(Expressions, "")
        if Eyes != "None":
            characters_eyes = self.options.get("模特眼神 | Eyes Expressions",
                                               {}).get(Expressions, "")
        if Hairstyle != "None":
            characters_hairstyle = self.options.get("模特发型|Hairstyle",
                                                    {}).get(Hairstyle, "")
        if BodyType != "None":
            characters_bodytype = self.options.get("模特体型|Body type",
                                                   {}).get(BodyType, "")
        if Action != "None":
            characters_action = self.options.get("模特动作|Action",
                                                 {}).get(Action, "")

        if SceneSpring != "None":
            scene_template = self.options.get("场景Scene_spring",
                                              {}).get(SceneSpring, "")
        if SceneSummer != "None":
            scene_template = self.options.get("场景Scene_summer",
                                              {}).get(SceneSummer, "")
        if SceneAutumn != "None":
            scene_template = self.options.get("场景Scene_autumn",
                                              {}).get(SceneAutumn, "")
        if SceneWinter != "None":
            scene_template = self.options.get("场景Scene_winter",
                                              {}).get(SceneWinter, "")
        if SceneT != "None":
            scene_template = self.options.get("场景Scene_T", {}).get(SceneT, "")
        if SceneRoom != "None":
            scene_template = self.options.get("场景Scene_room",
                                              {}).get(SceneRoom, "")
        if SceneSimple != "None":
            scene_template = self.options.get("场景Scene_simple",
                                              {}).get(SceneSimple, "")
        if SceneOffice != "None":
            scene_template = self.options.get("场景Scene_office",
                                              {}).get(SceneOffice, "")
        if SceneGuizhou != "None":
            scene_template = self.options.get("场景Scene_Guizhou",
                                              {}).get(SceneGuizhou, "")

        if Hat != "None":
            hat_color = self.options.get("颜色Color", {}).get(HatColor, "")
            hat = self.options.get("帽子Flux", {}).get(Hat, "")
            byz_clothes.append(f"Wearing a ({hat_color} {hat}:{Hat_weight})")
        if Clothes != "None":
            pattern = self.options.get("图案Patterns",
                                       {}).get(ClothesPattern, "")
            color = self.options.get("颜色Color", {}).get(ClothesColor, "")
            cloth = self.options.get("衣服Flux", {}).get(Clothes, "")
            byz_clothes.append(
                f"Wearing a ({color} {pattern} {cloth}:{Clothes_weight})")
        if Pants != "None":
            color = self.options.get("颜色Color", {}).get(PantsColor, "")
            value = self.options.get("裤子", {}).get(Pants, "")
            byz_clothes.append(f"Wearing a ({color} {value}:{Pants_weight})")
        if Shoes != "None":
            color = self.options.get("颜色Color", {}).get(ShoesColor, "")
            value = self.options.get("鞋子", {}).get(Shoes, "")
            byz_clothes.append(f"Wearing a ({color} {value}:{Shoes_weight})")
        if Backpack != "None":
            color = self.options.get("颜色Color", {}).get(BackpackColor, "")
            value = self.options.get("背包", {}).get(Backpack, "")
            byz_clothes.append(
                f"Wearing a ({color} {value}:{Backpack_weight})")
        if OtherClothes:
            byz_clothes.append(OtherClothes)

        if scene_template == '':
            scene_template = '{clothes}'
        byz_clothes = ", ".join(byz_clothes)

        clip_prefix = []
        if image_style:
            clip_prefix.append(image_style)
        if image_characters:
            clip_prefix.append(image_characters)
        clip_prefix = ",".join(clip_prefix)

        t5xxl = scene_template.format(clothes=byz_clothes)
        clip_l = f'{clip_prefix},{byz_clothes}'

        style_prefix = []
        if image_style:
            style_prefix.append(image_style)
        if image_characters:
            style_prefix.append(image_characters)
        if characters_hairstyle:
            style_prefix.append(characters_hairstyle)
        if characters_bodytype:
            style_prefix.append(characters_bodytype)
        if characters_expressions:
            style_prefix.append(characters_expressions)
        if characters_eyes:
            style_prefix.append(characters_eyes)
        if characters_action:
            style_prefix.append(characters_action)

        style_suffix = []
        if image_composition:
            style_suffix.append(image_composition)

        if style_prefix:
            style_prefix = ",".join(style_prefix)
        else:
            style_prefix = ''

        if style_suffix:
            style_suffix = ",".join(style_suffix)
        else:
            style_suffix = ''

        t5xxl = f"{style_prefix},{t5xxl},{style_suffix}"
        #prompt = prompt.lower()

        #negative_prompt = "NSFW,drawing,painting,crayon,sketch,graphite,impressionist,noisy,blurry,soft,deformed,ugly,(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4),text,close up,cropped,out of frame,worst quality,low quality,jpeg artifacts,ugly,duplicate,morbid,mutilated,extra fingers,mutated hands,poorly drawn hands,poorly drawn face,mutation,deformed,blurry,dehydrated,bad anatomy,bad proportions,extra limbs,cloned face,disfigured,gross proportions,malformed limbs,missing arms,missing legs,extra arms,extra legs,fused fingers,too many fingers,long neck,((nsfw)),sketches,tattoo,(beard:1.3),(EasyNegative:1.3),badhandv4,(worst quality:2),(low quality:2),(normal quality:2),lowers,normal quality, facing away,looking away,text,error,extra digit,fewer digits,cropped,jpeg artifacts,signature,watermark,username,blurry,skin spots,acnes,skin blemishes,bad anatomy,fat,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,tilted head.bad anatomy.bad hands,extra fingers,fewer digits.,extra limbs.extra arms,extra legs,malformed limbs.fused fingers,too many fingers,long neck,cross-eyed,mutated hands,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit,extra arms,extra leg,extra foot,missing fingers,(Worst quality,low quality,lowres:1.2),error,cropped,jpeg artifacts,out of frame,watermark,signature, (worst quality, low quality,nsfw,nipple, pussy:1.3)"

        return (
            clip_l,
            t5xxl,
        )
