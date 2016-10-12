$(function(){
	
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
	
	
	
	function Diolag(){
		//点击出现弹层
		$('.dialog_wrap').removeClass('none');
		$('.dialog').addClass('active');
		//关闭弹层
		
		$('.close_a').click(function(){
			$('.dialog_wrap').addClass('none');
			$('.dialog').removeClass('active');
		})
	};
	
	var Tiem='';		
	$('.shake').click(function(){
		$('.dialog_wrap').removeClass("none")
		Tiem=setTimeout(function(){
			$('.dialog_wrap').addClass("none");
		},4000)
	})	
	$('.dialog_wrap').click(function(){
		$('.dialog_wrap').addClass("none");
		clearTimeout(Tiem);
	})
	var data_Url='';
	var workId=getQueryString("workId");
	
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
					data_Url="http://"+window.location.host+data.workUrl;
					$('.box_img img').attr("src",data.workUrl);
					$('.votedCount').text(data.workVotedCount);
					$('.wrokId').text(data.workId);
					$('.workName').text(data.workName);
					$('.author').text(data.authorName);
					$('.school').text(data.authorSchool);
					ShareFun(data_Url,workId);
				},
				error:function(jqXHR){
					alert("数据请求失败，请稍后再试");
					return false;
				}
			});
	
	
	function ShareFun(data_Url,workId){
	
	var WX_share=function(){
			
			var  TT='盆友，这次我真的傲娇的上天了！';
			var ImgUrl=data_Url;
			var Desc='不接收你的膝盖，只接受你的点赞。';
			var	IndexUrl=window.location.href;	
			var Url="http://fanta.kuh5.net/fenda201605/mobile/details.html?worId="+workId;
			$.ajax({
				type: "POST",
				url: "http://fanta.kuh5.net/fenda201605/mobile/getSignPackage",
				data: {
					url:IndexUrl
				},
				async: !0,
				dataType: "json",
				//jsonpCallback: "callbackWordTabletEntryHandler",
				success: function(a) {
					if (a) {
						var nonceStr = a["nonceStr"],
							timestamp = a["timestamp"],
							signature = a["signature"],
							mpappid = a["appId"];
						wx.config({
							debug:false,
							appId: mpappid,
							timestamp: timestamp,
							nonceStr: nonceStr,
							signature: signature,
							jsApiList: ["onMenuShareAppMessage", "onMenuShareTimeline", "onMenuShareQQ", "onMenuShareWeibo", "onMenuShareQZone","addCard","checkJsApi" ]
						});
						wx.ready(function() {
							
							wx.onMenuShareTimeline({
								title:TT ,
								desc: Desc,
								link: Url,
								imgUrl: ImgUrl
							});
							wx.onMenuShareAppMessage({
								title: TT,
								desc: Desc,
								link: Url,
								imgUrl:ImgUrl,
								success:function(){
									
								}
							});
							wx.onMenuShareQQ({
								title: TT,
								desc: Desc,
								link: Url,
								imgUrl: ImgUrl
							});
							wx.onMenuShareWeibo({
								title: TT,
								desc: Desc,
								link: Url,
								imgUrl: ImgUrl
							});
							wx.onMenuShareQZone({
								title: TT,
								desc: Desc,
								link: Url,
								imgUrl: ImgUrl
							});
							wx.checkJsApi({
							   jsApiList: [
							   'addCard','onMenuShareTimeline','onMenuShareAppMessage','onMenuShareQQ','onMenuShareWeibo','onMenuShareQZone'
							   ],
							   success: function (res) {
							   var t = res.checkResult.addCard;
							   //判断checkJsApi 是否成功 以及 wx.config是否error
							   if(t){
							   	
							   }
							   }
							  })
						})
					}
				},
				error: function(a, b) {}
			})
	};

var browser = {
    versions: function () {
        var u = navigator.userAgent, app = navigator.appVersion;
        return {         //移动终端浏览器版本信息
            trident: u.indexOf('Trident') > -1, //IE内核
            presto: u.indexOf('Presto') > -1, //opera内核
            webKit: u.indexOf('AppleWebKit') > -1, //苹果、谷歌内核
            gecko: u.indexOf('Gecko') > -1 && u.indexOf('KHTML') == -1, //火狐内核
            mobile: !!u.match(/AppleWebKit.*Mobile.*/), //是否为移动终端
            ios: !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/), //ios终端
            android: u.indexOf('Android') > -1 || u.indexOf('Linux') > -1, //android终端或uc浏览器
            iPhone: u.indexOf('iPhone') > -1, //是否为iPhone或者QQHD浏览器
            iPad: u.indexOf('iPad') > -1, //是否iPad
            webApp: u.indexOf('Safari') == -1 //是否web应该程序，没有头部与底部
        };
    }(),
    language: (navigator.browserLanguage || navigator.language).toLowerCase()
}


if (browser.versions.mobile) {//判断是否是移动设备打开。browser代码在下面
        var ua = navigator.userAgent.toLowerCase();//获取判断用的对象
        if (ua.match(/MicroMessenger/i) == "micromessenger") {
                //在微信中打开
               WX_share();	
        }
        if (ua.match(/WeiBo/i) == "weibo") {
                //在新浪微博客户端打开
        }
        if (ua.match(/QQ/i) == "qq") {
                //在QQ空间打开
        }
        if (browser.versions.ios) {
                //是否在IOS浏览器打开
        } 
        if(browser.versions.android){
                //是否在安卓浏览器打开
        }
	} 
	else {
	        //否则就是PC浏览器打开
	}
	
//分享	
	
	
	
	
}
	
})
		
			
			
		