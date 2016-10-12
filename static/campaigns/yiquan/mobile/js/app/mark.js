(function($) {
	H.mark = {
		
		init: function() {
			This=this;
			var Height=$('#fenshu').width();
			$('#fenshu').height(Height);
			This.Html();
			This.Swipe();
		},
		Swipe:function(){
		
			var swipe1=document.getElementById('swipe1');
			var swipe2=document.getElementById('swipe2');
			var moveY=0,StartY=0;
			swipe1.ontouchstart=function(e){
				var ev=e||window.event;
				StartY=ev.changedTouches[0].clientY;
				document.ontouchmove=function(e){
					var ev=e||window.event;
					moveY=ev.changedTouches[0].clientY-StartY;
					e.preventDefault()
				}
				document.ontouchend=function(){
					if(-moveY>50){
						swipe2.style.top="0%";
						document.ontouchmove=null;
						document.ontouchend=null;
					}
					e.preventDefault()
				}
			}
		},
		Html:function(){
			var num=getQueryString("num");
			var fs=getQueryString("fs");
			//console.log(num)
			$('#fenshu>i:last-of-type').find("img").attr('src','img/mark_text'+num+'.png');
			var pi=$('#fenshu>i:nth-child(2)')
			var Img1=$('.img1 img'),Img2=$('.img2 img');
			var fo=fs/10;
			var remainder=fs%10;
			var i=0,j=0;
			var Time=setInterval(function(){

				i++;
				if(i>=fs){
					clearInterval(Time)
				}

				if( (i%10)>=9 && j<fo ){
					j++;
					if(j==10) j=9;
					Img1.attr('src','img/shuzi/'+j+'.png');
				}
				Img2.attr('src','img/shuzi/'+(i%10)+'.png');
				pi.css({
					transform: 'rotate('+(3.6*i)+'deg)'
				})
			},30)
			
		},
		
		
	};
})(Zepto);

$(function() {
	H.mark.init();
});