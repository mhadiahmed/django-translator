$(document).ready(function(){
	var $myForm = $('.my-ajax-form');
	var $update = $('#update');
	$myForm.submit(function(event){
		event.preventDefault();
		var $formData = $myForm.serialize();
		var $thisURL = $myForm.attr('data-url') || window.loaction.href;
		$.ajax({
			method:'POST',
			url: $thisURL,
			data: $formData,
			success: handleSuccess,
			error: handleError,
		});
		function handleSuccess(data){
			if (data.laste == "") {
				$('#update').html("bad translate.");
			}else{
				$('#update').html(data.laste);
			}
			
			$myForm[0].reset();
		}
		function handleError(ThrowError){
			console.log(ThrowError);
		}
	});


});