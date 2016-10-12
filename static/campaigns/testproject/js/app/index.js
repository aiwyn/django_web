(function($){
	H.index={
		userId:getQueryString('userId'),
		init:function(){
			This=this;
			This.GetInfo();
			This.Sign();
			This.logOff();
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
					if(data.result_code==2){
						window.location.href='activelogin';
						return false;
					}
					if(data.result_code==0){
						$('.Sign').addClass('none');
						$('.signend').removeClass('none');
					}
					$('#userDisplay').attr('src',data.display);
					$('.userName').html(data.nickname);
					$('.phone').html(data.usernum);
					$('.address').html(data.usraddr);
					if(data.point==null){
						data.point=0;
					}
					$('.jf').html(data.point);
					if(data.continuity==null){
						data.continuity=0;
					}
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
					url : "signed",
					data:{
						userId:H.index.userId
					},
					dataType : "json",
					success : function(data) {
						var jf=parseInt( $('.jf').html() );
						var continuity=parseInt( $('.day').html() )+1;
						var fs=1;
						if(continuity==7){
							fs=5;
						}
						if(continuity/30==0){
							fs=10;
						}
						$('.day').html(continuity+'天');
						$('.jf').html(jf+fs);
						$('.Sign').addClass('none');
						$('.signend').removeClass('none');
						showTips('签到成功');
						
						var t = simpleTpl();
						t._('<div id="goLottery">')
							._('<div class="goLotBox">')
								._('<h1>获得一次免费抽奖机会</h1>')
								._('<p><a class="p_close">关闭</a><a class="p_but" href="lottery.html">抽奖</a></p>')
							._('</div>')
						._('</div>');
						
						$('body').append(t.toString());
						$('.p_close').remove('#goLottery');
						
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
		},
		logOff:function(){
			
			$('.logOff').click(function(){
				
				$.ajax({
					type:"get",
					url:"cancellation",
					async:true,
					success:function(data){
						//console.log(data);
						$.fn.cookie('_Phone','',-1);
						window.location.href="activelogin";
					},
					error:function(jq){
						alert(jq.responseText);
						return false;
					}
				});
				
			})
			
			
		}
	}
})(Zepto)

$(function(){
	H.index.init();
})
