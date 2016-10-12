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
	
	$('.upload_but').click(function(){
		
			if(j==0){
				dialog();
				return false;
			}
			diyCanvas.deactivate();
			var formdata = new FormData();
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
				url : "uploadwork",
				data:formdata,
				dataType : "json",
	        	contentType: false,
	        	processData: false,
				success : function(data) {
					if(bg){
						window.location.href="wx-weMakeShare1.html?workId="+data.workId;
					}else{
						window.location.href="wx-makeSuccess.html?workId="+data.workId;
					}
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
			
		})
			
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