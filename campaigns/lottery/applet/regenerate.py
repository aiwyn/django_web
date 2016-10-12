# -*- coding: utf-8 -*-
from campaigns.foundation.applet import utils
from campaigns.yiquan.config import RegenerateConfig
from campaigns.foundation.applet.regenerate import prepare_image_list, regenerate_image_by_feature_list


def generate_filename_list():
    filename_list = []
    abs_path = RegenerateConfig.KIT_ABS_PATH
    for i in range(1, 16):
        filename_list.append('{}t{}.png'.format(abs_path, i))
    for i in range(1, 35):
        filename_list.append('{}{}.png'.format(abs_path, i))
    return filename_list


def regenerate(feature_list):
    source_image_list = prepare_image_list(generate_filename_list())
    work_image =  regenerate_image_by_feature_list(
        feature_list, RegenerateConfig.RAW_CANVAS_WIDTH, RegenerateConfig.RAW_CANVAS_HEIGHT,
        source_image_list, RegenerateConfig.DES_CANVAS_WIDTH, RegenerateConfig.DES_CANVAS_HEIGHT
    )
    full_filename = '{}{}.png'.format(RegenerateConfig.BIG_WORK_IMAGE_FILE_PATH, utils.generate_uuid())
    work_image.save(full_filename)
    return full_filename
