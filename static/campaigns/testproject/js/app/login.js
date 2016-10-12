(function($){
	H.login={
		expires_in:30,
		init:function(){
			This=this;
			if($.fn.cookie("_Phone")!=''){
				$('.phone').val($.fn.cookie("_Phone"))
			}
			This.Login();
		},
		Login:function(){
			
			$('#login_p').click(function(){
				var Pass=$('.pass').val().trim();
				var Phone=$('.phone').val().trim();
				var ph=/^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
				if(!ph.test(Phone)){
					showTips("手机号码不能为空或填写不正确");
					return false;
				}
				
				if(Pass==""){
					showTips("请输入用密码");
					return false;
				}
				console.log(hex_md5(Pass))
				//$.fn.cookie("Pass" + '_city', city, H.login.expires_in);
				$.ajax({
					type : 'POST',
					async : true,
					timeout:20000,
					url : "login",
					data:{
						usernum:Phone,
						passwd:hex_md5(Pass)
					},
					dataType : "json",
					success : function(data) {
						if(data.result_code==0){
							$.fn.cookie("_Phone", Phone, H.login.expires_in);
							window.location.href="index";
						}else{
							showTips(data.result_msg)
						}
					},
					error:function(jq,textStatus){
						if(textStatus=="timeout"){
							showTips("请求超时，请重试"); 
	                        return false;
						}
						alert(jq.responseText);
						return false;
					}
				})	
			})
		}
	}
})(Zepto)
$(function(){
	H.login.init();
})
