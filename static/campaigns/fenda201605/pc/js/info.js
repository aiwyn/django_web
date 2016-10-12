$(function(){
	

	
	function Diolag(obj,text){
		//点击出现弹层
		$(obj).removeClass('none');
		$(obj).find('.dialog').addClass('active');
		$(".dialog_wrap .content h1").html(text);
		//关闭弹层
		$(obj).find('.close_a').hover(function(){
			$(this).css({transform: 'rotate(180deg)'})
		},function(){
			$(this).css({transform: 'rotate(0deg)'})
		})
		$(obj).find('.close_a').click(function(){
			$(obj).addClass('none');
			$(obj).find('.dialog').removeClass('active');
		})
	};
	
	
	$('.cj_submit').click(function(){
		
		var Name=$('.name').val().trim();
		var Phone=$('.phone').val().trim();
		var WorkName=$('.workName').val().trim();
		var Yx=$('.yx').val().trim();
		if(Name==""){
			Diolag('.dialog_wrap',"请填写姓名")
			return false;
		}
		var ph=/^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
		if(!ph.test(Phone)){
			Diolag('.dialog_wrap',"手机号码不能为空或填写不正确")
			return false;
		}
		if(WorkName==""){
			Diolag('.dialog_wrap',"请填写作品名")
			return false;
		}
		if(Yx==""){
			Diolag('.dialog_wrap',"请填写院校名")
			return false;
		}
		
		$.ajax({
			type : 'GET',
			async : false,
			url : "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=vv1&json=1&p=3&sid=1467_19556_18241_19690_17944_18205_19559_17001_15636_11753_19368_10632&req=2&csor=0&cb=jQuery110205150351876243915_1460608238093&_=1460608238099",
			data: {
					name:Name,
					phone:Phone,
					WorkName:WorkName,
					Yx:Yx
					},
			dataType : "jsonp",
			jsonpCallback : "jQuery110205150351876243915_1460608238093",
			success : function(data) {
				window.location.href="works.html";
			},
			error:function(){
				alert("数据请求失败，请稍后再试")
			}
		});
		
		
		
		
		
	})
	
	
	
})
