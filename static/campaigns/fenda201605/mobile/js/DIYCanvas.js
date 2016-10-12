function DIYCanvas(canvasId, width, height, cornerSize, zoomValue, borderColor) {
    this.canvas = new fabric.Canvas(canvasId, {
        selection: false,
        enableRetinaScaling: true
    });
    this.canvas.setDimensions({width: width, height: height});
    if (typeof zoomValue === "undefined")
        zoomValue = 1;
    zoomValue && this.canvas.setZoom(zoomValue);
    this.cornerSize = cornerSize;
    this.zoomValue = zoomValue;
    this.borderColor = borderColor;
}
DIYCanvas.prototype = {
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
                rotatingPointOffset: 0
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
    toImageFile: function() {
        var dataURL = this.canvas.toDataURL("image/png");
        var arr = dataURL.split(','), mime = arr[0].match(/:(.*?);/)[1],
            bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
        while(n--){
            u8arr[n] = bstr.charCodeAt(n);
        }
        return new Blob([u8arr], {type:mime});
    },
    toImageSrc: function() {
        return this.canvas.toDataURL("image/png");
    }
};

function start(w,h,W,H,BoxW) {
	
	
    var bg1 = document.getElementById('bg1');
     var diyCanvas='';
    if(W==320 && H<=480){
    	 diyCanvas= new DIYCanvas('canvas', BoxW, h, 40, 0.4, 'red');
    	 diyCanvas.addKit(bg1,w/20,h/1);
    }
    else if(W==320 && H<=568){
    	 diyCanvas= new DIYCanvas('canvas',BoxW, h, 40, 0.5, 'red');
    	 diyCanvas.addKit(bg1,w/20,h/1.5);
    }
    else if(W<=375){
    	 diyCanvas= new DIYCanvas('canvas', BoxW, h, 40, 0.7, 'red');
    	 diyCanvas.addKit(bg1,w/10,h/3.4);
    }
    else if(W<=414){
    	 diyCanvas= new DIYCanvas('canvas', BoxW, h, 40, 0.8, 'red');
    	 diyCanvas.addKit(bg1,w/20,h/3.9);
    	 console.log(1)
    }
    else if(W<768){
    	 diyCanvas= new DIYCanvas('canvas', BoxW, h, 40,0.9, 'red');
    	 diyCanvas.addKit(bg1,w/24,h/4.5);
    	 console.log(2)
    }
    else  if(W>=768){
    	 diyCanvas= new DIYCanvas('canvas', BoxW, h, 40,1, 'red');
    	 diyCanvas.addKit(bg1,w/20,h/3.8);
    	 console.log(31)
    }else{
    	diyCanvas= new DIYCanvas('canvas',BoxW, h*0.8, 40, 0.5, 'red');
    	 diyCanvas.addKit(bg1,w/10,h/3.5);
    	 console.log(h)
    }
    diyCanvas.toImageFile()
    var imgObjList = document.getElementsByClassName('kit');
    for (var i = 0, length = imgObjList.length; i < length; ++i) {
        //var imgObj = imgObjList[i];
        imgObjList[i].onclick = function() {
            diyCanvas.addKit(this,w/2,h/5);
        }
    }
    var pro_canvas = document.getElementById('pro_canvas');
     var pro_img = document.getElementById('pro_img');
 	var final_but = document.getElementById("final_but");
 	var final_img=document.getElementById('final_img');
 	final_but.onclick=function(){
 		diyCanvas.canvas.deactivateAll();
 		//final_img.className='';
 		//pro_canvas.style.display="none";
 		//pro_img.style.display="block";
		//final_img.src = diyCanvas.toImageSrc();
		//console.log(diyCanvas.toImageFile())
 	}
 	
	
	
		//cookie设置
	function setCookie(name,value){ 
	　　var exp = new Date(); 
	　　exp.setTime(exp.getTime() + 1*60*60*1000);//有效期1小时 
	　　document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString(); 
	}
	
	function getCookie(name){
	　　var arr = document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
	　　if(arr != null)　　　　
	　　　　return unescape(arr[2]);
	　　return null;
	}
		
	if(getCookie('name')){
		$('.name').val(getCookie('name'))
	}
	if(getCookie('phone')){
		$('.phone').val(getCookie('phone'))
	}
	
	
	$('.sub2').click(function(){
		var Name=$('.name').val().trim();
			var Phone=$('.phone').val().trim();
			var WorkName=$('.workName').val().trim();
			var Yx=$('.yx').val().trim();
			if(Name==""){
				Diolag('.dialog_wrap',"请填写姓名")
				return false;
			}
			setCookie("name",Name);
			var ph=/^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
			if(!ph.test(Phone)){
				Diolag('.dialog_wrap',"手机号码不能为空或填写不正确")
				return false;
			}
			setCookie("phone",Phone);
			if(WorkName==""){
				Diolag('.dialog_wrap',"请填写作品名")
				return false;
			}
			if(Yx==""){
				Diolag('.dialog_wrap',"请填写院校名")
				return false;
			}
			var formdata = new FormData();
			
			formdata.append("authorName",Name);
			formdata.append("authorCellphone",Phone)
			formdata.append("workName",WorkName)
			formdata.append("authorSchool",Yx);
			formdata.append("workImage",diyCanvas.toImageFile());
			
			$.ajax({
				type : 'POST',
				async : false,
				url : "uploadDIYWork",
				data:formdata,
				dataType : "json",
	        	contentType: false,
	        	processData: false,
				success : function(data) {
					window.location.href="resulted.html?workId="+data.workId;
				},
				error:function(jqXHR){
					alert("数据请求失败，请稍后再试");
					return false;
				}
			});
			
		})
			
}

$(function() {
	var box_canvas=document.getElementById('box_canvas');
	var BoxW=box_canvas.offsetWidth;
    var image = new Image();
    var W =window.screen.availWidth;
    var H =window.screen.availHeight;
    var w =window.screen.availWidth*0.8;
     var h =window.screen.availHeight;
    if(h>568){
    	h =window.screen.availHeight*0.45;
    }else{
    	h =window.screen.availHeight*0.35;
    }
    image.onload = function() {
        fabricCustom.loadImageObj(this);
        start(w,h,W,H,BoxW);
    };
    image.src = "/static/campaigns/fenda201605/mobile/img/control.png";
});