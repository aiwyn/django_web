$(function(){
	var totalPages=0;
	var page=1;
	function Ajax(nowPage,pageRows,orderByVotes,orderByDate,searchKeyWords){
				$.ajax({
					type : 'POST',
					async : true,
					url : "fetchWorks",
					data:{
						nowPage:nowPage,
						pageRows:pageRows,
						orderByVotes:orderByVotes,
						orderByDate:orderByDate,
						searchKeyWords:searchKeyWords
					},
					dataType : "json",
					success : function(data) {
						 var dataList=data.workList;
						 totalPages=data.totalPages;
						 if(totalPages<=1&&dataList<9){
						 	$('.but_left').addClass('none');
						 	$('.but_right').addClass('none');
						 }else{
						 	$('.but_left').removeClass('none');
						 	$('.but_right').removeClass('none');
						 }
						console.log(data)
						 var str="";
						 for(var i=0;i<9;i++){
						 	str+="<li data-id="+dataList[i].workId+">\
									<em class='li_left'><img src='"+dataList[i].workUrl+"'/></em>\
									<div class='li_right'>\
										<p>编号:<span>no."+dataList[i].workId+"</span></p>\
										<p>尺码:<span>"+dataList[i].workVotedCount+"</span></p>\
										<p>票数:<span class='li_ps'>"+dataList[i].workVotedCount+"</span></p>\
										<p>排行:<span>"+dataList[i].authorSchool+"</span></p>\
									</div>\
								</li>";
						 }
						 
						 $('.ul_list').html(str);
						 
						 $('.ul_list li').bind("click",function(){
						 	var Index=$(this).index();
						 	$('.pro_img img').attr('src',dataList[Index].workUrl);
						 	$('.bh').text(dataList[Index].workId);
						 	$('.ps').text(dataList[Index].workVotedCount);
						 	$('.cc').text(dataList[Index].workId);
						 	$('.ph').text(dataList[Index].workId);
						 	$('.tp_but').attr('data-id',dataList[Index].workId);
						 	$('.tp_but').attr('data-eq',Index)
						 	$('.dialog').removeClass('none').addClass('active');
						 });
						 
						 $('.close').click(function(){
						 	$('.dialog').addClass('none');
						 });
						 
						 $('.tp_but').click(function(){
						 	var workId=$(this).attr('data-id');
						 	var Eq=$(this).attr('data-eq');
						 	$.ajax({
								type : 'POST',
								async : true,
								url : "vote",
								data:{
									workId:workId
								},
								dataType : "json",
								success : function(data) {
										$('.tp_but').addClass('active');
										setTimeout(function(){
											$('.tp_but').removeClass('active');
										},80);
										$('.ps').html( parseInt($('.ps').text())+1 );
										$('.ul_list li').eq(Eq).find('.li_ps').html(parseInt($('.ul_list li').eq(Eq).find('.li_ps').text())+1)
								},
								error:function(jqXHR){
									alert('今日投票次数已经用完');
									return false;
								}
							});
						 	
						 })
					},
					error:function(jqXHR){
						alert("数据请求失败，请稍后再试");
						return false;
					}
				});
				
		}
			
	Ajax(1,9,"true");
	
	// 搜索
	
	var byVotes='',byDate='';
	$('.sp1').click(function(){
		$(this).addClass('active').siblings('.sp2').removeClass('active');
		byVotes=true;
		byDate=false;
		Ajax(1,9,byVotes);
		
	});
	$('.sp2').click(function(){
		$(this).addClass('active').siblings('.sp1').removeClass('active');
		$('.swiper-wrapper').html("");
		byVotes=false;
		byDate=true;
		Ajax(1,9,byVotes,byDate);
	})
	
	$('.but_search').click(function(e){
			var submitText=$('input[name=number]').val().trim();
			Ajax(1,9,false,false,submitText);
			return false;
			
	})
	
	
	$('.but_left').on('click', function(){
		page--;
		if(page<=1){
			page=1;
		}
		Ajax(page,9,byVotes,byDate);
		
	})
	$('.but_right').on('click', function(){
			page++;
			if(page>=totalPages){
				page=totalPages;
			}
			Ajax(page,9,byVotes,byDate);
			
	});
	
	
	
	var Product={
		init:function(){
			//首页浮层
			$('.buts_1').click(function(){
				$('.index_dialog').removeClass('none');
				$('.index_dialogWrap').addClass('active');
			})
				//关闭弹层
			$('.close').hover(function(){
				$(this).css({transform: 'scale(1.1)'})
			},function(){
				$(this).css({transform: 'scale(1)'})
			})
			$('.close_a1').click(function(){
				$('.index_dialog').addClass('none');
				$('.index_dialogWrap').removeClass('active');
			});
		}
	};
	Product.init();
	
})


