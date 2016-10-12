(function($) {
	H.mark = {
		buts_i:$('.buts i'),
		init: function() {
			This=this;
			This.buts_i.eq(0).addClass('active');
			This.getData();
			This.Click();
		},
		Click:function(){
			This=this;
			This.buts_i.click(function(){
				$(this).addClass('active').siblings('i').removeClass('active');
				var Ieq=$(this).index();
				if(Ieq==0){
					This.getData();	
					return false;
				}
				if(Ieq==1){
					This.getData();	
					return false;
				}
			})
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
			
		},
		getData:function(nowPage,pageRows,orderByVotes,orderByDate){
			
			$.ajax({
				type : 'POST',
				async : true,
				url : "fetchWorks",
				data:{
					nowPage:nowPage,
					pageRows:pageRows,
					orderByVotes:orderByVotes,
					orderByDate:orderByDate
				},
				dataType : "json",
				success : function(data) {
					var dataList=data.workList;
					var t = simpleTpl();
					for(var i=0;i<dataList.length;i++){
					
						t._('<li data-my='+i+' data-id='+dataList[i].workId+'>')
							._('<em><img src="'+dataList[i].workUrl+'"/></em>')
							._('<div class="pro_right">')
								._('<p>编号:<span>'+dataList[i].workName+'</span></p>')
								._('<p>尺码:<span>'+dataList[i].workId+'</span></p>')
								._('<p>投票:<span>'+dataList[i].workVotedCount+'</span></p>')
								._('<p>排行:<span>'+dataList[i].workVotedCount+'</span></p>')
							._('</div>')
						._('</li>')
					}
					
					$('.box_ul').html(t.toString());
					
					$('.box_ul li').bind('click',function(){
						var This_id=$(this).attr('data-id');
						if($(this).attr('data-my')/2==0){
							window.location.href='wx-myProduct.html?workId='+This_id;
						}else{
							window.location.href='wx-otherProduct.html?workId='+This_id;
						}
					});
					var box_h=$('.box_wrap').height();
					var box_ul=$('.box_ul').height();
					if(box_ul>box_h){
						$('.box_top').addClass('none');
						$('.box_top').addClass('none');
					}else{
						$('.box_top').removeClass('none');
						$('.box_top').removeClass('none');
					}
				},
				error:function(jqXHR){
					alert("数据请求失败，请稍后再试");
					return false;
				}
			});
			
			
		}
	};
})(Zepto);

$(function() {
	H.mark.init();
});