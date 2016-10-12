(function($) {
	H.index = {
		turnplate:{
					restaraunts:[],				//大转盘奖品名称
					colors:[],					//大转盘奖品区块对应背景颜色
					outsideRadius:192,			//大转盘外圆的半径
					textRadius:155,				//大转盘奖品位置距离圆心的距离
					insideRadius:68,			//大转盘内圆的半径
					startAngle:0,				//开始角度
					
					bRotate:false				//false:停止;ture:旋转
		},
		prizesid:'',    ///奖品池中对应id
		usrprizes:'',   //如果中奖返回奖品编号 未中奖返回None
		cacheData:'',
		hitprizes:'',  //奖品名称
		prizeslvl:'',  //奖品等级
		init: function() {
			That=this;
			That.trunTable();
			That.drawRouletteWheel();
		},
		trunTable:function(){
			That=this;
			//console.log(timeTransform(999923312221) )
//			var getReact=function(){
//				showLoading();
//				$.ajax({
//					type : "GET",
//					async :false,
//					url :"js/app/JSON.js",
//					data: {},
//					dataType : "json",
//					complete: function() {
//						hideLoading();
//					},
//					success : function(data) {
//						That.turnplate.restaraunts=data.list;
//					}
//				});
//			}
//			
//			
			
			//动态添加大转盘的奖品与奖品区域背景颜色
			That.turnplate.restaraunts = [ "一等奖", "二等奖", "三等奖", "四等奖", "五等奖", "六等奖 ", "七等奖", "八等奖", "九等奖","十等奖","十一等奖","谢谢参与"];
			That.turnplate.colors = ["#FFF4D6", "#FFFFFF", "#FFF4D6", "#FFFFFF","#FFF4D6", "#FFFFFF", "#FFF4D6", "#FFFFFF","#FFF4D6", "#FFFFFF", "#FFF4D6", "#FFFFFF"];
		
			
			var rotateTimeOut = function (){
				jQuery('#wheelcanvas').rotate({
					angle:0,
					animateTo:2160,
					duration:8000,
					callback:function (){
						alert('网络超时，请检查您的网络设置！');
					}
				});
			};
		
			//旋转转盘 item:奖品位置; txt：提示语;
			var rotateFn = function (item, txt){
				var angles = item * (360 / That.turnplate.restaraunts.length) - (360 / (That.turnplate.restaraunts.length*2));
				if(angles<270){
					angles = 270 - angles; 
				}else{
					angles = 360 - angles + 270;
				}
				jQuery('#wheelcanvas').stopRotate();
				jQuery('#wheelcanvas').rotate({
					angle:0,
					animateTo:angles+1800,
					duration:8000,
					callback:function (){
						if(item==0){
							showTips("谢谢参与，再来一次");
						}else if(item!=0){
							H.dialog.flow.open(H.index.cacheData);
						}
						That.turnplate.bRotate = !That.turnplate.bRotate;
					}
				});
			};
			var buts=true;
			$('.pointer').click(function (){
				$.ajax({
					type : "POST",
					async :false,
					url :"cache",
					data: {
						activeid:"active1", //活动ID
						userid:'None'    //用户ID
					},
					dataType : "json",
					success : function(data) {
						if(data.result_code!=0){
							showTips(data.result_msg);
							return;
						}
						buts=true;
						H.index.cacheData=data;
						H.index.prizesid=data.prizesid;
						H.index.usrprizes=data.usrprizes;
						H.index.hitprizes=data.hitprizes;
						H.index.prizeslvl=data.prizeslvl;
					},
					error:function(jqXHR){
						alert(jqXHR.responseText);
						buts=false;
						return;
					}
				});
				if(!buts)return;
				if(That.turnplate.bRotate)return;
				That.turnplate.bRotate = !That.turnplate.bRotate;
				//获取随机数(奖品个数范围内)
				var item=H.index.prizeslvl;
				//奖品数量等于10,指针落在对应奖品区域的中心角度[252, 216, 180, 144, 108, 72, 36, 360, 324, 288]
				rotateFn(item);
				console.log(item);
			});
			function rnd(n, m){
				var random = Math.floor(Math.random()*(m-n+1)+n);
				return random;
			}
		},
		drawRouletteWheel:function() {    
			That=this;
			  var canvas = document.getElementById("wheelcanvas");    
			  if (canvas.getContext) {
				  //根据奖品个数计算圆周角度
				  var arc = Math.PI / (That.turnplate.restaraunts.length/2);
				  var ctx = canvas.getContext("2d");
				  //在给定矩形内清空一个矩形
				  ctx.clearRect(0,0,422,422);
				  //strokeStyle 属性设置或返回用于笔触的颜色、渐变或模式  
				  ctx.strokeStyle = "#FFBE04";
				  //font 属性设置或返回画布上文本内容的当前字体属性
				  ctx.font = '16px Microsoft YaHei';      
				  for(var i = 0; i < That.turnplate.restaraunts.length; i++) {       
					  var angle = That.turnplate.startAngle + i * arc;
					  ctx.fillStyle = That.turnplate.colors[i];
					  ctx.beginPath();
					  //arc(x,y,r,起始角,结束角,绘制方向) 方法创建弧/曲线（用于创建圆或部分圆）    
					  ctx.arc(211, 211, That.turnplate.outsideRadius, angle, angle + arc, false);    
					  ctx.arc(211, 211, That.turnplate.insideRadius, angle + arc, angle, true);
					  ctx.stroke();  
					  ctx.fill();
					  //锁画布(为了保存之前的画布状态)
					  ctx.save();   
					  //----绘制奖品开始----
					  ctx.fillStyle = "#E5302F";
					  var text = That.turnplate.restaraunts[i];
					  var line_height = 17;
					  //translate方法重新映射画布上的 (0,0) 位置
					  ctx.translate(211 + Math.cos(angle + arc / 2) * That.turnplate.textRadius, 211 + Math.sin(angle + arc / 2) * That.turnplate.textRadius);
					  
					  //rotate方法旋转当前的绘图
					  ctx.rotate(angle + arc / 2 + Math.PI / 2);
					  
					 
					  /** 下面代码根据奖品类型、奖品名称长度渲染不同效果，如字体、颜色、图片效果。(具体根据实际情况改变) **/
					  if(text.indexOf("M")>0){//流量包
						  var texts = text.split("M");
						  for(var j = 0; j<texts.length; j++){
							  ctx.font = j == 0?'bold 20px Microsoft YaHei':'16px Microsoft YaHei';
							  if(j == 0){
								  ctx.fillText(texts[j]+"M", -ctx.measureText(texts[j]+"M").width / 2, j * line_height);
							  }else{
								  ctx.fillText(texts[j], -ctx.measureText(texts[j]).width / 2, j * line_height);
							  }
						  }
					  }else if(text.indexOf("M") == -1 && text.length>6){//奖品名称长度超过一定范围 
						  text = text.substring(0,6)+"||"+text.substring(6);
						  var texts = text.split("||");
						  for(var j = 0; j<texts.length; j++){
							  ctx.fillText(texts[j], -ctx.measureText(texts[j]).width / 2, j * line_height);
						  }
					  }else{
						  //在画布上绘制填色的文本。文本的默认颜色是黑色
						  //measureText()方法返回包含一个对象，该对象包含以像素计的指定字体宽度
						  ctx.fillText(text, -ctx.measureText(text).width / 2, 0);
					  }
					   //添加对应图标
					  if(text.indexOf("闪币")>0){
						  var img= document.getElementById("shan-img");
						  img.onload=function(){  
							 // ctx.drawImage(img,-15,10);      
						  }; 
						  ctx.drawImage(img,-15,10);  
					  }else if(text.indexOf("谢谢参与")>=0){
						  var img= document.getElementById("sorry-img");
						  img.onload=function(){  
							 //ctx.drawImage(img,-15,10);      
						  };  
						  ctx.drawImage(img,-15,10);  
					  }
					  
					  
					  //把当前画布返回（调整）到上一个save()状态之前 
					  ctx.restore();
					  //----绘制奖品结束----
				  }     
			  } 
			},
	};
})(Zepto);

$(function() {
	
	H.index.init();
});