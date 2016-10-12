$(function(){
	/*点击切换底色*/
	$('.buts span').click(function(){
		var This=$(this).index();
		$('.lists .list').eq(This).removeClass('none').siblings('div').addClass('none')
	})
	
	
	var j=0;
	$('.solider_div li').click(function(){
		j++;
	})
	//点击出现弹层
		$('.sub1').bind('click',function(){
			if(j==0){
				Diolag('.dialog_wrap',"请至少选择一项制作元素")
				return false;
			}else{
				$('.box2').removeClass('none');
				$('.box1').addClass('none');
			}
		})
		//关闭弹层
		$('.close_a').click(function(){
			$('.dialog_wrap').addClass('none');
			$('.dialog').removeClass('active');
		})
})
function Diolag(obj,text){
		//点击出现弹层
		$(obj).removeClass('none');
		$(obj).addClass('active');
		$(".dialog_wrap .content h1").html(text);
		//关闭弹层
		
		$(obj).find('.close_a').click(function(){
			$(obj).addClass('none');
			$(obj).find('.dialog').removeClass('active');
		})
	};
	
