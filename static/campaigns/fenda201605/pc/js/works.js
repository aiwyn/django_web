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
						if(DataList.length<=12){
							$(".buts").addClass('none');
						}else{
							$(".buts").removeClass('none');
						}
						totalPages=data.totalPages;
						Struct(data);
						
						var spanLength=$('.pagination');
						var str='';
						for(var i=0;i<totalPages;i++){
							str+="<span>"+(i+1)+"</span>";
						}
						spanLength.html(str);
						$(".pagination span").eq(page-1).addClass('swiper-active-switch');
						if(orderByVotes){
							for(var i=0;i<3;i++){
								$('.swiper-wrapper li').eq(i).append('<i><img src="/static/campaigns/fenda201605/pc/img/no'+(i+1)+'.png"/></i>')
							}
						}
						Init();
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
			
			
			
			function VoteAjax(workID,That){
				
				$.ajax({
					type : 'POST',
					async : true,
					url : "vote",
					data:{
						workId:workID
					},
					dataType : "json",
					success : function(data) {
										
							$('.pro_name1 span').html( parseInt(That.find(".tps").text())+1 );
							That.find('.tps').html(parseInt(That.find(".tps").text())+1)

					},
					error:function(jqXHR){
						$('.tpts').removeClass('none');
						return false;
					}
				});
				
			}
			
			
			
			function Struct(data){
				var Html='';
				var Data=data.workList;
				var c=0;
					for(var i=0;i<Math.ceil(Data.length/12);i++){
						var Ul="";
						var Li="";
						for(var j=0;j<12;j++){
							try{
								Li+="<li data-id="+c+" data-workId="+Data[c].workId+">\
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
									</li>";
								
								c++;
							}
							catch(e){
								
							}
						}
						Ul="<ul  class='swiper-slide singerUrl'>"+Li+"</ul>";
						Html+=Ul;
					};
				
				$('.swiper-wrapper').html(Html);
			}
	
	
		Ajax(1,12,"true");
		for(var i=0;i<3;i++){
			$('.swiper-wrapper li').eq(i).append('<i><img src="/static/campaigns/fenda201605/pc/img/no'+(i+1)+'.png"/></i>')
		}
		var byVotes='',byDate='';
		$('.radio input').bind("change",function(){
			if($('.rad1').prop('checked')){
				byVotes=true;
				byDate=false;
				Ajax(1,12,byVotes);
				
				
				
				$('.pagination span').eq(0).addClass('swiper-active-switch')
			}else{
					$('.swiper-wrapper').html("");
					byVotes=false;
					byDate=true;
					Ajax(1,12,byVotes,byDate);
					
					$('.pagination span').eq(0).addClass('swiper-active-switch')
				}
		})
	
		$('input[type=submit]').click(function(e){
			var submitText=$('input[name=pro_name]').val().trim();
			Ajax(1,12,false,false,submitText);
			e.preventDefault();
			return false;
			
		})
	
	
	
	
	$('.arrow-left').on('click', function(){
		page--;
		if(page<=1){
			page=1;
		}
		Ajax(page,12,byVotes,byDate);
		
	})
	$('.arrow-right').on('click', function(){
			page++;
			if(page>=totalPages){
				page=totalPages;
			}
			Ajax(page,12,byVotes,byDate);
			
	});
	
	
	
	
	
	
	
	function Init(){
		
		
		function Diolag(){
			//点击出现弹层
			$('.dialog_wrap').removeClass('none');
			$('.dialog').addClass('active');
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
		};
		
		var dataId='';
		var cp=0;
		$('.swiper-wrapper li').click(function(){
			var That=$(this);
			
			dataId=$(this).attr('data-id');
			var workDataId=$(this).attr('data-workId')
			$('.tu img').attr("src",DataList[dataId].workUrl)
			$('.pro_name1 span').html(DataList[dataId].workVotedCount);
			$('.No').html(DataList[dataId].workId);
			$('.work_name span').html(DataList[dataId].workName);
			$('.author span').html(DataList[dataId].authorName);
			$('.school_name span').html(DataList[dataId].authorSchool);
			Diolag();
			
			window._bd_share_config = {
							    "common": {
							        "bdSnsKey": {},
							        "bdText": "快来为他投一票吧",
							        "bdMini": "2",
							        "bdMiniList": false,
							        "bdPic": "",
							        "bdStyle": "0",
							        "bdSize": "24",
							        "bdUrl":"http://192.168.100.250:8000/fenda201605/mobile/details.html?worId="+workDataId
							        
							    },
							    "share": {}
							};
							with(document) 0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = 'http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion=' + ~(-new Date() / 36e5)];
			cp=0;
			$('.tpts').addClass('none');
			$(".vote").click(function(e){
				VoteAjax(workDataId,That);
				 e.preventDefault(); 
				 e.stopPropagation();
			})
			
		})
		}
	Init();

})
