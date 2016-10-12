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
	
	
	var num=getQueryString("num");
	//console.log(num)
	$("#data_img img").attr("src","img/hx/"+tibs_data[num].bjgImg);
	$("#data_p").html(tibs_data[num].wrods);
	
})
