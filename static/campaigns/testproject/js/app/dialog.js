(function($) {
    H.dialog = {
    	 $container: $('body'),
        init: function() {
            var me = this;
            this.$container.delegate('.btn-close', 'click', function(e) {
                e.preventDefault();
                me.close();
            })
        },
        close: function() {
            $('.modal').addClass('none');
        },
        open: function(data) {
            if (this.$dialog) {
                this.$dialog.removeClass('none');
            } else {
                this.$dialog = $(this.tpl(data));
                H.dialog.$container.append(this.$dialog);
                
            }
        }, 
		flow:{
			$dialog: null,
			open: function(data) {
				console.log(data)
				H.dialog.open.call(this,data);
				this.event(data);
				var winW = $(window).width(),
					winH = $(window).height();
				var lotteryW = Math.round(winW * 0.94);
				var lotteryH = Math.round(lotteryW * 789 / 540);
				var lotteryT = Math.round((winH - lotteryH) / 2);
				$('#rp-dialog .open-rptip-dialog').css({
					//'width': lotteryW-30,
					'height': lotteryH,
					//'left': Math.round((winW - lotteryW) / 2)+15,
					'top': lotteryT
				});
			},
			close: function() {
				this.$dialog && this.$dialog.remove();
				this.$dialog=null;
			},
			event: function(data) {
				var me = this;
				console.log(H.index.hitprizes);
				this.$dialog.find('.btn-close').click(function(e) {
					e.preventDefault();
					me.close();
					//H.lottery.isCanShake = true;
				});
				
				$("#promptly").unbind("click").click(function(){
					
					if($('#promptly').hasClass('hasClick')){
						return false;
					}
					
					if ($('.u-name').val().trim() == "") {
						showTips("请填写姓名");
	                	return false;
		            };
		            if ($('.u-phone').val().trim() == "") {
		            	showTips("请填写手机号码！");
		                return false;
		            };
		            if (!/^\d{11}$/.test($('.u-phone').val())) {
		                showTips("这手机号，可打不通...");
		                return false;
		            };
		            if ($('.u-address').val().length < 5 || $('.u-address').val().length > 60) {
		            	showTips("地址长度应在5到60个字！");
	                    return false;
	                };
	                
	                var name = $.trim($('.u-name').val()),
	                	mobile = $.trim($('.u-phone').val()),
						address = $.trim($('.u-address').val());
						
					showLoading();
					
					$.ajax({
						type : "POST",
						async :false,
						url :"userinfo",
						data: {
							usrname:name,
							usrnum:mobile,
							usraddr:address,
							hitprizes:H.index.hitprizes,  // 所中奖项
							prizesid:H.index.prizesid,   // 具体奖项id
							prizeslvl:H.index.prizeslvl, //奖品等级
							userid:'None'                    //用户ID
						},
						dataType : "json",
						complete: function() {
							hideLoading();
						},
						success : function(data) {
							H.dialog.flow.success();
						},
						error:function(jqXHR){
							alert(jqXHR.responseText);
							return false;
						}
					});
					
					$("#promptly").addClass('hasClick');
					
				});
			},
			
			success:function(){
				$('.u-name').attr('readonly','readonly');
				$('.u-phone').attr('readonly','readonly');
				$('.u-address').attr('readonly','readonly');
				/*$(".cdd-btn-submit").addClass('none');*/
				
					$('.data_tt').html("以下是您的相关信息，敬请等待！！");
					setTimeout(function(){
						H.dialog.flow.close();
					},4000);
				
				$('.otherInfos1').addClass('none');
				$(".cdd-btn-submit").html('已领取').unbind('click').click(function(e){
					e.preventDefault();
					return false;
				});
				
				showTips("领取成功~");
				
			},
			
			update: function(rule) {},
			tpl: function(data) {
				var t = simpleTpl();
				t._('<section class="modal" id="rp-dialog">')
					._('<div class="dialog open-rptip-dialog dialog_animate" style="display: -webkit-box;-webkit-box-pack: center;-webkit-box-align: center;">')
						._('<a href="#" class="btn-close btn-close1" ></a>')
						._('<div class="rp-content" style="position:relative;">')
							//._('<img src="" style="width: 30%;">')
							._('<p class="otherInfos data_tt">'+data.hitprizes+'</p>')
							._('<p class="cj_p"><label for="input1"><img src="images/icon7.png"/>姓名:</label><input class="u-name" placeholder="" value="" id="input1"/></p>')
							._('<p  class="cj_p"><label for="input2"><img src="images/icon8.png"/>电话:</label><input class="u-phone" type="tel" placeholder="" value="" id="input2"/></p>')
							//._('<p  class="cj_p"><label for="input3"><img src="images/icon9.png"/>身份证号:</label><input class="u-idcade" type="number" placeholder=""  id="input3"/></p>')
							._('<p class="cj_p cj_mb"><label for="input4"><img src="images/icon10.png"/>地址:</label><input class="u-address" placeholder="" value="" id="input4"/></p>')
							._('<span class="cdd-btn-submit" id="promptly" >确认</span>')
						._('</div>')
					._('</div>')
				._('</section>');
				return t.toString();
			}
		},
		
    };
    
   
    
})(Zepto);

$(function() {
    H.dialog.init();
});
