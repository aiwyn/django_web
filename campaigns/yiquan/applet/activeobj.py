from campaigns.foundation.const import FoundationConst
from campaigns.yiquan import models
from campaigns.yiquan.applet import utils
import time, random
from PIL import Image

class addwork(object):
    def add_kit_to_canvas(self, canvas, kit, x, y, scale, angle):
        if scale != 1:
            width = kit.width
            print width
            height = kit.height
            print height
            kit = kit.resize((int(width * scale), int(height * scale)), resample=Image.BILINEAR)
        if angle != 0:
            angle = 360 - angle
            kit = kit.rotate(angle, resample=Image.BILINEAR, expand=True)
        mask = Image.merge("L", (kit.split()[3],))
        canvas.paste(kit, (x, y), mask)

    def prepare_image_list(self, kit_filename_list, root_path=None):
        if root_path is not None:
            self.kit_filename_list = [root_path + kit_filename for kit_filename in kit_filename_list]
        return [Image.open(kit_filename).convert(FoundationConst.RN_RGBA) for kit_filename in kit_filename_list]

    def generate_filename_list(self):
        filename_list = []
        abs_path = "/www/project/simagedir/"
        for i in range(1, 16):
            filename_list.append('{}t{}.png'.format(abs_path, i))
        for i in range(1, 35):
            filename_list.append('{}{}.png'.format(abs_path, i))
        return filename_list

    def regenerate_image_by_feature_list(self, feature_list, raw_width, raw_height, source_image_list, des_width, des_height):
        canvas = Image.new(FoundationConst.RN_RGBA, (des_width, des_height), (0, 0, 0, 0))
        for feature in feature_list:
            index = int(feature[FoundationConst.RN_INDEX])
            x = int(float(feature[FoundationConst.RN_X]))
            y = int(float(feature[FoundationConst.RN_Y]))
            scale = float(feature[FoundationConst.RN_SCALE])
            angle = float(feature[FoundationConst.RN_ANGLE])
            print source_image_list[index]
            self.add_kit_to_canvas(canvas, source_image_list[index], x, y, scale, angle)
        return canvas

    def regenerate(self, feature_list):
        source_image_list = self.prepare_image_list(self.generate_filename_list())
        work_image = self.regenerate_image_by_feature_list(
            feature_list, 450, 636,
            source_image_list, 450, 636
        )
        full_filename = '{}{}.png'.format("media/campaigns/yiquan/work/image", utils.generate_uuid())
        work_image.save(full_filename)
        return full_filename

    def __init__(self, _addwork):
        self._addwork = _addwork
        if int(self._addwork.count) > 0:
            maxcount = int(self._addwork.count)
            countwork = models.CheatWork.objects.create(
                id=int(time.time()),
                count=maxcount
            )
            while maxcount > 0:
                _size = random.randint(0, 3)
                _colors = random.randint(0, 3)
                l1 = list()
                _maxlist = random.randint(3, 5)
                while _maxlist > 0:
                    d1 = dict()
                    x = random.uniform(-44, 330)
                    y = random.uniform(-44, 491)
                    angle = random.uniform(1, 359)
                    scale = random.uniform(1, 2)
                    index = random.randint(1, 47)
                    d1['index'] = index
                    d1['x'] = x
                    d1['y'] = y
                    d1['angle'] = angle
                    d1['scale'] = scale
                    l1.append(d1)
                    _maxlist -= 1
                l2 = list()
                __maxlist = random.randint(1, 5)
                while __maxlist > 0:
                    d1 = dict()
                    x = random.uniform(-44, 330)
                    y = random.uniform(-44, 491)
                    angle = random.uniform(1, 359)
                    scale = random.uniform(1, 2)
                    index = random.randint(1, 47)
                    d1['index'] = index
                    d1['x'] = x
                    d1['y'] = y
                    d1['angle'] = angle
                    d1['scale'] = scale
                    l2.append(d1)
                    __maxlist -= 1
                sback = self.regenerate(l2)
                sfront = self.regenerate(l1)
                sback = sback.strip("media/")
                sfront = sfront.strip("media/")
                workcount = models.YQWork.objects.create(
                    ImageSBack=sback,
                    ImageSFront=sfront,
                    fixstatus=0,
                    openid="workadd",
                    ImageFront=str(l1),
                    ImageBack=str(l2)
                )
                printwork=models.PrintWork.objects.create(
                    workid=workcount.id,
                    printcode="workadd",
                    size=_size,
                    colors=_colors,
                    isprint=0,
                )
                maxcount -= 1