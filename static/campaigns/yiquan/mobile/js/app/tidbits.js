(function($) {
	H.mark = {
		i_img_1:$("footer i").eq(0),
		i_img_2:$("footer i").eq(1),
		init: function() {
			This=this;
			This.Swipe()
			This.Click()
		},
		Swipe:function(){
			//头部动画切换效果
			var mySwiper = new Swiper('.swiper-container',{
				    pagination: '.pagination',
				    loop:true,
				    grabCursor: true,
				    paginationClickable: true
//				    onSlideChangeStart:function(swiper){
//				    	funEnd();
//				    	Num(H.interaction.cj); 
//				    }
				  })
			//左右点击切换
//	 		$('.arrow-left').on('click', function(e){
//			    e.preventDefault()
//			    mySwiper.swipePrev()
//			  })
//			  $('.arrow-right').on('click', function(e){
//			    e.preventDefault()
//			    mySwiper.swipeNext()
//			  })
			
			
		},
		Click:function(){
			This=this;
			This.i_img_1.bind("click",function(){
				This.Tip(1)
			});
			
			This.i_img_2.bind("click",function(){
				This.Tip(2)
			});
		},
		Tip:function(num){
			var t = simpleTpl();
         		t._('<div class="dialog_img">')
					._('<div class="dialog_wrap">')
						._('<div>')
							._('<em><img src="img/hx/tidbits-'+num+'.png"/></em>')
						._('</div>')
					._('</div>')
				._('</div>')
        	
        	$('body').append(t.toString());
        	$('.dialog_img').addClass('active');
        	$('.dialog_img').bind("click",function(){
				console.log(11)
				$('.dialog_img').remove()
			})
			
		}
	};
})(Zepto);

$(function() {
	H.mark.init();
});