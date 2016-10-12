$(function(){
	
	var index={
		init:function(){
			//首页浮层
			$('.buts_1').click(function(){
				$('.index_dialog').removeClass('none');
				$('.index_dialogWrap').addClass('active');
			})
				//关闭弹层
			
			$('.close_a1').click(function(){
				$('.index_dialog').addClass('none');
				$('.index_dialogWrap').removeClass('active');
			});
		},
		rule:function(){
			//活动规则
			$('.buts_3').click(function(){
				$('.dialog_wrap').removeClass('none');
				$('.dialog').addClass('active');
			})
				//关闭弹层
			
			$('.close_a').click(function(){
				$('.dialog_wrap').addClass('none');
				$('.dialog').removeClass('active');
			});
			
		}
		
	};
	index.init();
	index.rule();
})


