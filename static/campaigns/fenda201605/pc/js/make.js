//滚动
$(function(){
		/*五官滚动配置*/
	    var scrollPic_01 = new ScrollPic();
	    scrollPic_01.scrollContId= "ISL_Cont_1"; //内容容器ID
	    scrollPic_01.arrLeftId= "leftArrindex_1";//左箭头ID
	    scrollPic_01.arrRightId= "rightArrindex_1"; //右箭头ID
	    scrollPic_01.frameWidth= 350;//显示框宽度
	    scrollPic_01.pageWidth= 172; //翻页宽度
	    scrollPic_01.speed= 50; //移动速度(单位毫秒，越小越快)
	    scrollPic_01.space= 20; //每次移动像素(单位px，越大越快)
	    scrollPic_01.autoPlay=false; //自动播放
	    scrollPic_01.autoPlayTime= 3; //自动播放间隔时间(秒)
	    scrollPic_01.initialize(); //初始化			
	
	/*发型滚动配置*/
		var scrollPic_02 = new ScrollPic();
	    scrollPic_02.scrollContId= "ISL_Cont_2"; //内容容器ID
	    scrollPic_02.arrLeftId= "leftArrindex_2";//左箭头ID
	    scrollPic_02.arrRightId= "rightArrindex_2"; //右箭头ID
	    scrollPic_02.frameWidth= 350;//显示框宽度
	    scrollPic_02.pageWidth= 172; //翻页宽度
	    scrollPic_02.speed= 50; //移动速度(单位毫秒，越小越快)
	    scrollPic_02.space= 20; //每次移动像素(单位px，越大越快)
	    scrollPic_02.autoPlay=false; //自动播放
	    scrollPic_02.autoPlayTime= 3; //自动播放间隔时间(秒)
	    scrollPic_02.initialize(); //初始化	
	
	/*脸型滚动配置*/
	    var scrollPic_03 = new ScrollPic();
	    scrollPic_03.scrollContId= "ISL_Cont_3"; //内容容器ID
	    scrollPic_03.arrLeftId= "leftArrindex_3";//左箭头ID
	    scrollPic_03.arrRightId= "rightArrindex_3"; //右箭头ID
	    scrollPic_03.frameWidth= 350;//显示框宽度
	    scrollPic_03.pageWidth= 172; //翻页宽度
	    scrollPic_03.speed= 50; //移动速度(单位毫秒，越小越快)
	    scrollPic_03.space= 20; //每次移动像素(单位px，越大越快)
	    scrollPic_03.autoPlay=false; //自动播放
	    scrollPic_03.autoPlayTime= 3; //自动播放间隔时间(秒)
	    scrollPic_03.initialize(); //初始化	
	
//	/*点击切换底色*/
//	$('.small_pro i').click(function(){
//		var i=$(this).index();
//		$('.pro_beg img').attr('src','img/fd'+i+'.png');
//		
//	})
	

		//关闭弹层
		$('.close_a').hover(function(){
			$(this).css({transform: 'rotate(180deg)'})
		},function(){
			$(this).css({transform: 'rotate(0deg)'})
		})
		$('.close_a').click(function(){
			$('.dialog_wrap').addClass('none');
			$('.dialog').removeClass('active');
		})
			
		
		
	
		
	
	
	
	
})
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
