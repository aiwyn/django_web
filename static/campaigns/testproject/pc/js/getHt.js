$(function(){
	
	$.post('test',{headline:'test'},function(response){
		console.log(response);
		$('body').html(response)
	})
	
})
