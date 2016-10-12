function DIYCanvas(canvasId, groupClassName, width, height, cornerSize, zoomValue, borderColor) {
    this.canvas = new fabric.Canvas(canvasId, {
        selection: false,
        enableRetinaScaling: true
    });
    this.canvas.setDimensions({width: width, height: height});
    if (typeof zoomValue === "undefined")
        zoomValue = 1;
    zoomValue && this.canvas.setZoom(zoomValue);
    this.groupClassName = groupClassName;
    this.cornerSize = cornerSize;
    this.zoomValue = zoomValue;
    this.borderColor = borderColor;
}
DIYCanvas.prototype = {
    _toDataURL: function(multiplier) {
        return this.canvas.toDataURL({
            format: 'png',
            quality: 1,
            multiplier: multiplier
        });
    },
    addKit: function(imgObj, top, left) {
        var imageObj = new Image();
        imageObj.onload = function() {
            var kitGroup = imgObj.getAttribute('data-kit-group');
            var kitIndex = imgObj.getAttribute('data-kit-index');
            for (var i = 0, length = this.canvas.size(); i < length; ++i) {
                var kit = this.canvas.item(i);
                if (kit.kitGroup == kitGroup) {
                    if (kit.kitIndex !== kitIndex) {
                        kit.setElement(imageObj);
                        kit.setCoords();
                        kit.kitIndex = kitIndex;
                        this.canvas.renderAll();
                    }
                    return;
                }
            }
            if (typeof top === "undefined") top = 0;
            if (typeof left == "undefined") left = 0;
            var kitStyle = imgObj.getAttribute('data-kit-style');
            var imgInstance = new fabric.Image(imageObj, {
                left: left,
                top: top,
                cornerSize: this.cornerSize * this.zoomValue,
                borderColor: this.borderColor,
                rotatingPointOffset: 0,
                lockScalingFlip : true,
                minScaleLimit: 0.5
                //perPixelTargetFind: true,
                //targetFindTolerance: 4
            });
            if (kitStyle === "static") {
                imgInstance.selectable = imgInstance.hasControls = imgInstance.hasBorders = false;
            }
            imgInstance.setControlsVisibility({'mb': false, 'mt': false, 'ml': false, 'mr': false, 'br': false});
            imgInstance.kitGroup = kitGroup;
            imgInstance.kitIndex = kitIndex;
            this.canvas.add(imgInstance);
        }.bind(this);
        imageObj.src = imgObj.src;
    },
    toImageFile: function(multiplier) {
        if (!multiplier) multiplier = 1;
        var dataURL = this._toDataURL(multiplier);
        var arr = dataURL.split(','), mime = arr[0].match(/:(.*?);/)[1],
            bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
        while(n--){
            u8arr[n] = bstr.charCodeAt(n);
        }
        return new Blob([u8arr], {type:mime});
    },
    toImageSrc: function(multiplier) {
        if (!multiplier) multiplier = 1;
        return this._toDataURL(multiplier);
    },
    toFeatureJson: function() {
        var kitList = [];
        for (var i = 0, length = this.canvas.size(); i < length; ++i) {
            var kit = this.canvas.item(i);
            var index = kit.kitIndex;
            var rect = kit.getBoundingRect();
            var angle = kit.angle || 0;
            var scale = kit.scaleX || 1;
            var kitFeature = {
                'index': index,
                'x': rect['left'],
                'y': rect['top'],
                'angle': angle,
                'scale': scale
            };
            kitList.push(kitFeature);
        }
        return JSON.stringify(kitList);
    },
    activate: function() {
        var self = this;
        var imgObjList = document.getElementsByClassName(this.groupClassName);
        for (var i = 0, length = imgObjList.length; i < length; ++i) {
            var imgObj = imgObjList[i];
            imgObj.onclick = function() {
                self.addKit(this);
            }
        }
    },
    deactivate: function() {
        this.canvas.deactivateAll();
    },
    clear: function() {
        this.canvas.clear();
    }
};
