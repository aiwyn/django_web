$(function(){
	
//	function Diolag(obj){
//		//点击出现弹层
//		$(obj).removeClass('none');
//		$(obj).find('.dialog').addClass('active');
//		//关闭弹层
//		
//		$(obj).find('.close_a').click(function(){
//			$(obj).addClass('none');
//			$(obj).find('.dialog').removeClass('active');
//		})
//	};
//	
	
	function Diolag(obj,text){
		//点击出现弹层
		$(obj).removeClass('none');
		$(obj).addClass('active');
		$(".dialog_wrap .content p").html(text);
		//关闭弹层
		
		$(obj).find('.close_a').click(function(){
			$(obj).addClass('none');
			$(obj).find('.dialog').removeClass('active');
		})
	};
	
	
	//上传照片
	var File=document.getElementById("File");
	var Files='';
	
	var box_canvas=document.getElementById('box_canvas');
	 var canvas = document.getElementById('canvas');
	var BoxW=box_canvas.offsetWidth-1;
	
    var h =Math.ceil(window.screen.availHeight*0.45);
	canvas.setAttribute("height",h);
	canvas.setAttribute("width",BoxW-4);
	
	File.onchange=function(){
		if(this.files[0].type.split('/')[1]!='jpeg'){
			Diolag(".dialog_wrap","请上传照片格式为jpg的图片");
			return false;
		}
		if(this.files[0].size/1024>5000){
			Diolag(".dialog_wrap","请上传图片大小小于5M的图片");
			return false;
		}
		Files=this.files[0];
		load_image();
		$('.img2').removeClass('none');
		$('.img1').addClass('none');
	}
	
	
	//画图
var image_file='';
function load_image() {
    image_file = document.getElementById("File").files[0];
    if (!image_file.type.match(/image.*/)) {
        alert("只能选择图片文件");
        return;
    }
    var file_reader = new FileReader();
    file_reader.onload = function() {
        var image = new Image();
        image.onload = function() {
        	var wrap_center=document.getElementById('wrap_center');
        	
        	box_canvas.style.background='none';
            var canvas = document.getElementById('canvas');
            var context = canvas.getContext("2d");
            context.clearRect(0,0,BoxW,h);
            var imgH=this.height;
            var imgW=this.width;
            var scaleH =1- (imgW-h)/imgW;    
            imgH = imgH*scaleH;
            var topY=(h-imgH)/2;
            context.drawImage(image, 0, topY,BoxW,imgH);
        };
        image.src = file_reader.result;
    };
    file_reader.readAsDataURL(image_file);

}
	
	
	
	//点击确认提交
	
	$('.qrtj').click(function(){
		if(!$('.img1').hasClass('none')){
			Diolag(".dialog_wrap","请上传照片");
			return false;
		}
		$('.main_box1').addClass('none');
		$('.main_box2').removeClass('none')
	})
	
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
	
	
	
	//点击确认上传
	
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
			formdata.append("authorCellphone",Phone);
			formdata.append("workName",WorkName);
			formdata.append("authorSchool",Yx);
			formdata.append("workImage",Files);
			$('body').append('<div class="dendai"><i><img src="/static/campaigns/fenda201605/mobile/img/jiazai.jpg"/></i></div>')
			$.ajax({
				type : 'POST',
				async : false,
				url : "uploadPhotoWork",
				data:formdata,
				dataType : "json",
	        	contentType: false,
	        	processData: false,
	        	complete: function() {
					$(".dendai").remove();
				},
				success : function(data) {
					window.location.href="resulted.html?workId="+data.workId;
				},
				error:function(jqXHR){
					if(jqXHR.status==400){
						alert(jqXHR.status+":"+jqXHR.responseJSON.errorMessage);
						return false;
					}
					if(jqXHR.status==404){
						alert(jqXHR.status+":"+jqXHR.responseJSON.errorMessage);
						return false;
					}
					if(jqXHR.status==500){
						alert(jqXHR.status+":"+jqXHR.responseJSON.errorMessage);
						return false;
					}
					if(jqXHR.status==501){
						alert(jqXHR.status+":"+jqXHR.responseJSON.errorMessage);
						return false;
					}
					alert("数据请求失败，请稍后再试");
					return false;
				}
			});
			
		})
			
			
		
	
	
	
	
	
	
	
	
})
