(function($){
	
	H.register={
		init:function(){
			This=this;
			This.reg();
		},
		reg:function(){
			//上传照片
			var Files='';
			var canvas = document.getElementById('canvas');
		    //var h =Math.ceil(window.screen.availHeight*0.45);
			//canvas.setAttribute("height",h);
			//canvas.setAttribute("width",BoxW-4);
			
			var photoCanvas = new PhotoCanvas('canvas', 60,60);
		    var file = document.getElementById('File');
			file.onchange=function(){
				canvas.setAttribute('data-buts','true');
				if(this.files[0].type.split('/')[0]!='image'){
					showTips("请上传照片格式为jpg的图片");
					return false;
				}
				if(this.files[0].size/1024>5000){
					showTips("请上传图片大小小于5M的图片");
					return false;
				}
				photoCanvas.loadFile(this.files[0]);
			}
			
		$('#login_p').click(function(){
			var Name=$('.name').val().trim();
			var Pass=$('.pass').val().trim();
			var Phone=$('.phone').val().trim();
			var address=$('.address').val().trim();
			var sex=$('input[type=radio]:checked').val();
			if($('#canvas').attr('data-buts')!='true'){
				showTips("请上传头像");
				return false;
			}
			if(Name==""){
				showTips("请填写用户名");
				return false;
			}
			if(Pass==""){
				showTips("请填写用户密码");
				return false;
			}
			if(Pass.length<6){
				showTips("密码长度不少于6个数");
				return false;
			}
			var ph=/^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
			if(!ph.test(Phone)){
				showTips("手机号码不能为空或填写不正确");
				return false;
			}
			if(address==""){
				showTips("请填写地址");
				return false;
			}
			if(address.length<5||address.length>60){
				showTips("地址长度应在5到60个字");
				return false;
			}
			
			var formdata = new FormData();
			formdata.append("nickname",Name);
			formdata.append("usernum",Phone);
			formdata.append("usraddr",address);
			formdata.append("passwd",hex_md5(Pass));
			formdata.append("sex",sex);
			formdata.append("display",photoCanvas.toImageFile());
			console.log(photoCanvas.toImageFile())
			setTimeout(function(){
				$.ajax({
				type : 'POST',
				async : false,
				timeout:20000,
				url : "register",
				data:formdata,
				dataType : "json",
	        	contentType: false,
	        	processData: false,
				success : function(data) {
					if(data.result_code==0){
						showTips('注册成功');
						setTimeout(function(){
							window.location.href="activelogin";
						},1000)
					}else if(data.result_code==1){
						showTips(data.result_msg);
					}
					else{
						showTips('注册失败');
					}
					
				},
				error:function(jqXHR,textStatus){
					if(textStatus=="timeout"){  
                        showTips("请求超时，请重试"); 
                        return false;
                    }
					alert(jqXHR.responseText);
					return false;
				}
			});
			
			},100)
			
		})
			
			
		},
	}
	
})(Zepto)

$(function() {
	H.register.init();
});
