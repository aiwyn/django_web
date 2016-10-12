$(function(){
	
	
	var New={
		init:function(){
			//首页浮层
			$('.rule').click(function(){
				$('.dialog').removeClass('none');
				$('.dialog_wrap').addClass('active');
			})
				//关闭弹层
			$('.close').hover(function(){
				$(this).css({transform: 'scale(1.1)'})
			},function(){
				$(this).css({transform: 'scale(1)'})
			})
			$('.close').click(function(){
				$('.dialog').addClass('none');
				$('.dialog_wrap').removeClass('active');
			});
		},
		newData:function(){
			
			$.ajax({
					type : 'GET',
					async : true,
					url : "{{ static_url }}pc/js/new_data.js",
					data:{},
					dataType : "json",
					success : function(data) {
						console.log(data)
						var data=data.list;
						for(var i=0;i<data.length;i++){
							$('.hd li').eq(i).find('img').attr("src",data[i].smallImg);
							$('.bd li').eq(i).find('a img').attr("src",data[i].begImg);
							$('.bd li').eq(i).find('.title a').html(data[i].title);
						}
					},
					error:function(jqXHR){
						alert("数据请求失败，请稍后重试")
						return false;
					}
				});
			
			
			
		}
	};
	New.init();
	New.newData();
	
	
	
	
})
