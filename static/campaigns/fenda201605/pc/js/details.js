$(function(){
	
		
		with(document) 0[(getElementsByTagName('head')[0] || body).appendChild(createElement('script')).src = 'http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion=' + ~(-new Date() / 36e5)];
	var getQueryString = function( name ) {
	    var currentSearch = decodeURIComponent( location.search.slice( 1 ) );
	    if ( currentSearch != '' ) {
	        var paras = currentSearch.split( '&' );
	        for ( var i = 0, l = paras.length, items; i < l; i++ ) {
	            items = paras[i].split( '=' );
	            if ( items[0] === name) {
	                return items[1];
	            }
	        }
	        return '';
	    }
	    return '';
	};
	var workId=getQueryString("workId");
	

window._bd_share_config = {
							    "common": {
							        "bdSnsKey": {},
							        "bdText": "快来为他投一票吧",
							        "bdMini": "2",
							        "bdMiniList": false,
							        "bdPic": "",
							        "bdStyle": "0",
							        "bdSize": "24",
							        "bdUrl":"http://192.168.100.43:8020/HBuilderProject/fendaMobile/details.html?num="+workId
							        
							    },
							    "share": {}
							};


	
	$.ajax({
				type : 'POST',
				async : false,
				url : "fetchWork",
				data:{
					workId:workId
				},
				dataType : "json",
				success : function(data) {
					var data=data.work;
					$('.box_img img').attr("src",data.workUrl);
					$('.pro_name1 span').text(data.workVotedCount);
					$('.No').text("no."+data.workId);
					$('.author span').text(data.authorName);
					$('.school_name span').text(data.authorSchool);
					$('.work_name span').html(data.workName);
				},
				error:function(jqXHR){
					alert("数据请求失败，请稍后再试");
					return false;
				}
			});
	
})
		
			
			
		