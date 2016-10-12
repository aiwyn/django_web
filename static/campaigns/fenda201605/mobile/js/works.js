$(function(){
		
			var DataList='';
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
						if(searchKeyWords){
							$(".buts").addClass('none');
						}else{
							$(".buts").removeClass('none');
						}
						DataList=data.workList;
						totalPages=data.totalPages;
						Struct(data);
						
						if(orderByVotes){
							for(var i=0;i<3;i++){
								$('.swiper-wrapper li').eq(i).append('<i><img src="/static/campaigns/fenda201605/mobile/img/'+(i+1)+'.png"/></i>')
							}
						}
						$('.singerUrl li').bind("click",function(){
							var workId=$(this).attr("data-workId");
							window.location.href="details.html?worId="+workId;
						});
						
					},
					error:function(jqXHR){
						if(jqXHR.status==400){
							alert(jqXHR.status+":"+jqXHR.responseJSON.errorMessage);
							return false;
						}
						if(jqXHR.status==404){
							alert(jqXHR.status+":"+jqXHR.responseJSON.errorMessage);
							return false;
						}
						if(jqXHR.status==500){
							alert(jqXHR.status+":"+jqXHR.responseJSON.errorMessage);
							return false;
						}
						if(jqXHR.status==501){
							alert(jqXHR.status+":"+jqXHR.responseJSON.errorMessage);
							return false;
						}
						alert("数据请求失败，请稍后再试");
						return false;
					}
				});
				
			}
		function Struct(data){
				var Data=data.workList;
				var c=0;
				var Ul="";
				var Li="";
						for(var j=0;j<4;j++){
							try{
								Li+="<li data-id="+c+" data-workId="+Data[c].workId+">\
										<a>\
										<em><img src='"+Data[c].workUrl+"' /></em>\
										<p class='pro_name'>\
										<span>"+Data[c].workId+"</span>\
										目前投票：<span class='tps'>"+Data[c].workVotedCount+"</span>\
										</p>\
										<aside class='datas'>\
										<p>作品名:<span>"+Data[c].workName+"</span></p>\
										<p>作者:<span>"+Data[c].authorName+"</span></p>\
										<p>院校名:<span>"+Data[c].authorSchool+"</span></p>\
										</aside>\
										</a>\
									</li>";
								
								c++;
							}
							catch(e){
								
							}
						}
				Ul="<ul  class='swiper-slide singerUrl' id='singerUrl'>"+Li+"</ul>";
				$('.swiper-wrapper').html(Ul);
				
			}
	
	
		Ajax(1,4,"true");
		for(var i=0;i<3;i++){
			$('.swiper-wrapper li').eq(i).append('<i><img src="/static/campaigns/fenda201605/mobile/img/'+(i+1)+'.png"/></i>')
		}
		var byVotes='',byDate='';
		$('.radio input').bind("change",function(){
			if($('.rad1').prop('checked')){
				byVotes=true;
				byDate=false;
				Ajax(1,4,byVotes);
				
			}else{
					$('.swiper-wrapper').html("");
					byVotes=false;
					byDate=true;
					Ajax(1,4,byVotes,byDate);
					
				}
		})
		
		
		$('input[type=submit]').click(function(e){
			var submitText=$('input[name=pro_name]').val().trim();
			Ajax(1,4,false,false,submitText);
			e.preventDefault();
			return false;
			
		})
		
		
		$('.arrow-left').on('click', function(){
			page--;
			if(page<=1){
				page=1;
			}
			Ajax(page,4,byVotes,byDate);
			
		})
		$('.arrow-right').on('click', function(){
				page++;
				if(page>=totalPages){
					page=totalPages;
				}
				Ajax(page,4,byVotes,byDate);
				
		});
		
		
		var Wem=$('.singerUrl li').eq(0).find('em').width();
		$('.singerUrl li em').height(Wem*1.2);
		var HH=$('.singerUrl li em').height();
		
	
	

})
