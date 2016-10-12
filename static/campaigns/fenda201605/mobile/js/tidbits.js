$(function(){
	//console.log(Math.ceil(tibs_data.length/4))
	var Html='';
	var c=0;
		for(var i=0;i<Math.ceil(tibs_data.length/4);i++){
			var Ul="";
			var Li="";
			for(var j=0;j<4;j++){
				try{
					Li+="<li data-id="+c+">\
						<em><img src='img/hx/"+tibs_data[c].smallImg+"'/></em>\
						<p>"+tibs_data[c].title+"</p>\
					</li>";
					c++;
				}
				catch(e){
					
				}
			}
			Ul="<ul  class='swiper-slide singerUrl'>"+Li+"</ul>";
			Html+=Ul;
		};
		
		$('.swiper-wrapper').append(Html);
		
		
		
		
		
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
	
	$('.singerUrl li').bind("click",function(){
			console.log(111)
			var Li_num=$(this).attr("data-id");
			window.location.href="tidbits_open.html?num="+Li_num;
		})
})
