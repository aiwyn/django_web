function start(w,h,W,H,BoxW) {
	var bg=false;
	if($('#bg').length){
		 var bg1 = document.getElementById('bg1');
		  var bg2 = document.getElementById('bg2');
		  diyCanvas.addKit(bg1);
		  diyCanvas2.addKit(bg2);
		  bg=true;
	}
    fabricCustom.loadControlImageObj(document.getElementById("controlImage"));
    var diyCanvas='';
	var diyCanvas2='';
//  if(W<=320 && H<=480){
//  	 diyCanvas= new DIYCanvas('canvas','kit', BoxW, h, 40, 0.4, 'red');
//  	 diyCanvas.addKit(bg1,w/20,h/1);
//  }
//  else if(W<=320 && H<=568){
//  	 diyCanvas= new DIYCanvas('canvas','kit',BoxW, h, 40, 0.5, 'red');
//  	 diyCanvas.addKit(bg1,w/20,h/1.5);
//  }
//  else if(W<=375){
//  	 diyCanvas= new DIYCanvas('canvas','kit', BoxW, h, 40, 0.7, 'red');
//  	 diyCanvas.addKit(bg1,w/10,h/3.4);
//  }
//  else if(W<=414){
//  	 diyCanvas= new DIYCanvas('canvas','kit', BoxW, h, 40, 0.8, 'red');
//  	 diyCanvas.addKit(bg1,w/20,h/3.9);
//  }
//  else if(W<768){
//  	 diyCanvas= new DIYCanvas('canvas','kit', BoxW, h, 40,0.9, 'red');
//  	 diyCanvas.addKit(bg1,w/24,h/4.5);
//  }
//  else  if(W>=768){
//  	 diyCanvas= new DIYCanvas('canvas','kit', BoxW, h, 40,1, 'red');
//  	 diyCanvas.addKit(bg1,w/20,h/3.8);
//  }else{
//  	diyCanvas= new DIYCanvas('canvas','kit',BoxW, h*0.8, 40, 0.5, 'red');
//  	 diyCanvas.addKit(bg1,w/10,h/3.5);
//  }
   diyCanvas= new DIYCanvas('canvas','kit',BoxW, h*0.9, 40, 0.5, 'red');
   diyCanvas2 = new DIYCanvas('canvas2','kit',BoxW, h*0.9, 40, 0.5, 'red');
//  	 diyCanvas.addKit(bg1,w/10,h/3.5);
   diyCanvas.activate();
	
		//cookie设置
	function setCookie(name,value){ 
	　　var exp = new Date(); 
	　　exp.setTime(exp.getTime() + 1*60*60*1000);//有效期1小时 
	　　document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString(); 
	}
	
	function getCookie(name){
	　　var arr = document.cookie.match(new RegExp("(^| )"+name+"=([^;]*)(;|$)"));
	　　if(arr != null)　　　　
	　　　　return unescape(arr[2]);
	　　return null;
	}
		
	if(getCookie('name')){
		$('.name').val(getCookie('name'))
	}
	if(getCookie('phone')){
		$('.phone').val(getCookie('phone'))
	}
	
	
	function dialog(){
		var str='<div class="dialog_img">\
					<div class="make_dialog">\
							<em><img src="img/make16.png"/></em>\
						</div>\
				</div>';
        	
        	$('body').append(str);
        	$('.dialog_img').addClass('active');
        	var Time=setTimeout(function(){
        		$('.dialog_img').remove()
        	},3000);
        	
        	$('.dialog_img').bind("click",function(){
				$('.dialog_img').remove();
				clearTimeout(Time);
			})
	}
	
	function dialog1(){
		var str='<div class="dialog_img dialog_img1">\
					<div class="make_dialog">\
							<em><img src="img/weMake2.png"/></em>\
						</div>\
				</div>';
        	
        	$('body').append(str);
        	$('.dialog_img').addClass('active');
        	var Time=setTimeout(function(){
        		$('.dialog_img').remove()
        	},3000);
        	
        	$('.dialog_img').bind("click",function(){
				$('.dialog_img').remove();
				clearTimeout(Time);
			})
	}
	
	
	var j=0;
	$('.list li').click(function(){
		j++;
	});
	
	
	var but=false;
	$('.filp').click(function(){
		if(but){
			diyCanvas.activate();
			$('.canvas_img').eq(0).removeClass('vH').siblings().addClass('vH');
		}else{
			diyCanvas2.activate();
			$('.canvas_img').eq(1).removeClass('vH').siblings().addClass('vH');
		}
		but=!but;
	})
	
	$('.empty').click(function(){
		if(!but){
			diyCanvas.clear();
		}else{
			diyCanvas2.clear();
		}
		j=0;
	})
	
	$('.upload_but').click(function(){
		if(j==0){
			dialog();
			return false;
		}else{
			dialog1();
			return false;
		}
				
	});
	
	
	var dressModel='';
	$('.main_left span').click(function(){
		dressModel=$(this).index();
		$(this).addClass('active').siblings('span').removeClass('active');
	})
	//选颜色
	var dressColor='';
	$('.main_right span').click(function(){
		dressColor=$(this).index();
		var Index=$(this).index();
		var IndexImg=0;
		if(Index==0) IndexImg=7;
		if(Index==1) IndexImg=3;
		if(Index==2) IndexImg=5;
		if(Index==3) IndexImg=1;
		$(this).addClass('active').siblings('span').removeClass('active');
		$('.canvas_img em').eq(0).find('img').attr('src',"img/yifu/"+IndexImg+".png");
		$('.canvas_img em').eq(1).find('img').attr('src',"img/yifu/"+(IndexImg+1)+".png");
	})
	
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
	var workId=getQueryString('workId') || 0;
	function GetAjax(){
			diyCanvas.deactivate();
			var formdata = new FormData();
			formdata.append("workId",workId);
			formdata.append("AuthorSize",dressModel);
			formdata.append("AuthorColors",dressColor);
			formdata.append("workImageFront",diyCanvas.toFeatureJson());
			formdata.append("workImageBack",diyCanvas2.toFeatureJson());
			formdata.append("workImageSFront",diyCanvas.toImageFile());
			formdata.append("workImageSBack",diyCanvas2.toImageFile());
			$.ajax({
				type : 'POST',
				async : false,
				timeout:2000,
				url : "uploadworks",
				data:formdata,
				dataType : "json",
	        	contentType: false,
	        	processData: false,
				success : function(data) {
					window.location.href="wx-weMakeSeed.html?workId="+data.workId;
					
				},
				error:function(jqXHR,textStatus){
					if(textStatus=="timeout"){  
                        alert("请求超时，请重试"); 
                        return false;
                    }
					alert("数据请求失败，请稍后再试");
					return false;
				}
			});
			
	};
		
		
	
	var shareUpdate = function () {
		var	IndexUrl=window.location.href;
		$.ajax({
				type: "POST",
				url: "http://fanta.kuh5.net/fenda201605/mobile/mobile_share",
				data: {
					url:IndexUrl,
					workId : workId
				},
				async: !0,
				dataType: "json",
				success: function(a) {
				},
				error: function(a, b) {}
		})
	}
	
	var WX_share=function(){
			
			var  TT='盆友，这次我真的傲娇的上天了！';
			var ImgUrl="";
			var Desc='不接收你的膝盖，只接受你的点赞。';
			var	IndexUrl=window.location.href;	
			var Url="http://fanta.kuh5.net/yiquan/mobile/wx-weMakeShare.html?worId=";
			$.ajax({
				type: "POST",
				url: "http://fanta.kuh5.net/yiquan/mobile/getSignPackage",
				data: {
					url:IndexUrl
				},
				async: !0,
				dataType: "json",
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
								imgUrl: ImgUrl,
								success:function(){
									shareUpdate();
									backFun();
								}
							});
							wx.onMenuShareAppMessage({
								title: TT,
								desc: Desc,
								link: Url,
								imgUrl:ImgUrl,
								success:function(){
									shareUpdate();
									GetAjax();
								}
							});
							wx.onMenuShareQQ({
								title: TT,
								desc: Desc,
								link: Url,
								imgUrl: ImgUrl,
								success:function(){
									shareUpdate();
									GetAjax();
								}
							});
							wx.onMenuShareWeibo({
								title: TT,
								desc: Desc,
								link: Url,
								imgUrl: ImgUrl,
								success:function(){
									shareUpdate();
									GetAjax();
								}
							});
							wx.onMenuShareQZone({
								title: TT,
								desc: Desc,
								link: Url,
								imgUrl: ImgUrl,
								success:function(){
									shareUpdate();
									GetAjax();
								}
							});
							wx.checkJsApi({
							   jsApiList: [
							   'addCard','onMenuShareTimeline','onMenuShareAppMessage','onMenuShareQQ','onMenuShareWeibo','onMenuShareQZone'
							   ],
							   success: function (res) {
							   		var t = res.checkResult.addCard;
							   		//判断checkJsApi 是否成功 以及 wx.config是否error
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
			
			
		





$(function() {
	var box_canvas=document.getElementById('box_canvas');
	var BoxW=box_canvas.offsetWidth;
    var W =window.screen.availWidth;
    var H =window.screen.availHeight;
    var w =window.screen.availWidth*0.8;
     var h =$('.canvas_img').height();
    
    start(w,h,W,H,BoxW);    
});