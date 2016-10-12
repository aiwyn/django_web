(function($){
	H.index={
		userId:getQueryString('userId'),
		init:function(){
			This=this;
			This.GetInfo();
			This.Sign();
		},
		GetInfo:function(){
			$.ajax({
				type : 'GET',
				async : true,
				timeout:20000,
				url : "center",
				data:{
					//userId:H.index.userId
				},
				dataType : "json",
				success : function(data) {
					if(data.result_code==0){
						$('.Sign').addClass('none');
						$('.signend').removeClass('none');
					}
					$('#userDisplay').attr('src',data.display);
					$('.userName').html(data.nickname);
					$('.phone').html(data.usrnum);
					$('.usraddr').html(data.address);
					$('.jf').html(data.point);
					$('.day').html(data.continuity+'天');
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
		},
		Sign:function(){
			$('.Sign').click(function(){
				
				$.ajax({
					type : 'POST',
					async : true,
					timeout:20000,
					url : "management/signed",
					data:{
						userId:H.index.userId
					},
					dataType : "json",
					success : function(data) {
						var jf=parseInt( $('.jf').html() );
						$('.jf').html(jf+data.jf);
						$('.Sign').addClass('none');
						$('.signend').removeClass('none');
						showTips('签到成功');
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
	H.index.init();
})
