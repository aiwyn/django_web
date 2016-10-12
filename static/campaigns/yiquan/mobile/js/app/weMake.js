(function($) {
	H.weMark = {
		firStep:$('#firStep'),
		nextBut:$('.nextBut'),
		nextStep:$('#nextStep'),
		nestButs:$('.nestButs'),
		list:$('.list'),
		upload_but:$('.upload_but'),
		back_a:$('.back_a'),
		mainLleftP:$('.main_left span'),
		mainRightP:$('.main_right span'),
		canvas_img:$('.canvas_img img'),
		dressModel:'',//衣服型号
		dressColor:'',//衣服颜色
		init: function() {
			This=this;
			
			This.Click();
			
		},
		ScrollFun:function(){
			
			var parent_div=$('.list').eq(0);
			var chile_div=$('.list ul').eq(0);
			var Div_height=parent_div.height();
			var Ul_height=chile_div.height();
			var chaH=Ul_height-Div_height;
			var IndexY=0,MoveY=0,Scllo=0;
			console.log(parent_div.height())
			console.log(Ul_height)
			if(chaH>0){
				parent_div.bind('touchstart',function(e){
					
					IndexY=e.originalEvent.changedTouches[0].clientY;
					Scllo=parent_div.scrollTop();
				})
				$('body').bind('touchmove',function(e){
						MoveY=IndexY-e.originalEvent.changedTouches[0].clientY;
						parent_div.scrollTop(Scllo+MoveY);
						e.preventDefault();
					});
				
				$('body').bind('touchend',function(e){
					parent_div.scrollTop(Scllo+MoveY);
					e.preventDefault();
				})	
			}
				
			
		},
		Click:function(){
			This=this;
			var i=0;
			
			This.firStep.find("span").click(function(){
				i++;
			});
			This.nextBut.click(function(){
				console.log(i)
				if(i==0){
					This.Tip('make6');
					return false;
				}
				This.firStep.addClass("none");
				$('.firstStep_but').addClass('none');
				This.nextStep.removeClass('none');
				This.nestButs.removeClass('none');
				This.Tip('make15');
				//This.ScrollFun();
				return false;
			});
			
			This.back_a.click(function(){
				This.firStep.removeClass("none");
				$('.firstStep_but').removeClass('none');
				This.nextStep.addClass('none');
				This.nestButs.addClass('none');
			});
			
			
			
			
		},
		Tip:function(imgName){
			var t = simpleTpl();
         		t._('<div class="dialog_img">')
						._('<div class="make_dialog">')
							._('<em><img src="img/'+imgName+'.png"/></em>')
						._('</div>')
				._('</div>')
        	
        	$('body').append(t.toString());
        	$('.dialog_img').addClass('active');
        	var Time=setTimeout(function(){
        		$('.dialog_img').remove()
        	},3000);
        	
        	$('.dialog_img').bind("click",function(){
				$('.dialog_img').remove();
				clearTimeout(Time);
			})
        	
			
		},
		
		
		
		
		
	};
})(Zepto);

$(function() {
	var image = new Image();
    image.onload = function() {
    	var ImgH=new Image()
    	var Height=$('.em1').height();
    	var Width=$('.em1').width();
    	$('.canvas_img').height(Height);
    	$('.canvas_img').width(Width);
    	H.weMark.init();
    };
    image.src = "img/yifu/1.png";
	
	
	
});