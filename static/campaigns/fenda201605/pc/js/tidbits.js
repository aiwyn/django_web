$(function(){
	var cj={
		init:function(){
			//活动花絮列表数据配置
			var tibs_data=[
			{
				title:"标题111",
				smallImg:"img-1.png",
				bjgImg:"img-1-1.jpg",
				wrods:"花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮"
			},
			{
				title:"标题2222",
				smallImg:"img-1.png",
				bjgImg:"img-1-1.jpg",
				wrods:"花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮"
			},
			{
				title:"标题3333",
				smallImg:"img-1.png",
				bjgImg:"img-1-1.jpg",
				wrods:"花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮"
			},
			{
				title:"标题4444",
				smallImg:"img-1.png",
				bjgImg:"img-1-1.jpg",
				wrods:"花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮花絮"
			},
		];
		var Html='';
		for(var i=0;i<tibs_data.length;i++){
			Html+="<li data-id="+i+">\
					<i><img src='img/hx/"+tibs_data[i].smallImg+"'/></i>\
					<p>"+tibs_data[i].title+"</p>\
				</li>";
		};
		
		$('.tib_ul').append(Html);
		
		//点击出现弹层
		$('.tib_ul li').bind('click',function(){
			var this_index=$(this).attr('data-id');
			$('.dialog_wrap').removeClass('none');
			$('.dialog').addClass('active');
			$('.content').find('img').attr('src','img/hx/'+tibs_data[this_index].bjgImg);
			$('.content').find('h1').text(tibs_data[this_index].title);
			$('.content').find('p').html(tibs_data[this_index].wrods)
		})
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
			
			
		},
	};
	cj.init();
})